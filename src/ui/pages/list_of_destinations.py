from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget, QGridLayout, QStackedWidget
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from src.ui.components.addbutton.addbutton import FloatingAddButton
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon
import sys

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
        self.header_itinerary_label = QtWidgets.QLabel("All Destinations")
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