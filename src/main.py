
# if __name__ == '__main__':
#     artikel_controller = ArtikelController()
#     destinasi_controller = DestinasiController()
#     itinerary_controller = ItineraryController()

#     print("---------ENTER NEW DESTINASI---------")
#     destinasi_controller.add_destinasi('Bandung', 'Booked', '2004-05-07', '2004-09-07', 1000000, 300000)

#     print("---------ENTER NEW ITINERARY---------")
#     itinerary_controller.add_itinerary(1,'ITB','2004-05-07', '17:00:00', '18:00:00', 70000, 'jet', 'panas bro')
#     print("details for destinasi 1")
#     print(itinerary_controller.get_destinasi_detail(1))
#     print()
    
#     print("---------ARTIKEL----------")
#     artikel_list = artikel_controller.get_all_artikel()
#     for artikel in artikel_list:
#         print(artikel)
#         print()

#     print("---------DESTINASI----------")
#     destinasi_list = destinasi_controller.get_all_destinasi()
#     for destinasi in destinasi_list:
#         print(destinasi)
#         print()

#     print("---------ITINERARY----------")
#     itinerary_list = itinerary_controller.get_all_itinerary()
#     for itinerary in itinerary_list:
#         print(itinerary)
#         print()
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