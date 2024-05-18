from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from ui.components.articlecard.article_card import *

class Cards(QWidget):
     def __init__(self, content, card_count, base_url, parent=None):
        super().__init__(parent)

        # basic setup
        self.setFixedWidth(parent.width())
        self.card_count = card_count
        self.content = content

        # initiate layout
        self.widgets = QWidget()
        self.setMinimumHeight(int(0.5 * parent.height()))
        self.card_container = QGridLayout(self.widgets)
        self.card_container.setSpacing(-100)
        self.card_container.setContentsMargins(-30,-60,-30,30)

        # main layout
        layout = QVBoxLayout()
        layout.addWidget(self.widgets)

        # setup cards
        for i in range(self.card_count):
            image_path = f"{base_url}images/article{i+1}.png"
            card = ArticleCard(image_path, content[i][1], int(0.75 * self.width() / 2))
            self.card_container.addWidget(card, i // 2, i % 2, 1, 1)

        self.setLayout(layout)
        self.setContentsMargins(0,50,0,50)
        
        