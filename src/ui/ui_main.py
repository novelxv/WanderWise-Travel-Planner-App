from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QMainWindow, QSizePolicy
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from src.ui.pages.homepage import HomePage
from src.ui.pages.article_list import ArticleList
from src.ui.pages.list_of_destinations import ListOfDestinations
from src.ui.pages.listof_itineraries import Listof_Itineraries
# from ui.pages.article_details import *
# from ui.pages.itinerary_details import Itinerary_Details
from src.ui.pages.form_add_destination import FormAddDestination
# from ui.pages.form_add_itinerary import FormAddItinerary
from src.ui.pages.form_edit_destination import FormEditDestination
# from ui.pages.form_edit_itinerary import FormEditItinerary
from src.ui.pages.destination_detail import DestinationDetail
from src.ui.pages.no_destinations import DestinationsPage


class UI(object):
    def setup(self, parent:QMainWindow, destinations, articles):
        parent.setObjectName("Window")

        # Set background image
        pixmap = QPixmap('img/bg/window_bg.png')
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

        # TESTING DIANA
        # budgeting = BudgetingWindow()
        # content_container.addWidget(budgeting)
        # no_destinations = DestinationsPage()
        # content_container.addWidget(no_destinations)
        # no_itinerary = ItinerariesPage()
        # content_container.addWidget(no_itinerary)

        # TESTING THEA
        headers = ["Monday 10/12", "Tuesday 11/12", "Wednesday 12/12", "Thursday 13/12", "Thursday 13/12"]
        list_of_places = [
            ["Amusement Park", "Tamfest", "Famous Museum", "Waterboom", "Upno"], #monday
            ["Zoo", "Botanical Garden", "Historical Museum", "Aquarium", "Maxx"], #tuesday
            ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
            ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
            ["Beach", "Water Sports", "Seafood Restaurant", "Night Market", "Cat Cafe"]
        ]
        list_of_hours = [
            ["07.00-11.30", "11.30-13.00", "13.00-15.00", "15.30-20.00", "20.00-21.00"],
            ["08.00-12.00", "12.30-14.00", "14.30-16.00", "16.30-19.00", "19.30-21.00"],
            ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
            ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
            ["09.00-12.00", "12.30-15.00", "15.30-18.00", "18.30-21.00", "21.30-23.00"]
        ]
        # destinations = ["Bandung", "Semarang", "Makassar", "Padang", "Paris", "Jakarta"]
        # trip = "Bandung Trip 10/12/24 - 15/12/24"
        # list_of_itineraries = Listof_Itineraries(trip, headers, list_of_places, list_of_hours)
        # content_container.addWidget(list_of_itineraries)

        # TEST PAGE
        # destination_detail = DestinationDetail(1, parent)
        # content_container.addWidget(destination_detail)


        home_widget = HomePage(parent)
        article_list_widget = ArticleList(articles, parent)
        no_destinations = DestinationsPage(parent)
        destination_list_widget = ListOfDestinations(destinations, parent)
        # itinerary_list_widget = Listof_Itineraries(" Bandung Trip 10/10/24 - 15/10/24", headers, list_of_places, list_of_hours, parent)
        # itinerary_detail_widget = Itinerary_Details()
        # article_detail_widget = 
        form_add_destinasi_widget = FormAddDestination(parent)
        # form_add_itinerary_widget = FormAddItinerary(parent)
        form_edit_destinasi_widget = FormEditDestination(parent)
        # form_edit_itinerary_widget = FormEditItinerary(parent)
        
        # list_of_itineraries = Listof_Itineraries("trip", headers, list_of_places, list_of_hours,parent)
        # content_container.addWidget(list_of_itineraries)
        # parent.stacked_widget.form_widget = article_list_widget

        content_container.addWidget(home_widget) #PAGE 0
        content_container.addWidget(article_list_widget) #PAGE 1
        content_container.addWidget(no_destinations) #PAGE 2
        content_container.addWidget(destination_list_widget) #PAGE 3
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

