import sys
from PyQt5.QtWidgets import QWidget, QToolButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtCore import QSize, Qt

class CustomButton(QToolButton):
    def __init__(self, icon_path, text, width, parent=None):
        super().__init__(parent)

        # Set button icon
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(width, 120))  # Adjust size as needed

        # self.image = QLabel()
        # self.image.setPixmap(QPixmap(icon_path))
        # self.image.setScaledContents(True)
        # self.image.setMargin(0)
        # self.image.setFixedWidth(width)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.mousePressEvent = self.handle_article_click
        # Set button text
        text = text[:80]+"\n"+text[80:]
        # if(len(text)>80):
        self.setText(text)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # Set text under icon
        self.setStyleSheet("""
            QToolButton {
                font-size: 17px;
                border: 2px solid black;
                border-radius: 10px;
                background-color: #FFC800;
                color: black;
                padding-top: 2px;
                margin: 0px;
            }
            QToolButton::hover {
                background-color: #FFC000;
            }
        """)
        self.clicked.connect(self.handle_article_click)
        self.setFixedSize(QSize(width, int(0.5 * width)))  # Adjust the button size as needed
        # self.setMinimumSize(QSize(220, 250))  # Adjust the button size as needed
        self.setContentsMargins(0,0,0,0)

    def handle_article_click(self, event):
        print("clicked")