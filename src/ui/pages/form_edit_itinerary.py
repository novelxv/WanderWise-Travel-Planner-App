import re
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFrame, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from src.ui.components.ovalbutton.ovalbutton import *
from src.ui.components.Form.form_box import FormBox
from src.ui.components.dropdown.dropdown import *
from src.ui.components.errors.error import ErrorPopup
from src.ui.components.calendar.calendar_picker import *

class FormEditItinerary(QWidget):
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
        path = os.path.abspath('img/icons/Edit_Itinerary.png')
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

        # Add the FormBox instance For Location
        self.form_box_location = FormBox("Amusement Park", self, 950)
        self.form_box_location.setParent(content_widget)
        self.form_box_location.move(100, 180)

        # add the FormBox For Start Time
        self.form_box_stime = FormBox("07.00", self, 400)
        self.form_box_stime.setParent(content_widget)
        self.form_box_stime.move(100, 290)

        # add the FormBox For End Time
        self.form_box_etime = FormBox("11.30", self, 400)
        self.form_box_etime.setParent(content_widget)
        self.form_box_etime.move(545, 290)

        # Add the FormBox instance For Cost/Ticket
        self.form_box_cost = FormBox("XX XXX XXX", self, 400)
        self.form_box_cost.setParent(content_widget)
        self.form_box_cost.move(100, 400)

        # add the FormBox For Date
        self.form_box_date = FormBox("2001-01-01", self, 400)
        self.form_box_date.setParent(content_widget)
        self.form_box_date.move(545, 400)
        calendar_picker = CalendarPicker()
        calendar_picker.dateSelected.connect(self.update_date)
        calendar_picker.setParent(content_widget)
        calendar_picker.move(805, 405)

        # Add the Dropdown instance For Transport
        self.drop_down = DropDown(option_type="transport", button_text = "Transport", parent=self)
        self.drop_down.setParent(content_widget)
        self.drop_down.move(90, 510)

        # Add the FormBox instance For notes
        self.form_box_notes = FormBox("Lorem ipsum dolor sit amet...", self, 950)
        self.form_box_notes.setParent(content_widget)
        self.form_box_notes.move(100, 625)

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
    
    def update_date(self, date):
        self.form_box_date.setText(date.toString("yyyy-MM-dd"))

    def done_button_clicked(self):
        if self.compare_times() == 0:
            err_popup = ErrorPopup("Invalid time format. Please enter time in HH.MM format.")
            err_popup.exec_()
            return
        elif self.compare_times() == 1:
            err_popup = ErrorPopup("Invalid Input. End time must be later than start time.")
            err_popup.exec_()
            return

        try:
            cost = int(self.form_box_cost.getText().replace(' ', ''))
        except ValueError:
            err_popup = ErrorPopup("Invalid Input. Must be an integer.")
            err_popup.exec_()
            return

        if self.drop_down.selected_option == None:
            err_popup = ErrorPopup("Invalid Input. All field must be filled in.")
            err_popup.exec_()
            return

        match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', self.form_box_date.getText())
        if not match:
            err_popup = ErrorPopup("Invalid date format. Please enter date in yyyy-mm-dd format.")
            err_popup.exec_()
            return

        itinerary_data = [
            self.form_box_location.getText(),
            self.form_box_date.getText(),
            self.form_box_stime.getText(),
            self.form_box_etime.getText(),
            cost,
            self.drop_down.selected_option,
            self.form_box_notes.getText()
        ]

        for i in range(len(itinerary_data)):
            if i != 4:
                if itinerary_data[i] == "":
                    err_popup = ErrorPopup("Invalid Input. All field must be filled in.")
                    err_popup.exec_()
                    return

        self.done_signal.emit(itinerary_data)
        print("Done button clicked", itinerary_data)
        self.close_form()

    def close_form(self):
        self.close()
    
    def compare_times(self):
        # Get the start time and end time from QLineEdit widgets
        start_time_str = self.form_box_stime.getText()
        end_time_str = self.form_box_etime.getText()

        # Validate and convert time strings to QTime objects
        start_time = self.parse_time(start_time_str)
        end_time = self.parse_time(end_time_str)

        if start_time is None or end_time is None:
            return 0

        # Compare the times
        if start_time > end_time:
            return 1

    def parse_time(self, time_str):
        # Use regular expression to validate the time format HH.MM
        match = re.match(r'^([01]?[0-9]|2[0-3])\.([0-5]?[0-9])$', time_str)
        if match:
            hours, minutes = int(match.group(1)), int(match.group(2))
            return QtCore.QTime(hours, minutes)
        return None

def main():
    app = QApplication(sys.argv)
    form_edit_itinerary = FormEditItinerary()
    form_edit_itinerary.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
