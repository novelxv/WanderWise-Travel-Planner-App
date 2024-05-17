import os
from ui.components.destinationscard.cards import Cards
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

class articleList(QWidget):
    def __init__(self, articles, parent=None):
        super().__init__()
        self.parent = parent
        # self.stacked_widget = parent.stacked_widget if parent else None

        # Set page size
        parentWidth = parent.width() if parent else 1240
        parentHeight = parent.height() if parent else 500
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        # Set background image
        BASE_URL = '../img/'
        path = os.path.abspath(BASE_URL+'icons/List_of_Articles.png')
        bgLabel = QLabel(self)
        pixmap = QPixmap(path)
        bgLabel.setPixmap(pixmap)
        bgLabel.setScaledContents(True)
        bgLabel.setGeometry(0, 0, self.width(), self.height())
    
        # set boxes of list
        # content_layout = QVBoxLayout()
        cards = Cards(articles, len(articles), BASE_URL, self)
        # content_layout.addWidget(cards)

        # set footer

        # set layout
        layout = QVBoxLayout(self)
        layout.addWidget(cards)

        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)