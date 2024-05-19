import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QFrame, QLabel, QHBoxLayout, QGridLayout, QGroupBox
from src.ui.components.ovalbutton.ovalbutton import *
from src.ui.components.backbutton.backbutton import BackButton
from src.controller.itinerary_controller import ItineraryController

class Itinerary_Details(QtWidgets.QMainWindow):
    def __init__(self, itinerary_id, main_window, before_page):
        super().__init__(main_window)
        self.main_window = main_window
        self.before_page = before_page
        # self.stacked_widget = main_window.stacked_widget

        # Initialize ItineraryController to fetch data
        controller = ItineraryController()
        itinerary = controller.get_itinerary_by_id(itinerary_id)

        location = itinerary.lokasi
        hours = f"{itinerary.waktu_mulai.strftime('%H:%M')} - {itinerary.waktu_selesai.strftime('%H:%M')}"
        location_desc = "This is a placeholder description for the location."  # Replace with actual description if available
        ticket = itinerary.biaya
        transport = itinerary.transportasi
        notes = itinerary.catatan

        main_window_width = main_window.width()
        main_window_height = main_window.height() - 150
        self.setStyleSheet("padding-top: 100px")
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
        self.back_button = BackButton()
        self.back_button.clicked.connect(self.go_back)

        self.edit_button = OvalButtonIcon("Edit", "img/icons/Pencil.png", "#FFA200", 40)
        self.delete_button = OvalButtonIcon("Delete", "img/icons/trash-can.png", "#FF5D00", 40)
        self.header_layout.addWidget(self.back_button)
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
        scroll_area.setWidget(scroll_content)

        # Adding the image at the top
        self.image_label = QLabel()
        imagedest = "img/icons/AmusementPark.png"
        self.image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(900, 300, QtCore.Qt.KeepAspectRatio))
        self.grid_layout.addWidget(self.image_label, 0, 0, 1, 1)
        self.image_label.setAlignment(Qt.AlignLeft)

        # Adding description
        self.description_label = QLabel(location_desc)
        self.description_label.setAlignment(Qt.AlignCenter)  # Align the description label to the center
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font: bold 20px; color: #000000; padding-left: 30px;")
        self.description_label.setMaximumWidth(500)  # Set a maximum width for the description label
        self.grid_layout.addWidget(self.description_label, 0, 1, 1, 1)
        
        # Adding Notes below the description
        if notes is None:
            self.notes_image_label = QLabel()
            imagedest = "img/icons/Notes.png"
            self.notes_image_label.setPixmap(QtGui.QPixmap(imagedest).scaled(650, 300, QtCore.Qt.KeepAspectRatio))
            self.notes_image_label.setStyleSheet("padding-left: 50px")
            self.grid_layout.addWidget(self.notes_image_label, 1, 1, 1, 1)
            self.notes_image_label.setAlignment(Qt.AlignLeft)
        else:
            notes_text = f"<b>Notes:</b><br> {notes}"  # Add "Notes:" before the actual notes content
            self.notes_label = QLabel(notes_text)
            self.notes_label.setWordWrap(True)
            self.notes_label.setStyleSheet("font-size: 25px; padding: 18px; background-color: #D9D9D9; border-radius: 10px;")
            self.grid_layout.addWidget(self.notes_label, 1, 1, 1, 1)
        
        # Adding Ticket Information
        self.ticket_info_label = QGroupBox("Tickets: ")
        self.ticket_info_label.setStyleSheet("font: bold 30px; padding-bottom: 20px; background: transparent")
        self.ticket_info_label.setAlignment(Qt.AlignLeft)
        self.ticket_layout = QVBoxLayout()
        self.ticket_label = QLabel(f"${ticket}")
        self.ticket_label.setStyleSheet("padding-bottom: 5px; font: regular 20px; background: #D9D9D9; border-radius: 10px; padding-right: 10px;")
        self.ticket_label.setFixedHeight(60)
        self.ticket_label.setFixedWidth(400)
        self.ticket_layout.addWidget(self.ticket_label)
        self.ticket_info_label.setLayout(self.ticket_layout)
        self.grid_layout.addWidget(self.ticket_info_label, 1, 0, 1, 2)  # Moved ticket information to row 2

        # Adding a group box for transportation information
        self.transport_group_box = QGroupBox("Transportation: ")
        self.transport_group_box.setStyleSheet("font: bold 30px; padding-top: 50px; padding-bottom: 30px; background: transparent")
        self.transport_group_box.setAlignment(Qt.AlignLeft)
        self.transport_layout = QVBoxLayout()
        self.transport_label = QGroupBox(transport)
        self.transport_label.setStyleSheet("padding-bottom: 5px; padding-top: 100px; font: regular 20px; background: #D9D9D9; border-radius: 10px; padding-right: 10px;")
        self.transport_label.setFixedHeight(60)
        self.transport_label.setFixedWidth(400)
        self.transport_layout.addWidget(self.transport_label)
        self.transport_group_box.setLayout(self.transport_layout)
        self.grid_layout.addWidget(self.transport_group_box, 2, 0, 1, 2)

        # Connect button signals to handlers
        self.back_button.clicked.connect(self.handle_back_button_click)
        self.edit_button.clicked.connect(self.handle_edit_button_click)
        self.delete_button.clicked.connect(self.handle_delete_button_click)

    def handle_edit_button_click(self):
        print("Edit button clicked!")
        # Add your logic for edit button click here

    def handle_delete_button_click(self):
        print("Delete button clicked!")
        # Add your logic for delete button click here

    def handle_back_button_click(self):
        print("Back button clicked!")
        # Add your logic for back button click here

    def resizeEvent(self, event):
        # Set the maximum width of the description label to 70% of the screen width
        screen_width = self.central_widget.width()
        max_width = int(screen_width * 0.7)
        self.description_label.setMaximumWidth(max_width)
        super(Itinerary_Details, self).resizeEvent(event)

    def go_back(self):
        self.main_window.stacked_widget.setCurrentWidget(self.before_page)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    itinerary_id = 1  # Example itinerary_id
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(1024, 768)
    widget = Itinerary_Details(itinerary_id, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())
