from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from src.ui.components.articlecard.article_card import *

class Cards(QWidget):
    def __init__(self, content, card_count, base_url, parent=None):
        super().__init__(parent)

        # Basic setup
        self.setFixedWidth(parent.width())
        self.card_count = card_count
        self.content = content

        # Initiate layout
        self.widgets = QWidget()
        self.setMinimumHeight(int(0.5 * parent.height()))
        self.card_container = QGridLayout(self.widgets)

        # Adjust the margins to move the cards up
        self.card_container.setContentsMargins(0, 0, 0, 0)
        self.card_container.setVerticalSpacing(20)  # Optional: Adjust vertical spacing between cards

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.widgets)

        # Setup cards
        for i in range(self.card_count):
            image_path = f"{base_url}images/article{i+1}.png"
            card = ArticleCard(image_path, content[i][1], int(0.75 * self.width() / 2), int(0.75 * self.width() / 3.3))
            self.card_container.addWidget(card, i // 2, i % 2, 1, 1)

        # Add a spacer item at the bottom to push the cards up
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addSpacerItem(spacer)
    
        self.setLayout(layout)
