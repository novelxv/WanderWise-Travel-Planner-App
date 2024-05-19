import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QMainWindow, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QFrame, QLabel, QGridLayout, QPushButton, QGroupBox
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon
from src.ui.components.dropdown.dropdown import DropDown
from src.ui.pages.form_edit_destination import FormEditDestination
from src.ui.components.popup.pop_up_confirm import ConfirmationDialog
from src.ui.components.progressbar.progressbar import ProgressBarWindow
from src.controller.destinasi_controller import *
from src.ui.components.backbutton.backbutton import BackButton

class DestinationDetail(QWidget):
    def __init__(self, destination_id, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.destination_id = destination_id

        # Main window size
        main_window_width = main_window.width()
        main_window_height = main_window.height()

        # Set the size of the widget
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(20)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        # Adding the tag name x dest trip
        self.image_label = QLabel()
        imagedest = "img/icons/HelloDestTag.png"  # Path to your image
        self.image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(800, 400, QtCore.Qt.KeepAspectRatio))
        self.image_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)  # Align to top-left
        self.grid_layout.addWidget(self.image_label, 0, 0, 1, 1)

        # Top layout for buttons
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(50, 50, 50, 50)  # Add padding (left, top, right, bottom)
        self.top_layout.setSpacing(30)  # Set spacing between buttons

        # Spacer to push buttons to the right
        self.top_layout.addStretch()

        # Add buttons
        self.back_button = BackButton()
        self.edit_button = OvalButtonIcon("Edit", "img/icons/Pencil.png", "#FFA200", 40)
        self.delete_button = OvalButtonIcon("Delete", "img/icons/trash-can.png", "#FF5D00", 40)

        self.top_layout.addWidget(self.back_button, alignment=Qt.AlignTop)
        self.top_layout.addWidget(self.edit_button, alignment=Qt.AlignTop)
        self.top_layout.addWidget(self.delete_button, alignment=Qt.AlignTop)

        # Add top layout to grid layout
        self.grid_layout.addLayout(self.top_layout, 0, 0, 1, 1)

        # Schedule label
        self.schedule_label = QLabel("THE PLANS")
        self.schedule_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.grid_layout.addWidget(self.schedule_label, 2, 0, 1, 1)

        # Schedule details
        schedule_text = "Amusement Park  07.00-11.30\n" \
                        "Tamfest          11.30-13.00\n" \
                        "Famous Museum    13.00-15.00\n" \
                        "Waterboom        15.30-20.00\n" \
                        "Upno             20.00-21.00"
        self.schedule_details = QLabel(schedule_text)
        self.schedule_details.setStyleSheet("font-size: 16px;")
        self.grid_layout.addWidget(self.schedule_details, 3, 0, 1, 1)

        # Progress bar container widget
        self.progress_container = QWidget()
        self.progress_container_layout = QVBoxLayout(self.progress_container)
        self.progress_bar_window = ProgressBarWindow(2000000, 20000000)
        self.progress_container_layout.addWidget(self.progress_bar_window)
        # Add the progress container to the grid layout at a specific position
        self.grid_layout.addWidget(self.progress_container, 3, 0, 1, 1)

        # Button layout for "Budgeting" and "Itineraries"
        self.bottom_button_layout = QHBoxLayout()
        self.bottom_button_layout.addStretch()  # Spacer to push buttons to the right
        self.budgeting_button = OvalButtonIcon("Budgeting", "img/icons/Budget.png", "#FFA200", 40)
        self.itineraries_button = OvalButtonIcon("Itineraries", "img/icons/Itinerary.png", "#FFA200", 40)
        self.bottom_button_layout.addWidget(self.budgeting_button)
        self.bottom_button_layout.addWidget(self.itineraries_button)
        self.bottom_button_layout.setSpacing(30)
        # Bottom button container widget
        self.bottom_button_container = QWidget()
        self.bottom_button_container.setLayout(self.bottom_button_layout)
        self.bottom_button_container.setContentsMargins(50, 50, 50, 50)  # Add padding (left, top, right, bottom)

        # Add the bottom button container to the grid layout at a specific position
        self.grid_layout.addWidget(self.bottom_button_container, 4, 0, 1, 1)

        # Create and add footer
        self.footer_label = QLabel("")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(125)  # Adjust the height of the footer as needed
        self.grid_layout.addWidget(self.footer_label, 5, 0, 1, 1)

        self.setLayout(self.grid_layout)

        # Connect button signals to handlers
        self.edit_button.clicked.connect(self.handle_edit_button_click)
        self.delete_button.clicked.connect(self.handle_delete_button_click)
        self.budgeting_button.clicked.connect(self.handle_budgeting_button_click)
        self.itineraries_button.clicked.connect(self.handle_itineraries_button_click)
        self.back_button.clicked.connect(self.handle_back_button_click)


    def handle_edit_button_click(self):
        print("Edit button clicked!")
        # Add your logic for edit button click here

    def handle_delete_button_click(self):
        print("Delete button clicked!")
        # Add your logic for delete button click here

    def handle_budgeting_button_click(self):
        print("Budgeting button clicked!")
        # Add your logic for budgeting button click here

    def handle_itineraries_button_click(self):
        print("Itineraries button clicked!")
        # Add your logic for itineraries button click here

    def handle_back_button_click(self):
        print("Back button clicked!")
        # Add your logic for back button click here


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(1024, 768)
    window = DestinationDetail(1, main_window)
    main_window.setCentralWidget(window)
    main_window.show()
    sys.exit(app.exec_())
