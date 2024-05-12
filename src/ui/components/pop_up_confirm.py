import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class ConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Delete Itinerary")
        self.setGeometry(100, 100, 400, 200)  # Adjust size and position
        self.setFixedSize(400, 200)  # Makes the size fixed

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(10)

        # Image
        image = QLabel(self)
        pixmap = QPixmap("/mnt/data/image.png")  # Path to the image file
        image.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image.setAlignment(Qt.AlignCenter)

        # Label
        label = QLabel("Delete this itinerary?")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px;")

        # Button layout
        buttonLayout = QHBoxLayout()

        # Yes Button
        yesButton = QPushButton("Yes")
        yesButton.setIcon(QIcon("path/to/yes_icon.png"))  # Adjust path to icon if needed
        yesButton.setIconSize(QSize(24, 24))
        yesButton.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 16px; border: none; }"
                                "QPushButton:hover { background-color: #45A049; }")
        yesButton.setFixedSize(120, 50)
        yesButton.clicked.connect(self.accept)

        # No Button
        noButton = QPushButton("No")
        noButton.setIcon(QIcon("path/to/no_icon.png"))  # Adjust path to icon if needed
        noButton.setIconSize(QSize(24, 24))
        noButton.setStyleSheet("QPushButton { background-color: #F44336; color: white; font-size: 16px; border: none; }"
                               "QPushButton:hover { background-color: #D32F2F; }")
        noButton.setFixedSize(120, 50)
        noButton.clicked.connect(self.reject)

        # Add buttons to button layout
        buttonLayout.addWidget(yesButton)
        buttonLayout.addWidget(noButton)
        buttonLayout.setAlignment(Qt.AlignCenter)

        # Adding widgets to the main layout
        mainLayout.addWidget(image)
        mainLayout.addWidget(label)
        mainLayout.addLayout(buttonLayout)

        # Set dialog layout
        self.setLayout(mainLayout)

    def run(self):
        return self.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ConfirmationDialog()
    res = dialog.run()
    if res == QDialog.Accepted:
        print("Yes clicked")
    else:
        print("No clicked")
    sys.exit(app.exec_())