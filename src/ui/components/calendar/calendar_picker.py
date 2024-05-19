import sys
import signal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDialog, QCalendarWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, pyqtSignal, Qt

class CalendarDialog(QDialog):
    dateSelected = pyqtSignal(object)  # Signal to emit the selected date

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar Picker')
        self.setGeometry(300, 300, 350, 300)

        # Layout
        layout = QVBoxLayout()

        # Create a Calendar Widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.on_date_selected)

        # Adding widgets to layout
        layout.addWidget(self.calendar)

        # Set layout
        self.setLayout(layout)

    def on_date_selected(self):
        selected_date = self.calendar.selectedDate()
        self.dateSelected.emit(selected_date)
        self.accept()

    def selectedDate(self):
        return self.calendar.selectedDate()

class CalendarPicker(QWidget):
    dateSelected = pyqtSignal(object)  # Signal to emit the selected date

    def __init__(self):
        super().__init__()
        self.selected_date = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar Picker')
        self.setGeometry(300, 300, 100, 50)

        # Layout
        layout = QVBoxLayout()

        # Create a button to show the calendar dialog
        self.button = QPushButton('', self)
        self.button.setIcon(QIcon('img/icons/calendar_icon.svg'))
        self.button.setIconSize(QSize(32, 32))
        self.button.setFixedSize(40, 40)
        self.button.clicked.connect(self.show_calendar_dialog)

        # Adding widgets to layout
        layout.addWidget(self.button)

        # Set layout
        self.setLayout(layout)

    def show_calendar_dialog(self):
        dialog = CalendarDialog()
        dialog.dateSelected.connect(self.on_date_selected)
        if dialog.exec_():
            self.selected_date = dialog.selectedDate()
            self.dateSelected.emit(self.selected_date)
            print(f"Selected Date: {self.selected_date.toString()}")

    def on_date_selected(self, date):
        self.selected_date = date
        self.dateSelected.emit(date)


signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarPicker()
    ex.show()
    sys.exit(app.exec_())
