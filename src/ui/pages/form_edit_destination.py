import re
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFrame, QLabel
from PyQt5.QtGui import QPixmap
from src.ui.components.calendar.calendar_picker import *
from src.ui.components.dropdown.dropdown import *
from src.ui.components.ovalbutton.ovalbutton import *
from src.ui.components.Form.form_box import FormBox
from src.ui.components.errors.error import ErrorPopup

class FormEditDestination(QWidget):
    done_signal = pyqtSignal(list)  # Ubah sinyal untuk mengirimkan data sebagai list

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.stacked_widget = parent.stacked_widget if parent else None

        # Set size if parent is not provided
        parentWidth = 1214
        parentHeight = 793

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)
        self.file_name = ""

        # Set background image
        path = os.path.abspath('img/icons/Edit_Destination.png')
        if not os.path.exists(path):
            print(f"Image not found at {path}")
        else:
            print(f"Image found at {path}")

        # Create background label
        bgLabel = QLabel(self)
        pixmap = QPixmap(path)
        bgLabel.setPixmap(pixmap)
        bgLabel.setScaledContents(True)
        bgLabel.setGeometry(0, 0, self.width(), self.height())

        # Create a container widget to hold the scroll area
        container = QWidget(self)
        container.setGeometry(0, 0, self.width(), self.height())
        container.setStyleSheet("background: transparent;")

        # SCROLL AREA
        scroll_area = QScrollArea(container)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background: transparent;")

        # CONTENT WIDGET
        content_widget = QWidget()
        content_widget.setStyleSheet("background: transparent;")
        content_widget.setMinimumWidth(scroll_area.width())
        scroll_area.setWidget(content_widget)

        # add the FormBox and CalendarPicker widget For Start Date
        self.form_box_sdate = FormBox("01/01/01", self, 400)
        self.form_box_sdate.setParent(content_widget)
        self.form_box_sdate.move(100, 180)
        calendar_picker_start = CalendarPicker()
        calendar_picker_start.dateSelected.connect(self.update_start_date)
        calendar_picker_start.setParent(content_widget)
        calendar_picker_start.move(360, 185)

        # add the FormBox and CalendarPicker widget For End Date
        self.form_box_edate = FormBox("02/01/01", self, 400)
        self.form_box_edate.setParent(content_widget)
        self.form_box_edate.move(545, 180)
        calendar_picker_end = CalendarPicker()
        calendar_picker_end.dateSelected.connect(self.update_end_date)
        calendar_picker_end.setParent(content_widget)
        calendar_picker_end.move(805, 185)

        # Add the FormBox instance For destination
        self.form_box_destination = FormBox("Jakarta", self, 950)
        self.form_box_destination.setParent(content_widget)
        self.form_box_destination.move(100, 290)

        # Add DropDown instance For Category
        self.drop_down = DropDown(option_type="category", button_text = "Category", parent=self)
        self.drop_down.setParent(content_widget)
        self.drop_down.move(90, 405)

        # Add the FormBox instance For savings
        self.form_box_savings = FormBox("XX XXX XXX", self, 950)
        self.form_box_savings.setParent(content_widget)
        self.form_box_savings.move(100, 510)

        # Add the FormBox instance For budget
        self.form_box_budget = FormBox("XX XXX XXX", self, 950)
        self.form_box_budget.setParent(content_widget)
        self.form_box_budget.move(100, 625)

        # Add the oval button done for submitting the form
        oval_button_done = OvalButton("Done", "#69C99E", 35, self)
        oval_button_done.setParent(content_widget)
        oval_button_done.setFixedSize(149, 70)
        oval_button_done.move(350, 700)
        oval_button_done.clicked.connect(self.done_button_clicked)

        # Add the cancel button for closing the form
        oval_button_cancel = OvalButton("Close", "#FF5D00", 35, self)
        oval_button_cancel.setParent(content_widget)
        oval_button_cancel.setFixedSize(149, 70)
        oval_button_cancel.move(500, 700)
        oval_button_cancel.clicked.connect(self.close_form)

        # Adding the scroll area to the main layout
        main_layout = QVBoxLayout(container)
        main_layout.addWidget(scroll_area)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the layout for the main widget
        self.setLayout(main_layout)
    
    def update_start_date(self, date):
        self.form_box_sdate.setText(date.toString("yyyy-MM-dd"))

    def update_end_date(self, date):
        self.form_box_edate.setText(date.toString("yyyy-MM-dd"))
    
    def done_button_clicked(self):
        if self.compare_dates() == 0:
            err_popup = ErrorPopup("Invalid date format. Please enter date in yyyy-mm-dd format.")
            err_popup.exec_()
            return
        elif self.compare_dates() == 1:
            err_popup = ErrorPopup("Invalid Input. End date must be later than start date.")
            err_popup.exec_()
            return

        try:
            budget = int(self.form_box_budget.getText().replace(' ', ''))
        except ValueError:
            err_popup = ErrorPopup("Invalid Input. Must be an integer.")
            err_popup.exec_()
            return
        
        try:
            savings = int(self.form_box_savings.getText().replace(' ', ''))
        except ValueError:
            err_popup = ErrorPopup("Invalid Input. Must be an integer.")
            err_popup.exec_()
            return

        if self.drop_down.selected_option == None:
            err_popup = ErrorPopup("Invalid Input. All field must be filled in.")
            err_popup.exec_()
            return

        destination_data = [
            self.form_box_destination.getText(),
            self.drop_down.selected_option,
            self.form_box_sdate.getText(),
            self.form_box_edate.getText(),
            budget,
            savings
        ]

        for i in range(len(destination_data)-2):
            if destination_data[i] == "":
                err_popup = ErrorPopup("Invalid Input. All field must be filled in.")
                err_popup.exec_()
                return

        self.done_signal.emit(destination_data)
        print("Done button clicked", destination_data)
        self.close_form()

    def close_form(self):
        self.close()

    def compare_dates(self):
        # Get the start date and end date from QLineEdit widgets
        start_date_str = self.form_box_sdate.getText()
        end_date_str = self.form_box_edate.getText()

        # Validate and convert date strings to QDate objects
        start_date = self.parse_date(start_date_str)
        end_date = self.parse_date(end_date_str)

        if start_date is None or end_date is None:
            return 0

        # Compare the dates
        if start_date > end_date:
            return 1

    def parse_date(self, date_str):
        # Use regular expression to validate the date format yyyy-mm-dd
        match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_str)
        if match:
            year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return QtCore.QDate(year, month, day)
        return None

def main():
    app = QApplication(sys.argv)
    form_edit_destination = FormEditDestination()
    form_edit_destination.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()