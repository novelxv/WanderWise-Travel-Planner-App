import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFrame, QLabel, QHBoxLayout
from src.ui.components.boxofitinerary.boxofitinerary import *
from src.ui.components.addbutton.addbutton import *
class Listof_Itineraries(QtWidgets.QMainWindow):
    def __init__(self, trip, headers, list_of_places, list_of_hours):
        super().__init__()
        self.setWindowTitle("Test Itinerary with Floating Add Button")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Add header ITINERARY and trip labels
        self.header_itinerary_label = QtWidgets.QLabel("ITINERARY")
        self.header_trip_label = QtWidgets.QLabel(trip)
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
        self.layout.addWidget(scroll_area)
        self.setStyleSheet("background-color: #FFF9ED; border:none;")
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Hide vertical scroll bar
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Hide horizontal scroll 
        scroll_content = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(scroll_content)
        self.grid_layout.setVerticalSpacing(40)  
        scroll_area.setWidget(scroll_content)

        # Create ScheduleWidgets for each day's itinerary
        for index, (header, places, hours) in enumerate(zip(headers, list_of_places, list_of_hours)):
            schedule_widget = ScheduleWidget(header, places, hours)
            row = index // 2
            col = index % 2
            self.grid_layout.addWidget(schedule_widget, row, col)
            schedule_widget.clicked.connect(lambda index=index: self.handleScheduleWidgetClick(index))
            schedule_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button = FloatingAddButton(self.central_widget, position=(10, 10))
        self.add_button.setFloatingPosition()

        self.resizeEvent = lambda event: self.add_button.setFloatingPosition()
    
    def handleScheduleWidgetClick(self, index):
        print("Clicked ScheduleWidget at index:", index)

    # def handleAddButtonClick(self):

    def handleButtonEditClick(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Example data
    headers = ["Monday 10/12", "Tuesday 11/12", "Wednesday 12/12", "Thursday 13/12", "Thursday 13/12"]
    list_of_places = [
        ["Amusement Park", "Tamfest", "Famous Museum", "Waterboom", "Upno"], #monday
        ["Zoo", "Botanical Garden", "Historical Museum", "Aquarium", "Maxx"], #tuesday
        ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
        ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
        ["Beach", "Water Sports", "Seafood Restaurant", "Night Market", "Cat Cafe"]
    ]
    list_of_hours = [
        ["07.00-11.30", "11.30-13.00", "13.00-15.00", "15.30-20.00", "20.00-21.00"],
        ["08.00-12.00", "12.30-14.00", "14.30-16.00", "16.30-19.00", "19.30-21.00"],
        ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
        ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
        ["09.00-12.00", "12.30-15.00", "15.30-18.00", "18.30-21.00", "21.30-23.00"]
    ]
    trip = "Bandung Trip 10/12/24 - 15/12/24"
    window = Listof_Itineraries(trip, headers, list_of_places, list_of_hours)
    window.show()
    sys.exit(app.exec_())
