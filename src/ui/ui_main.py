from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QMainWindow, QSizePolicy
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from ui.pages.homepage import HomePage
from ui.pages.article_list import ArticleList
from ui.pages.list_of_destinations import ListOfDestinations
from ui.pages.listof_itineraries import Listof_Itineraries
# from ui.pages.article_details import *
# from ui.pages.itinerary_details import Itinerary_Details
from ui.pages.form_add_destination import FormAddDestination
# from ui.pages.form_add_itinerary import FormAddItinerary
from ui.pages.form_edit_destination import FormEditDestination
# from ui.pages.form_edit_itinerary import FormEditItinerary

class UI(object):
    def setup(self, parent:QMainWindow, destinations, articles):
        parent.setObjectName("Window")

        # Set background image
        pixmap = QPixmap('../img/bg/window_bg.png')
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        parent.setPalette(palette)

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
        home_widget = HomePage(parent)
        article_list_widget = ArticleList(articles, parent)
        destination_list_widget = ListOfDestinations(destinations, parent)
        # itinerary_list_widget = Listof_Itineraries()
        # itinerary_detail_widget = Itinerary_Details()
        # article_detail_widget = 
        form_add_destinasi_widget = FormAddDestination(parent)
        # form_add_itinerary_widget = FormAddItinerary(parent)
        form_edit_destinasi_widget = FormEditDestination(parent)
        # form_edit_itinerary_widget = FormEditItinerary(parent)
        
        
        parent.stacked_widget.form_widget = article_list_widget

        content_container.addWidget(home_widget) #PAGE 0
        content_container.addWidget(article_list_widget) #PAGE 1
        content_container.addWidget(destination_list_widget) #PAGE 2
        # content_container.addWidget(itinerary_list_widget) #PAGE 3
        # content_container.addWidget(itinerary_detail_widget) #PAGE 4
        # content_container.addWidget(article_detail_widget) #PAGE 5
        content_container.addWidget(form_add_destinasi_widget) #PAGE 6
        # content_container.addWidget(form_add_itinerary_widget) #PAGE 7
        content_container.addWidget(form_edit_destinasi_widget) #PAGE 8
        # content_container.addWidget(form_edit_itinerary_widget) #PAGE 9

        parent.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)
        layout.setSpacing(0)
        layout.addWidget(content_container)
        layout.setContentsMargins(0,0,0,0)

