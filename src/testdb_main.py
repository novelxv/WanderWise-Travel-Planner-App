from src.controller.destinasi_controller import *
from src.controller.itinerary_controller import *
if __name__ == '__main__':
    destinasi_controller = DestinasiController()
    itinerary_controller = ItineraryController()
    tests = [{"nama":"Paris", "kategori" : "Plan", "tanggal_mulai": "2023-06-15", "tanggal_selesai" : "2023-06-20", "budget": 5000000, "tabungan" : 1000000},
                {"nama":'Singapore', "kategori" : 'Booked',  "tanggal_mulai": '2004-05-07',"tanggal_selesai" : '2004-09-07', "budget": 1000000,"tabungan" : 300000}]
    # for i,entry in enumerate(tests):
    #     destinasi_controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    # itinerary_controller.add_itinerary(1,"Upno","2023-06-11","19:00:00","20:00:00",90000,"taxi","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"Waterboom","2023-06-11","19:00:00","20:00:00",90000,"bus","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"Resto","2023-06-11","19:00:00","20:00:00",90000,"car","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"Mountain hiking","2023-06-12","19:00:00","20:00:00",90000,"taxi","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"museum","2023-06-12","19:00:00","20:00:00",90000,"bus","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"waterfall","2023-06-12","19:00:00","20:00:00",90000,"train","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"school","2023-06-13","19:00:00","20:00:00",90000,"bus","INI NOTES NOTESSSSS")
    # itinerary_controller.add_itinerary(1,"park","2023-06-13","19:00:00","20:00:00",90000,"train","INI NOTES NOTESSSSS")
    
    # destinasi_controller.add_destinasi("Paris","Done","2024-12-10","2024-12-15",5000000,1000000)
    # destinasi_controller.add_destinasi("Makassar","Idea","2023-12-10","2023-12-15",3000000,1000000)
    # print all destinasi
    alldest = destinasi_controller.get_all_destinasi()

    
    
    result = itinerary_controller.get_destinasi_detail(3)
    print(result)

    for data in alldest:
        print(data.nama, data.kategori, data.destinasi_id)
    # result = destinasi_controller.get_destinasi_by_id(3)
    # print(result.destinasi_id)
    # itinerary_controller.add_itinerary(result.destinasi_id, "Upno", result.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    # itinerary_controller.add_itinerary(result.destinasi_id, "Waterboom", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    # itinerary_controller.add_itinerary(result.destinasi_id, "Museum", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "mobil", "mahal")
    # tanggal = itinerary_controller.get_tanggal_itinerary(result.destinasi_id)
    # print(tanggal)
    # data = []
    # for t in tanggal:
    #     print(t)
    #     # data.append({"tanggal":t, "attr":itinerary_controller.get_lokasi_by_tanggal(result.destinasi_id, t)})
    # print(data)


