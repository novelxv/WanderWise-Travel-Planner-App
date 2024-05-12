# import src.app.utils.mymath.addition as addition


# def main():
#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
#     print(addition.Math.add(1, 2))
from controller.artikel_controller import *
from controller.destinasi_controller import *
from controller.itinerary_controller import *

if __name__ == '__main__':
    artikel_controller = ArtikelController()
    destinasi_controller = DestinasiController()
    itinerary_controller = ItineraryController()

    print("---------ENTER NEW DESTINASI---------")
    destinasi_controller.add_destinasi('Bandung', 'Booked', '2004-05-07', '2004-09-07', 1000000, 300000)

    print("---------ENTER NEW ITINERARY---------")
    itinerary_controller.add_itinerary(1,'ITB','2004-05-07', '17:00:00', '18:00:00', 70000, 'jet', 'panas bro')
    print("details for destinasi 1")
    print(itinerary_controller.get_destinasi_detail(1))
    print()
    
    print("---------ARTIKEL----------")
    artikel_list = artikel_controller.get_all_artikel()
    for artikel in artikel_list:
        print(artikel)
        print()

    print("---------DESTINASI----------")
    destinasi_list = destinasi_controller.get_all_destinasi()
    for destinasi in destinasi_list:
        print(destinasi)
        print()

    print("---------ITINERARY----------")
    itinerary_list = itinerary_controller.get_all_itinerary()
    for itinerary in itinerary_list:
        print(itinerary)
        print()
