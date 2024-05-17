import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.ui_main import UI
from controller.artikel_controller import *
from controller.destinasi_controller import *
from controller.itinerary_controller import *

class Window(QMainWindow):
    artikel_controller = ArtikelController
    destinasi_controller = DestinasiController
    itinerary_controller = ItineraryController

    def __init__(self):
        super(Window, self).__init__()

        # setup controllers
        self.artikel_controller = ArtikelController()
        self.destinasi_controller = DestinasiController()
        self.itinerary_controller = ItineraryController()
        # setup articles and destination
        self.articles = self.artikel_controller.get_all_artikel()
        self.destinasi = self.destinasi_controller.get_all_destinasi()

        # setup UI
        self.setWindowTitle("Wanderwise")
        self.ui = UI()
        self.ui.setup(self, self.destinasi, self.articles)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())