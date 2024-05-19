import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QFrame, QLabel, QHBoxLayout, QGridLayout, QPushButton, QWidget, QGroupBox
from src.ui.components.ovalbutton.ovalbutton import *

class Itinerary_Details(QtWidgets.QMainWindow):
    def __init__(self, location, hours, location_desc, ticket, transport, notes, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.stacked_widget = main_window.stacked_widget

        main_window_width = main_window.width()
        main_window_height = main_window.height()
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Header layout to include labels and buttons
        self.header_layout = QHBoxLayout()
        
        self.header_itinerary_label = QLabel(location)
        self.header_trip_label = QLabel(hours)
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                padding-left: 60px;
            }
        """)
        self.header_trip_label.setStyleSheet("""
            QLabel {
                font: bold 30px;
                text-align: left;
                padding-left: 60px;
            }
        """)

        # Add labels to header layout
        self.header_labels_layout = QVBoxLayout()
        self.header_labels_layout.addWidget(self.header_itinerary_label)
        self.header_labels_layout.addWidget(self.header_trip_label)
        self.header_layout.addLayout(self.header_labels_layout)

        # Spacer to push buttons to the right
        self.header_layout.addStretch()

        # Adding buttons to the header layout
        self.edit_button = OvalButtonIcon("Edit", "img/icons/Pencil.png", "#FFA200", 40)
        self.delete_button = OvalButtonIcon("Delete", "img/icons/trash-can.png", "#FF5D00", 40)
        self.header_layout.addWidget(self.edit_button)
        self.header_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.header_layout)

        self.divider_line = QFrame()
        self.divider_line.setFrameShape(QFrame.HLine)
        self.divider_line.setFrameShadow(QFrame.Sunken)
        self.divider_line.setStyleSheet("color: #005A6D; background-color: #005A6D; height: 2px; border-radius: 5px;")
        self.layout.addWidget(self.divider_line)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout.addWidget(scroll_area)
        self.setStyleSheet("background-color: #FFF9ED; border:none;")

        scroll_content = QtWidgets.QWidget()
        self.grid_layout = QGridLayout(scroll_content)
        self.grid_layout.setVerticalSpacing(40)
        scroll_area.setWidget(scroll_content)

        # Adding the image at the top
        self.image_label = QLabel()
        imagedest = "img/icons/AmusementPark.png"
        self.image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(1000, 1500, QtCore.Qt.KeepAspectRatio))
        self.grid_layout.addWidget(self.image_label, 0, 0, 1, 1)
        self.image_label.setAlignment(Qt.AlignLeft)

        # Adding description
        self.description_label = QLabel(location_desc)
        self.description_label.setAlignment(Qt.AlignCenter)  # Align the description label to the center
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font: bold 25px; color: #000000; padding-left: 30px;")
        self.description_label.setMaximumWidth(700)  # Set a maximum width for the description label
        self.grid_layout.addWidget(self.description_label, 0, 1, 1, 1)

        # Adding Notes below the description
        if notes is None:
            self.notes_image_label = QLabel()
            imagedest = "img/icons/Notes.png"
            self.notes_image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(800, 300, QtCore.Qt.KeepAspectRatio))
            self.notes_image_label.setStyleSheet("padding-left: 30px")
            self.grid_layout.addWidget(self.notes_image_label, 1, 1, 1, 1)
            self.notes_image_label.setAlignment(Qt.AlignLeft)
        else:
            self.notes_label = QLabel(notes)
            self.notes_label.setWordWrap(True)
            self.notes_label.setStyleSheet("font-size: 26px; padding: 20px; background-color: #FFFFFF;")
            self.grid_layout.addWidget(self.notes_label, 1, 1, 1, 1)
        # Adding Ticket Information
        self.ticket_info_label = QLabel(f"Tickets: {ticket}")
        self.ticket_info_label.setStyleSheet("font-size: 18px; padding: 20px;")
        self.grid_layout.addWidget(self.ticket_info_label, 2, 0, 1, 2)

        # Adding a group box for transportation information
        self.transport_group_box = QGroupBox("Transportation")
        self.transport_group_box.setStyleSheet("font-size: 18px; padding: 20px;")
        self.transport_group_box.setAlignment(Qt.AlignLeft)
        self.transport_layout = QVBoxLayout()
        self.transport_label = QLabel(f"Transport: {transport}")
        self.transport_layout.addWidget(self.transport_label)
        self.transport_group_box.setLayout(self.transport_layout)
        self.grid_layout.addWidget(self.transport_group_box, 3, 0, 1, 1)


        # Connect button signals to handlers
        self.edit_button.clicked.connect(self.handle_edit_button_click)
        self.delete_button.clicked.connect(self.handle_delete_button_click)

    def handle_edit_button_click(self):
        print("Edit button clicked!")
        # Add your logic for edit button click here

    def handle_delete_button_click(self):
        print("Delete button clicked!")
        # Add your logic for delete button click here

    def resizeEvent(self, event):
        # Set the maximum width of the description label to 70% of the screen width
        screen_width = self.central_widget.width()
        max_width = int(screen_width * 0.7)
        self.description_label.setMaximumWidth(max_width)
        super(Itinerary_Details, self).resizeEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tickets = 900
    transport = "Taxi"
    notes = "Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes Ini notes"
    desc = "One attraction that we definitely can't miss is the stunning natural wonder, XXX Falls. Tucked away in the heart of the forest, these majestic falls cascade down in a breathtaking display of nature's power and beauty. We can take a leisurely hike through the lush trails surrounding the falls, listening to the soothing sounds of rushing water and birdsong. And when we reach the viewing platforms, we'll be treated to panoramic vistas of the falls, with rainbows dancing in the mist. After experiencing the awe-inspiring beauty of XXX Falls, we can immerse ourselves in the rich cultural heritage of the region by visiting the historic XXX Village. It's sure to be an unforgettable journey filled with adventure, natural beauty, and cultural discovery."
    hours = "07.00 - 10.00"
    location = "AMUSEMENT PARK"
    window = Itinerary_Details(location, hours, desc, tickets, transport, None)
    window.show()
    sys.exit(app.exec_())
