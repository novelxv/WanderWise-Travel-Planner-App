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
from src.ui.pages.budgeting import *
from src.controller.destinasi_controller import *
from src.controller.itinerary_controller import *
from src.ui.pages.listof_itineraries import *

class DestinationDetail(QWidget):
    def __init__(self, destination_id, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.destination_id = destination_id
        self.destinasi_controller = DestinasiController()
        self.itinerary_controller = ItineraryController()
        self.destinasi = self.destinasi_controller.get_destinasi_by_id(self.destination_id)
        self.itinerary = self.itinerary_controller.get_destinasi_detail(self.destination_id)

        # Main window size
        main_window_width = main_window.width()
        main_window_height = main_window.height()

        # Set the size of the widget
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(20)
        self.grid_layout.setContentsMargins(0, 50, 50, 0)

        # Adding the tag name x dest trip
        self.image_label = QLabel()
        imagedest = "img/icons/HelloDestTag.png"  # Path to your image
        self.image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(850, 450, QtCore.Qt.KeepAspectRatio))
        self.image_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)  # Align to top-left
        self.grid_layout.addWidget(self.image_label, 0, 0, 1, 1)

        # Tag label
        self.tag_label = QLabel("An exciting adventure starts on XX/XX/XX - XX/XX/XX")
        self.tag_label.setStyleSheet("font-size: 18px; font-weight: bold; background: transparent;")
        self.tag_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.grid_layout.addWidget(self.tag_label, 1, 0, 1, 1)

        # Top layout for buttons
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)  # Remove padding
        self.top_layout.setSpacing(30)  # Set spacing between buttons

        # Spacer to push buttons to the right
        self.top_layout.addStretch()

        # Add buttons
        self.back_button = BackButton()
        self.back_button.clicked.connect(lambda: self.main_window.stacked_widget.setCurrentIndex(3))
        self.edit_button = OvalButtonIcon("Edit", "img/icons/Pencil.png", "#FFA200", 40)
        self.delete_button = OvalButtonIcon("Delete", "img/icons/trash-can.png", "#FF5D00", 40)

        self.top_layout.addWidget(self.back_button, alignment=Qt.AlignTop)
        self.top_layout.addWidget(self.edit_button, alignment=Qt.AlignTop)
        self.top_layout.addWidget(self.delete_button, alignment=Qt.AlignTop)

        # Add top layout to a container widget to manage alignment
        self.top_button_container = QWidget()
        self.top_button_container.setLayout(self.top_layout)
        self.grid_layout.addWidget(self.top_button_container, 0, 1, 2, 1, alignment=Qt.AlignTop | Qt.AlignRight)

        # Scrollable area for itineraries
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedSize(400, 200)  # Set fixed size for the scrollable area

        # Container widget for scroll area
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)

        # Dummy data for itineraries
        for i in range(10):
            itinerary_label = QLabel(f"Itinerary {i + 1}: Activity details here")
            itinerary_label.setStyleSheet("font-size: 16px;")
            self.scroll_layout.addWidget(itinerary_label)

        self.scroll_area.setWidget(self.scroll_widget)
        self.grid_layout.addWidget(self.scroll_area, 2, 0, 1, 1)

        # Container for budget-related elements
        self.budget_container = QWidget()
        self.budget_layout = QVBoxLayout(self.budget_container)
        self.budget_layout.setAlignment(Qt.AlignRight)  # Align elements to the right

        # Budget goals remaining label
        self.budget_goals_label = QLabel("Goals remaining:")
        self.budget_goals_label.setStyleSheet("font-size: 20px; font-weight: bold; background: transparent;")
        self.budget_layout.addWidget(self.budget_goals_label, alignment=Qt.AlignRight)

        # Budget value label
        self.budget_value_label = QLabel("20,000,000")
        self.budget_value_label.setStyleSheet("font-size: 50px; font-weight: bold; background: transparent;")
        self.budget_layout.addWidget(self.budget_value_label, alignment=Qt.AlignRight)

        # Progress bar
        self.progress_bar_window = ProgressBarWindow(2000000, 20000000)
        self.progress_bar_window.setFixedSize(400, 30)  # Set fixed size for the progress bar
        self.budget_layout.addWidget(self.progress_bar_window, alignment=Qt.AlignRight)

        self.grid_layout.addWidget(self.budget_container, 2, 1, 1, 1, alignment=Qt.AlignTop)

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
        self.grid_layout.addWidget(self.bottom_button_container, 6, 0, 1, 2)

        # Create and add footer
        self.footer_label = QLabel("")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(125)  # Adjust the height of the footer as needed
        self.grid_layout.addWidget(self.footer_label, 7, 0, 1, 2)

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
        print("CEK KEGANTI GA TABUNGAN", self.destinasi.tabungan) # debug
        budgeting_page = BudgetingWindow(self.destinasi, self.main_window, self)
        self.main_window.stacked_widget.addWidget(budgeting_page)
        self.main_window.stacked_widget.setCurrentWidget(budgeting_page)

    def handle_itineraries_button_click(self):
        print("Itineraries button clicked!")
        itinerary_page = Listof_Itineraries(self.destination_id, self, self.main_window)
        self.main_window.stacked_widget.addWidget(itinerary_page)
        self.main_window.stacked_widget.setCurrentWidget(itinerary_page)

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
