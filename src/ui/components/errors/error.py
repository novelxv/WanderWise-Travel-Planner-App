from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QPalette, QBrush

class ErrorPopup(QtWidgets.QDialog):
    def __init__(self, error_message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(300, 150)  # Set fixed size for the popup

        # Set background image
        self.pixmap = QPixmap('img/icons/eror2.png')
        self.updateBackground()

        layout = QtWidgets.QVBoxLayout()

        # Add a spacer to push the error message to the left
        error_layout = QtWidgets.QHBoxLayout()
        left_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        error_layout.addItem(left_spacer)

        self.error_label = QtWidgets.QLabel(error_message)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the left
        self.error_label.setWordWrap(True)
        self.error_label.setFixedWidth(200) 
        self.error_label.setStyleSheet("""
            QLabel {
                font: 16px;
                padding: 10px;
                font-weight: bold;
            }
        """)
        error_layout.addWidget(self.error_label)

        right_spacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        error_layout.addItem(right_spacer)

        layout.addLayout(error_layout)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer_item)

        button_layout = QtWidgets.QHBoxLayout()

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.setStyleSheet("QPushButton { background-color: none; border: none; color: black; font-size: 14px; font-weight: bold; }")
        self.ok_button.clicked.connect(self.accept)

        # Add the OK button to the layout
        button_layout.addWidget(self.ok_button)

        # Add a spacer item to the right side to ensure proper alignment
        right_spacer_button = QtWidgets.QSpacerItem(35, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        button_layout.addItem(right_spacer_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateBackground()

    def updateBackground(self):
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_message = "You must enter 1000 characters, 10 dreams, and 1 ice cream."
    popup = ErrorPopup(error_message)
    popup.show()
    sys.exit(app.exec_())
