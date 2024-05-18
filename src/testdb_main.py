from controller.destinasi_controller import *
from controller.itinerary_controller import *
if __name__ == '__main__':
    destinasi_controller = DestinasiController()
    itinerary_controller = ItineraryController()
    tests = [{"nama":"Paris", "kategori" : "Plan", "tanggal_mulai": "2023-06-15", "tanggal_selesai" : "2023-06-20", "budget": 5000000, "tabungan" : 1000000},
                {"nama":'Singapore', "kategori" : 'Booked',  "tanggal_mulai": '2004-05-07',"tanggal_selesai" : '2004-09-07', "budget": 1000000,"tabungan" : 300000}]
    # for i,entry in enumerate(tests):
    #     destinasi_controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    
    result = destinasi_controller.get_destinasi_by_id(3)
    # itinerary_controller.add_itinerary(result.destinasi_id, "Upno", result.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    # itinerary_controller.add_itinerary(result.destinasi_id, "Waterboom", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    # itinerary_controller.add_itinerary(result.destinasi_id, "Museum", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "mobil", "mahal")
    tanggal = itinerary_controller.get_tanggal_itinerary(result.destinasi_id)
    data = []
    for t in tanggal:
        data.append({"tanggal":t, "attr":itinerary_controller.get_lokasi_by_tanggal(result.destinasi_id, t)})
    print(data)
