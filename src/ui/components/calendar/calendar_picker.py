import sys
import signal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class CalendarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar Picker')
        self.setGeometry(300, 300, 350, 300)  # Adjust window position and size

        # Layout
        layout = QVBoxLayout()

        # Create a Calendar Widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)  # Show grid lines
        self.calendar.clicked.connect(self.accept)  # Close dialog on date click

        # Adding widgets to layout
        layout.addWidget(self.calendar)

        # Set layout
        self.setLayout(layout)

    def selectedDate(self):
        return self.calendar.selectedDate()

class CalendarPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_date = None  # Variable to store selected date
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar Picker')
        self.setGeometry(300, 300, 100, 50)  # Adjust window position and size

        # Layout
        layout = QVBoxLayout()

        # Create a button to show the calendar dialog
        self.button = QPushButton('', self)
        self.button.setIcon(QIcon('img/icons/calendar_icon.svg'))
        self.button.setIconSize(QSize(32, 32))  # Set icon size
        self.button.setFixedSize(40, 40)  # Set button size
        self.button.clicked.connect(self.show_calendar_dialog)

        # Adding widgets to layout
        layout.addWidget(self.button)

        # Set layout
        self.setLayout(layout)

    def show_calendar_dialog(self):
        dialog = CalendarDialog()
        if dialog.exec_():
            self.selected_date = dialog.selectedDate()
            print(f"Selected Date: {self.selected_date.toString()}")

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarPicker()
    ex.show()
    sys.exit(app.exec_())
