from PyQt5.QtWidgets import QWidget, QToolButton, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import QSize, Qt

class CustomButton(QWidget):
    def __init__(self, icon_path, text, width, parent=None):
        super().__init__(parent)

        # Create main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Set button icon
        self.button = QToolButton()
        pixmap = QPixmap(icon_path).scaled(width, int(0.5 * width), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.button.setIcon(QIcon(pixmap))
        self.button.setIconSize(QSize(width, int(0.5 * width)))  # Adjust size as needed
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button.setStyleSheet("""
            QToolButton {
                border: 5px solid black;
                margin: 0px;
                border-top-right-radius: 10px;
                border-top-left-radius: 10px;
                background: none;
            }
        """)
        self.button.clicked.connect(self.handle_article_click)
        layout.addWidget(self.button)

        # Set text label
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.label.setStyleSheet("""
            QLabel {
                background-color: #FFC800;
                color: black;
                font: 25px bold;
                border: 5px solid black;
                border-top: 0;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
                margin: 0px;
            }
        """)
        layout.addWidget(self.label)

        # Set fixed size for the custom button widget
        self.setFixedSize(QSize(width, int(0.5 * width) + self.label.sizeHint().height()))

    def handle_article_click(self, event):
        print("clicked")
