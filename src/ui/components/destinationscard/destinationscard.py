import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QColor
from PyQt5.QtCore import QSize, Qt


class CustomButton(QToolButton):
    def __init__(self, icon_path, text, parent=None):
        super().__init__(parent)

        # Set button icon
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(200, 200))  # Adjust size as needed

        # Set button text
        self.setText(text)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # Set text under icon
        self.setStyleSheet("""
            QToolButton {
                font-size: 20px;
                border: 2px solid black;
                border-radius: 10px;
                background-color: #FFC800;
                color: black;
                padding-top: 5px;
                margin: 0px;
            }
            QToolButton::hover {
                background-color: #FFC000;
            }
        """)
        self.setMinimumSize(QSize(220, 250))  # Adjust the button size as needed


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Custom Button Example')
        self.setGeometry(100, 100, 300, 400)

        # Create a layout
        layout = QVBoxLayout()

        # Create and add custom button
        button = CustomButton('img/images/foto_1.jpg', 'Bandung')
        layout.addWidget(button)

        # Set layout to the window
        self.setLayout(layout)


# Create the application
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()
window.show()

# Run the application event loop
sys.exit(app.exec_())
