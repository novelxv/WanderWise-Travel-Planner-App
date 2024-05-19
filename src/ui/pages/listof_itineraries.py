import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.components.boxofitinerary.boxofitinerary import *
from src.ui.components.addbutton.addbutton import *
from src.ui.pages.form_add_itinerary import *

class Listof_Itineraries(QtWidgets.QMainWindow):
    def __init__(self, trip, headers, list_of_places, list_of_hours, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.stacked_widget = main_window.stacked_widget

        main_window_width = main_window.width()
        main_window_height = main_window.height()
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(10, 40, 80, 0)  # Adjust margins to create space on the sides

        # Add header ITINERARY and trip labels
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
                font: bold 35px ;
                text-align: left;
                padding-left: 20px;
            }
        """)

        self.layout.addWidget(self.header_itinerary_label)
        self.layout.addWidget(self.header_trip_label)

        # Add a blue line divider
        self.divider_line = QFrame()
        self.divider_line.setFrameShape(QFrame.HLine)
        self.divider_line.setFrameShadow(QFrame.Sunken)
        self.divider_line.setStyleSheet("color: #005A6D; background-color: #005A6D; height: 2px; border-radius: 5px;")
        self.layout.addWidget(self.divider_line)

        # Scroll area setup
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout.addWidget(scroll_area, alignment=Qt.AlignLeft)  # Align scroll area to the left
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
            schedule_widget.table_layout.itemAt(index).widget().clicked.connect(lambda i=index, r=schedule_widget.table_layout.itemAt(index).widget().index: self.handleScheduleWidgetRowClick(i, r))

        # Create and add footer
        self.footer_label = QLabel("")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(125)  # Adjust the height of the footer as needed
        self.layout.addWidget(self.footer_label)

        # Add the floating add button
        self.add_button = FloatingAddButton(self, position=(157, 170))
        self.add_button.clicked.connect(self.show_add_itinerary_form)
        self.add_button.setFloatingPosition()  # Ensure it is positioned correctly
        self.setStyleSheet("background: transparent; border:none;")
        self.resizeEvent = lambda event: self.add_button.setFloatingPosition()

    def show_add_itinerary_form(self):
        self.add_destination_form = FormAddItinerary(self)
        self.add_destination_form.setWindowModality(Qt.ApplicationModal)
        self.add_destination_form.setGeometry(40, 80, 800, 600)  # Set fixed size and position
        self.add_destination_form.show()

    def handleScheduleWidgetRowClick(self, widget_index, row_index):
        print(f"Clicked widget {widget_index}, row {row_index}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(1024, 768)
    headers = ["Monday 10/12", "Tuesday 11/12"]
    list_of_places = [
        ["Amusement Park", "Tamfest", "Famous Museum", "Waterboom", "Upno", "Upno2"],
        ["Park", "Mall", "Museum", "Aquarium", "Zoo", "Beach"]
    ]
    list_of_hours = [
        ["07.00-11.30", "11.30-13.00", "13.00-15.00", "15.30-20.00", "20.00-21.00", "20.00-21.00"],
        ["08.00-10.00", "10.00-12.00", "12.00-14.00", "14.00-16.00", "16.00-18.00", "18.00-20.00"]
    ]
    trip = "Trip to Wonderland"
    widget = Listof_Itineraries(trip, headers, list_of_places, list_of_hours, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())
