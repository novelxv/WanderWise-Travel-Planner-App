import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.components.boxofitinerary.boxofitinerary import *
from src.ui.components.addbutton.addbutton import *
from src.ui.pages.form_add_itinerary import FormAddItinerary
from src.ui.components.backbutton.backbutton import BackButton
from src.controller.itinerary_controller import ItineraryController
from src.controller.destinasi_controller import DestinasiController
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel

class Listof_Itineraries(QtWidgets.QMainWindow):
    def __init__(self, destination_id, before_page, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.stacked_widget = main_window.stacked_widget
        self.before_page = before_page
        self.destination_id = destination_id

        # Initialize ItineraryController to fetch data
        self.controller = ItineraryController()
        dest_controller = DestinasiController()
        destinasi = dest_controller.get_destinasi_by_id(destination_id)
        itineraries = self.controller.get_destinasi_detail(destination_id)

        trip = "Trip to " + str(destinasi.nama)  # Adjust as necessary based on your logic
        headers = [itinerary.tanggal.strftime('%A %d/%m') for itinerary in itineraries]
        list_of_places = [[itinerary.lokasi for itinerary in itineraries]]
        list_of_hours = [[f"{itinerary.waktu_mulai.strftime('%H:%M')}-{itinerary.waktu_selesai.strftime('%H:%M')}" for itinerary in itineraries]]

        main_window_width = main_window.width()
        main_window_height = main_window.height()
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a main layout for the central widget
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 40, 80, 0)  # Adjust margins to create space on the sides

        # Header layout to hold back button and header labels
        self.header_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        # BACK BUTTON
        self.back_button = BackButton()
        self.header_layout.addWidget(self.back_button, alignment=Qt.AlignRight)
        self.back_button.clicked.connect(self.go_back)

        # Add header ITINERARY and trip labels
        self.header_labels_layout = QtWidgets.QVBoxLayout()
        self.header_itinerary_label = QtWidgets.QLabel("ITINERARY")
        self.header_trip_label = QtWidgets.QLabel(trip)
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
                background: none;
                padding-left: 20px;
            }
        """)
        self.header_trip_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                padding-left: 20px;
            }
        """)
        self.header_labels_layout.addWidget(self.header_itinerary_label)
        self.header_labels_layout.addWidget(self.header_trip_label)
        
        self.header_layout.addLayout(self.header_labels_layout)
        self.header_layout.addStretch()  # Add stretch to push the header labels to the left

        # Add a blue line divider
        self.divider_line = QFrame()
        self.divider_line.setFrameShape(QFrame.HLine)
        self.divider_line.setFrameShadow(QFrame.Sunken)
        self.divider_line.setStyleSheet("color: #005A6D; background-color: #005A6D; height: 2px; border-radius: 5px;")
        self.main_layout.addWidget(self.divider_line)

        # Scroll area setup
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(scroll_area, alignment=Qt.AlignLeft)  # Align scroll area to the left
        self.setStyleSheet("background: transparent; border:none;")
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Hide vertical scroll bar
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Hide horizontal scroll
        scroll_content = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(scroll_content)
        self.grid_layout.setVerticalSpacing(40)
        self.grid_layout.setContentsMargins(20, 0, 0, 0)  # Add left margin to the grid layout
        self.grid_layout.setAlignment(Qt.AlignTop)  # Align items at the top of the grid layout
        scroll_area.setWidget(scroll_content)
        scroll_area.setFixedWidth(main_window_width - 100)  # Adjust width of the scroll area

        # Create ScheduleWidgets for each day's itinerary
        for index, (header, places, hours) in enumerate(zip(headers, list_of_places, list_of_hours)):
            schedule_widget = ScheduleWidget(header, places, hours)
            row = index // 2
            col = index % 2
            self.grid_layout.addWidget(schedule_widget, row, col, alignment=Qt.AlignLeft)  # Align each widget to the left
            for place_index in range(len(places)):
                schedule_widget.table_layout.itemAt(place_index).widget().clicked.connect(
                    lambda place_index=place_index, widget_index=index: self.handleScheduleWidgetRowClick(widget_index, place_index)
                )

        # Create and add footer
        self.footer_label = QLabel("")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(125)  # Adjust the height of the footer as needed
        self.main_layout.addWidget(self.footer_label)

        # Add the floating add button
        self.add_button = FloatingAddButton(self, position=(157, 170))
        self.add_button.clicked.connect(self.show_add_itinerary_form)
        self.add_button.setFloatingPosition()  # Ensure it is positioned correctly
        self.setStyleSheet("background: transparent; border:none;")
        self.resizeEvent = lambda event: self.adjust_positions(event)

    def adjust_positions(self, event):
        # Adjust positions of floating elements
        self.add_button.setFloatingPosition()

    def show_add_itinerary_form(self):
        self.add_destination_form = FormAddItinerary(self)
        self.add_destination_form.done_iti_signal.connect(self.on_done_signal)
        self.add_destination_form.setWindowModality(Qt.ApplicationModal)
        self.add_destination_form.setGeometry(40, 80, 800, 600)  # Set fixed size and position
        self.add_destination_form.show()

    def handleScheduleWidgetRowClick(self, widget_index, row_index):
        print(f"Clicked widget {widget_index}, row {row_index}")

    def go_back(self):
        self.stacked_widget.setCurrentWidget(self.before_page)

    def on_done_signal(self, itinerary_data):
        print("Received done signal with data:", itinerary_data) # debug
        self.controller.add_itinerary(self.destination_id, itinerary_data[0], itinerary_data[1], itinerary_data[2], itinerary_data[3], itinerary_data[4], itinerary_data[5], itinerary_data[6])
        self.refresh_itineraries()

    def refresh_itineraries(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        # Fetch the updated list of itineraries
        itineraries = self.controller.get_destinasi_detail(self.destination_id)

        # Rebuild the list of itineraries
        headers = [itinerary.tanggal.strftime('%A %d/%m') for itinerary in itineraries]
        list_of_places = [[itinerary.lokasi for itinerary in itineraries]]
        list_of_hours = [[f"{itinerary.waktu_mulai.strftime('%H:%M')}-{itinerary.waktu_selesai.strftime('%H:%M')}" for itinerary in itineraries]]

        for index, (header, places, hours) in enumerate(zip(headers, list_of_places, list_of_hours)):
            schedule_widget = ScheduleWidget(header, places, hours)
            row = index // 2
            col = index % 2
            self.grid_layout.addWidget(schedule_widget, row, col, alignment=Qt.AlignLeft)  # Align each widget to the left
            for place_index in range(len(places)):
                schedule_widget.table_layout.itemAt(place_index).widget().clicked.connect(
                    lambda place_index=place_index, widget_index=index: self.handleScheduleWidgetRowClick(widget_index, place_index)
                )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(1024, 768)
    destination_id = 1  # Example destination_id
    widget = Listof_Itineraries(destination_id, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())
