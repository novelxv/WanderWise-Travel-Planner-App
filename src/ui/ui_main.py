import sys
from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCursor
from PyQt5.QtCore import Qt
from src.ui.pages.homepage import HomePage
from src.ui.pages.article_list import ArticleList
from src.ui.pages.list_of_destinations import ListOfDestinations
from src.ui.pages.listof_itineraries import Listof_Itineraries
from src.ui.pages.form_add_destination import FormAddDestination
from src.ui.pages.form_edit_destination import FormEditDestination
from src.ui.pages.destination_detail import DestinationDetail
from src.ui.pages.no_destinations import DestinationsPage
from src.controller.destinasi_controller import DestinasiController

class UI(object):
    def setup(self, parent: QMainWindow, destinations, articles):
        self.parent = parent
        parent.setObjectName("Window")

        # Set background image
        pixmap = QPixmap('img/bg/window_bg.png')
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        parent.setPalette(palette)

        app = QApplication.instance()

        # set size property of Window
        width = int(0.8 * app.desktop().screenGeometry().width())
        height = int(width * 10 / 16)
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
        # content_container.setFixedWidth(int(0.9 * width))
        parent.stacked_widget = content_container

        # add stacked widget to window
        parent.last_page_idx = 0

        # ------------ UNCOMMENT THIS TO ADD PAGES
        home_widget = HomePage(parent)
        article_list_widget = self.wrap_with_footer(ArticleList(articles, parent))
        no_destinations = self.wrap_with_footer(DestinationsPage(parent))
        destination_list_widget = self.wrap_with_footer(ListOfDestinations(destinations, parent))
        # destination_detail_widget = self.wrap_with_footer(DestinationDetail(parent))

        content_container.addWidget(home_widget)  # PAGE 0
        content_container.addWidget(article_list_widget)  # PAGE 1
        content_container.addWidget(no_destinations)  # PAGE 2
        content_container.addWidget(destination_list_widget)  # PAGE 3
        # content_container.addWidget(destination_detail_widget)  # PAGE 4
        # ------------- UNCOMMENT THIS TO ADD PAGES

        parent.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)
        layout.setSpacing(0)
        layout.addWidget(content_container)
        layout.setContentsMargins(0, 0, 0, 0)

    def wrap_with_footer(self, widget):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(widget)
        layout.addWidget(self.create_footer())
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return container

    def create_footer(self):
        footer_layout = QHBoxLayout()
        destinations_label = QLabel("Destinations")
        destinations_label.setAlignment(Qt.AlignCenter)
        destinations_label.setStyleSheet("color: white; padding-left: 700px ;padding-bottom: 30px; font: bold 30px; background: transparent")
        destinations_label.setCursor(QCursor(Qt.PointingHandCursor))
        destinations_label.mousePressEvent = self.destinations_clicked

        articles_label = QLabel("Articles")
        articles_label.setAlignment(Qt.AlignCenter)
        articles_label.setStyleSheet("color: white; padding-bottom: 30px; font: bold 30px; background: transparent")
        articles_label.setCursor(QCursor(Qt.PointingHandCursor))
        articles_label.mousePressEvent = self.articles_clicked

        footer_layout.addWidget(destinations_label)
        footer_layout.addWidget(articles_label)

        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)
        footer_widget.setFixedHeight(100)

        return footer_widget

    def destinations_clicked(self, event):
        print("Destinations clicked!")
        dest = DestinasiController()
        n_dest = len(dest.get_all_destinasi())
        if n_dest == 0:
            self.parent.stacked_widget.setCurrentIndex(2)
        else:
            self.parent.stacked_widget.setCurrentIndex(3)

    def articles_clicked(self, event):
        print("Articles clicked!")
        self.parent.stacked_widget.setCurrentIndex(1)
        # Call the function for Articles

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI()
    ui.setup(window, [], [])
    window.show()
    sys.exit(app.exec_())