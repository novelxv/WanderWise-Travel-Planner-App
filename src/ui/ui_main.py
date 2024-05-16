from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QMainWindow, QSizePolicy
# from ui.components.form.form_row import Form
from ui.pages.article_list import *

class UI(object):
    def setup(self, parent:QMainWindow, destinations, articles):
        parent.setObjectName("Window")

        app = QApplication.instance()

        # set size property of Window
        width = int(0.8 * app.desktop().screenGeometry().width())
        height = int(width * 10/16)
        parent.setFixedSize(width, height)

        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(parent.sizePolicy().hasHeightForWidth())
        parent.setSizePolicy(size_policy)
        self.central_widget = QWidget(parent)
        self.central_widget.setObjectName('central_widget')

        # set content container
        content_container = QStackedWidget()
        content_container.setFixedWidth(int(0.9 * width))
        parent.stacked_widget = content_container

        # add stacked widget to window
        parent.last_page_idx = 0
        # form = Form(True, "Destination", "destination", parent)
        arc_list = articleList(articles, parent)
        parent.stacked_widget.form_widget = arc_list

        content_container.addWidget(arc_list)

        parent.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)
        layout.setSpacing(0)
        layout.addWidget(content_container)
        layout.setContentsMargins(0,0,0,0)

