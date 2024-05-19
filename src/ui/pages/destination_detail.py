from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QWidget, QScrollArea
from src.ui.components.addbutton.addbutton import FloatingAddButton
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon
from src.ui.components.destinationscard.destinationscard import CustomButton
from src.ui.pages.form_add_destination import FormAddDestination
import sys
from PyQt5.QtCore import Qt
from src.controller.destinasi_controller import *

class DestinationDetail(QWidget):
    def __init__(self, destination_id, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.destination_id = destination_id
        self.stacked_widget = main_window.stacked_widget

        # Main window size
        main_window_width = main_window.width()
        main_window_height = main_window.height()

        # Set the size of the widget
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        # Header
        self.header_itinerary_label = QLabel("ALL DESTINATIONS")
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
                background: none;
            }
        """)

        # Create a layout for the buttons
        idea_button = OvalButtonIcon("Idea", None, "#C5E5C0", 40)
        plan_button = OvalButtonIcon("Plan", None, "#FFCF52", 40)
        booked_button = OvalButtonIcon("Booked", None, "#FF5D00", 40)
        done_button = OvalButtonIcon("Done", None, "#00A6FF", 40)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)  # Set spacing between buttons

        buttons_layout.addWidget(idea_button)
        buttons_layout.addWidget(plan_button)
        buttons_layout.addWidget(booked_button)
        buttons_layout.addWidget(done_button)

        # Create a container for the buttons
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_layout)
        buttons_container.setContentsMargins(0, 0, 150, 0)  # Add right margin to prevent cutting off

        # Add spacer to push the buttons to the right
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.header_itinerary_label)
        top_layout.addStretch()  # Push the buttons to the right
        top_layout.addWidget(buttons_container)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.addLayout(top_layout)

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        # Scroll content layout
        self.grid_layout = QtWidgets.QGridLayout(scroll_content)
        self.grid_layout.setHorizontalSpacing(60)  # Set horizontal spacing between cards
        self.grid_layout.setVerticalSpacing(30)    # Set vertical spacing between cards
        self.grid_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(800, 600)  # Example size for the main window
    widget = DestinationDetail(1, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())