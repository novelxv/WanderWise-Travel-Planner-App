from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from src.ui.components.addbutton.addbutton import FloatingAddButton
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon

class ListOfDestinations(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('List of Destinations')
        self.setGeometry(300, 100, 1500, 600)  # Adjust window position and size

        # Set background image
        self.pixmap = QPixmap('img/bg/lod_bg.svg')
        self.updateBackground()

        layout = QVBoxLayout()
        # Add buttons (Idea, Plan, Booked, Done)
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_names = ["Idea", "Plan", "Booked", "Done"]
        for name in button_names:
            button = OvalButtonIcon(name, None, "#C5E5C0", 20)
            button_layout.addWidget(button)
        layout.addLayout(button_layout)

        # Add spacer to push buttons to the top
        spacer = QSpacerItem(800, 800, QSizePolicy.Minimum, QSizePolicy.Fixed)
        layout.addItem(spacer)

        # Add floating add button
        self.add_button = FloatingAddButton(self, position=(10, 10))
        self.setLayout(layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateBackground()
        self.add_button.setFloatingPosition()

    def updateBackground(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio)))
        self.setPalette(palette)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ListOfDestinations()
    window.show()
    sys.exit(app.exec_())