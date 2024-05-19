import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import Qt, QTimer

class ProgressBarWindow(QWidget):
    def __init__(self, now, goal):
        super().__init__()

        # Set up the main layout
        layout = QVBoxLayout()

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(int(now/goal*100))  # Set initial value to 70%
        self.progress_bar.setTextVisible(False)  # Hide the percentage text
        self.progress_bar.setFixedSize(550, 40)

        # Set the stylesheet for the progress bar to match the desired design
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid black;
                border-radius: 18px;
                background: white;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #48C9B0;
                border-radius: 18px;
                margin: 0px;
            }
        """)

        # Add the progress bar to the layout
        layout.addWidget(self.progress_bar)

        # Set layout to the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Progress Bar Example")
        self.setGeometry(100, 100, 400, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBarWindow(70000, 100000)
    window.show()
    sys.exit(app.exec_())