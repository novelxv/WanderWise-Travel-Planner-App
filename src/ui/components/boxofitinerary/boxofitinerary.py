from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class ScheduleWidget(QtWidgets.QWidget):
    def __init__(self, header, places, hours, parent=None):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        # Set the border for the entire ScheduleWidget
        self.setStyleSheet("""
            QWidget {
                border-bottom: 0px;
                background-color: #FFF9ED;
            }
        """)

        # Header Tanggal
        self.header_label = QtWidgets.QLabel(header)
        self.header_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.header_label.setStyleSheet("""
            QLabel {
                background-color: #C36F0C;
                color: black;
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border-top: 5px solid;
                border-left: 5px solid;
                border-right: 5px solid;
            }
        """)
        self.main_layout.addWidget(self.header_label)

        # Table widget
        self.table_widget = QtWidgets.QWidget()
        self.table_layout = QtWidgets.QVBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setSpacing(0)
        self.table_widget.setLayout(self.table_layout)
        self.table_widget.setStyleSheet("""
            QWidget {
                background-color: #FFF9ED;
                border-left: 5px solid;
                border-right: 5px solid;
            }
        """)
        self.main_layout.addWidget(self.table_widget)

        # Populate the table

        for i, (place, hour) in enumerate(zip(places, hours)):
            row_widget = QtWidgets.QWidget()
            row_layout = QtWidgets.QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            row_widget.setLayout(row_layout)
        
            place_label = QtWidgets.QLabel(place)
            hour_label = QtWidgets.QLabel(hour)
            place_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            hour_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            place_label.setWordWrap(True)
            hour_label.setWordWrap(True)
            place_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            hour_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            
            
            if i % 2 == 0:
                row_widget.setStyleSheet("background-color: #FFF9ED; padding: 10px; margin: 0px;  border-radius: 0px")
            else:
                row_widget.setStyleSheet("background-color: #FFBE00; padding: 10px; margin: 0px;  border-radius: 0px")
            row_layout.addWidget(place_label)
            row_layout.addWidget(hour_label)
            if i == len(places) - 1:
                row_widget.setStyleSheet(row_widget.styleSheet() + "; border-bottom: 5px solid; ")
            place_label.setStyleSheet("border-right: 0px solid;")
            hour_label.setStyleSheet("border-left: 0px solid;")
            self.table_layout.addWidget(row_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    header = "Monday 10/12"
    places = ["Amusement Pasadiasbdjashbjhsark", "Tamfest", "Famous Museum", "Waterboom", "Upno", "Upno2"]
    hours = ["07.00-11.30", "11.30-13.00", "13.00-15.00", "15.30-20.00", "20.00-21.00", "20.00-21.00"]
    widget = ScheduleWidget(header, places, hours)
    widget.show()
    sys.exit(app.exec_())
