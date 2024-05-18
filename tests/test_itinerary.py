from datetime import date
from unittest import TestCase

from src.controller.itinerary_controller import ItineraryController
from src.models.itinerary import Itinerary
from src.database.database import clear_db


    # def test_get_destinasi_detail_by_tanggal(self):
    #     for i,entry in enumerate(self.tests):
    #         self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
    #     result = self.controller.get_destinasi_by_id(1)
    #     Itinerary_controller = ItineraryController()
    #     Itinerary_controller.add_itinerary(result.destinasi_id, "Upno", result.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    #     Itinerary_controller.add_itinerary(result.destinasi_id, "Waterboom", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
    #     Itinerary_controller.add_itinerary(result.destinasi_id, "Museum", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "mobil", "mahal")
    #     destinasidetail = Itinerary_controller.get_destinasi_detail_by_tanggal(result.destinasi_id, result.tanggal_mulai)
    #     print(destinasidetail)