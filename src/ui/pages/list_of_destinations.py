from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget
from src.ui.components.addbutton.addbutton import FloatingAddButton
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon
from src.ui.pages.form_add_destination import FormAddDestination
import sys
from PyQt5.QtCore import Qt

class ListOfDestinations(QWidget):
    def __init__(self, destinations, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.destinations = destinations
        self.stacked_widget = main_window.stacked_widget
        self.visible_destinations = self.destinations

        # Main window size
        main_window_width = main_window.width()
        main_window_height = main_window.height()

        # Set the size of the widget
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        # Header
        self.header_itinerary_label = QtWidgets.QLabel("ALL DESTINATIONS")
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
            }
        """)

        # Create a layout for the buttons
        idea_button = OvalButtonIcon("Idea", None, "#C5E5C0", 40)
        plan_button = OvalButtonIcon("Plan", None, "#FFCF52", 40)
        booked_button = OvalButtonIcon("Booked", None, "#FF5D00", 40)
        done_button = OvalButtonIcon("Done", None, "#00A6FF", 40)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.setSpacing(10)  # Set spacing between buttons

        buttons_layout.addWidget(idea_button)
        buttons_layout.addWidget(plan_button)
        buttons_layout.addWidget(booked_button)
        buttons_layout.addWidget(done_button)

        # Create a container for the buttons
        buttons_container = QtWidgets.QWidget()
        buttons_container.setLayout(buttons_layout)
        buttons_container.setContentsMargins(0, 0, 150, 0)  # Add right margin to prevent cutting off

        # Add spacer to push the buttons to the right
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.header_itinerary_label)
        top_layout.addStretch()  # Push the buttons to the right
        top_layout.addWidget(buttons_container)

        # Main layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(top_layout)
        
        spacer = QSpacerItem(800, 800, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout.addItem(spacer)
        
        self.setLayout(self.layout)

        # Add the floating add button
        self.add_button = FloatingAddButton(self, position=(20, 20))
        self.add_button.clicked.connect(self.show_add_destination_form)
        
    def show_add_destination_form(self):
        self.add_destination_form = FormAddDestination(self)
        self.add_destination_form.setWindowModality(Qt.ApplicationModal)
        self.add_destination_form.setGeometry(40, 80, 800, 600)  # Set fixed size and position
        self.add_destination_form.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(800, 600)  # Example size for the main window
    destinations = []  # Example destinations list
    widget = ListOfDestinations(destinations, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())
