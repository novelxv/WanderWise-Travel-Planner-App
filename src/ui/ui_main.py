from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget, QHBoxLayout, QMainWindow, QSizePolicy
# from ui.components.form.form_row import Form
from ui.pages.homepage import HomePage
from ui.pages.article_list import ArticleList
from ui.pages.list_of_destinations import ListOfDestinations
from ui.pages.listof_itineraries import *
from ui.pages.budgeting import *
from ui.pages.no_destinations import *
from ui.pages.no_itinerary import *

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

        # TESTING DIANA
        # budgeting = BudgetingWindow()
        # content_container.addWidget(budgeting)
        # no_destinations = DestinationsPage()
        # content_container.addWidget(no_destinations)
        # no_itinerary = ItinerariesPage()
        # content_container.addWidget(no_itinerary)

        # TESTING THEA
        # headers = ["Monday 10/12", "Tuesday 11/12", "Wednesday 12/12", "Thursday 13/12", "Thursday 13/12"]
        # list_of_places = [
        #     ["Amusement Park", "Tamfest", "Famous Museum", "Waterboom", "Upno"], #monday
        #     ["Zoo", "Botanical Garden", "Historical Museum", "Aquarium", "Maxx"], #tuesday
        #     ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
        #     ["Mountain Climb", "City Tour", "Art Gallery", "Theater", "Bar"],
        #     ["Beach", "Water Sports", "Seafood Restaurant", "Night Market", "Cat Cafe"]
        # ]
        # list_of_hours = [
        #     ["07.00-11.30", "11.30-13.00", "13.00-15.00", "15.30-20.00", "20.00-21.00"],
        #     ["08.00-12.00", "12.30-14.00", "14.30-16.00", "16.30-19.00", "19.30-21.00"],
        #     ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
        #     ["06.00-10.00", "10.30-12.00", "12.30-14.00", "14.30-17.00", "17.30-19.00"],
        #     ["09.00-12.00", "12.30-15.00", "15.30-18.00", "18.30-21.00", "21.30-23.00"]
        # ]
        # trip = "Bandung Trip 10/12/24 - 15/12/24"
        # list_of_itineraries = Listof_Itineraries(trip, headers, list_of_places, list_of_hours)
        # content_container.addWidget(list_of_itineraries)

        home_widget = HomePage(parent)
        article_list_widget = ArticleList(articles, parent)
        destination_list_widget = ListOfDestinations(destinations, parent)
        parent.stacked_widget.form_widget = article_list_widget

        content_container.addWidget(home_widget) #PAGE 0
        content_container.addWidget(article_list_widget) #PAGE 1
        content_container.addWidget(destination_list_widget) #PAGE 2

        parent.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)
        layout.setSpacing(0)
        layout.addWidget(content_container)
        layout.setContentsMargins(0,0,0,0)

