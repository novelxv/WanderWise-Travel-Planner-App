import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import QSize, Qt

class ArticleCard(QWidget):
    def __init__(self, icon_path, text, width, height, parent=None):
        super().__init__(parent)
        # self.stacked_widget = parent.stacked_widget
        self.content = text
        
        # Set image
        self.image = QLabel()
        self.image.setPixmap(QPixmap(icon_path))
        self.image.setScaledContents(True)
        self.image.setMargin(0)

        self.image.setObjectName("image_article")
        self.image.setStyleSheet("""
            #image_article {
                background-color: #FFC800;
                border: 5px solid black;
                margin: 0px;
                border-top-right-radius: 10px;
                border-top-left-radius: 10px;
                width: 100px;
            }
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.mousePressEvent = self.handle_article_click

        # Set button text
        text = text[:80]+"\n"+text[80:]
        self.title = QPushButton()
        self.title.setText(text)
        self.title.setObjectName("article_title")
        self.title.setStyleSheet("""
            #article_title {
                background-color: #FFC800;
                padding-top: 10px;
                font: bold 20px;
                border: 5px solid black;
                border-top : 0;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
                border-top-left-radius: 0;
                border-top-right-radius: 0;
                margin: 0px;
            }
        """)
        self.title.clicked.connect(self.handle_article_click)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(0,0,0,0)
        card_layout.setSpacing(0)
        card_layout.addWidget(self.image)
        card_layout.addWidget(self.title)
        self.setFixedSize(QSize(width, height))
        self.setLayout(card_layout)
        self.setContentsMargins(0,0,0,0)

    def handle_article_click(self, event):
        print("clicked")
        # UPDATE RECIPE DETAIL WIDGET
        # self.stacked_widget.article_detail_widget.update_article_detail(self.content)

        # CHANGE STACKED WIDGET TO RECIPE DETAIL
        # self.stacked_widget.setCurrentIndex(4)