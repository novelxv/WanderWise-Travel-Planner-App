import os
from src.ui.components.articlecard.cards import Cards
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from src.ui.components.backbutton.backbutton import BackButton


class ArticleList(QWidget):
    def __init__(self, articles, parent=None):
        super().__init__()
        self.parent = parent
        self.stacked_widget = parent.stacked_widget if parent else None

        # Set page size
        parentWidth = parent.width() if parent else 1240
        parentHeight = parent.height() if parent else 500
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        BASE_URL = 'img/'

        # Create the header label
        self.header_itinerary_label = QtWidgets.QLabel("ARTICLES")
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
                background: none;
                padding-top: 40px;
                padding-bottom: 40px;
            }
        """)

        # Create the back button
        self.back_button = BackButton()
        self.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        # Create the top layout and add the back button and header label
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignRight)
        top_layout.addWidget(self.header_itinerary_label)
        top_layout.addStretch()  # Ensure the label is aligned to the left

        # Create the cards
        cards = Cards(articles, len(articles), BASE_URL, self)

        # Create the main layout and add the top layout and cards
        layout = QVBoxLayout(self)
        layout.addLayout(top_layout)
        layout.addWidget(cards)


        # Adjust layout margins and spacings
        layout.setSpacing(0)

        # Set the main layout for the widget
        self.setLayout(layout)