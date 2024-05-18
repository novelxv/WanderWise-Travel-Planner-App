import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFrame, QLabel
from PyQt5.QtGui import QPixmap
from src.ui.components.ovalbutton.ovalbutton import *
from src.ui.components.Form.form_box import FormBox

class FormAddItinerary(QWidget):
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
        path = os.path.abspath('img/icons/Add_Itinerary.png')
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
        form_box_location = FormBox("Amusement Park", self, 950)
        form_box_location.setParent(content_widget)
        form_box_location.move(100, 180)

        # add the FormBox For Start Time
        form_box_stime = FormBox("07.00", self, 400)
        form_box_stime.setParent(content_widget)
        form_box_stime.move(100, 290)

        # add the FormBox For End Time
        form_box_etime = FormBox("11.30", self, 400)
        form_box_etime.setParent(content_widget)
        form_box_etime.move(545, 290)

       # Add the FormBox instance For Cost/Ticket
        form_box_cost = FormBox("XX.XXX.XXX", self, 950)
        form_box_cost.setParent(content_widget)
        form_box_cost.move(100, 400)

        # Add the FormBox instance For description
        form_box_description = FormBox("Lorem ipsum dolor sit amet, consectetur...", self, 950)
        form_box_description.setParent(content_widget)
        form_box_description.move(100, 510)

        # Add the FormBox instance For notes
        form_box_notes = FormBox("Lorem ipsum dolor sit amet...", self, 950)
        form_box_notes.setParent(content_widget)
        form_box_notes.move(100, 625)

        # Add the oval button done for submitting the form
        oval_button = OvalButton("Done", "#69C99E", 35, self)
        oval_button.setParent(content_widget)
        oval_button.setFixedSize(149, 70)
        oval_button.move(450, 700)
        oval_button.clicked.connect(self.done_button_clicked)

        # Adding the scroll area to the main layout
        main_layout = QVBoxLayout(container)
        main_layout.addWidget(scroll_area)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the layout for the main widget
        self.setLayout(main_layout)
    
    def done_button_clicked(self):
        print("Done button clicked")

def main():
    app = QApplication(sys.argv)
    form_add_itinerary = FormAddItinerary()
    form_add_itinerary.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
