from datetime import date, time
from unittest import TestCase

from src.controller.itinerary_controller import ItineraryController
from src.controller.destinasi_controller import DestinasiController
from src.models.itinerary import Itinerary
from src.database.database import clear_db

class TestItineraryController(TestCase):
    def setUp(self):
        destinasi_controller = DestinasiController()
        self.controller = ItineraryController()
        destinasi_controller.add_destinasi("Montenegro", "Booked", "2023-06-15", "2023-06-20",5000000, 1000000)
        destinasi_controller.add_destinasi("Indonesia", "Idea", "2023-06-15", "2023-06-20",5000000, 1000000)

        # des1 = destinasi_controller.get_destinasi_by_id(1)
        # des2 = destinasi_controller.get_destinasi_by_id(2)
        # self.controller.add_itinerary(des1.destinasi_id, "Upno", des1.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        # self.controller.add_itinerary(des1.destinasi_id, "Museum", des1.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        # self.controller.add_itinerary(des2.destinasi_id, "Upno", des2.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        # self.controller.add_itinerary(des2.destinasi_id, "Waterboom", des2.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        self.tests = [{"destinasi_id": 1, "lokasi": "Upno", "tanggal": "2023-06-15", "waktu_mulai": "18:00:00", "waktu_selesai": "18:10:00", "biaya": 10000, "transportasi": "motor", "catatan": "mahal"},
                      {"destinasi_id": 1, "lokasi": "Museum", "tanggal": "2023-06-20", "waktu_mulai": "18:00:00", "waktu_selesai": "18:10:00", "biaya": 10000, "transportasi": "motor", "catatan": "mahal"},
                      {"destinasi_id": 2, "lokasi": "Upno", "tanggal": "2023-06-15", "waktu_mulai": "18:00:00", "waktu_selesai": "18:10:00", "biaya": 10000, "transportasi": "motor", "catatan": "mahal"},
                      {"destinasi_id": 2, "lokasi": "Waterboom", "tanggal": "2023-06-20", "waktu_mulai": "18:00:00", "waktu_selesai": "18:10:00", "biaya": 10000, "transportasi": "motor", "catatan": "mahal"}]
        
    def tearDown(self) -> None:
        clear_db()

    def test_get_all_itinerary(self):
        list_itinerary = []
        for i,entry in enumerate(self.tests):
            self.controller.add_itinerary(entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"])
            list_itinerary.append(Itinerary(i+1, entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"]))
        
        result = self.controller.get_all_itinerary()

        for i,entry in enumerate(self.tests):
            assert result[i].destinasi_id == list_itinerary[i].destinasi_id
            assert result[i].lokasi == list_itinerary[i].lokasi
            assert result[i].tanggal == list_itinerary[i].tanggal
            assert result[i].waktu_mulai == list_itinerary[i].waktu_mulai
            assert result[i].waktu_selesai == list_itinerary[i].waktu_selesai
            assert result[i].biaya == list_itinerary[i].biaya
            assert result[i].transportasi == list_itinerary[i].transportasi
            assert result[i].catatan == list_itinerary[i].catatan

    def test_get_itinerary_by_id(self):
        list_itinerary = []
        for i,entry in enumerate(self.tests):
            self.controller.add_itinerary(entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"])
            list_itinerary.append(Itinerary(i+1, entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"]))
        
        result = self.controller.get_itinerary_by_id(1)
        assert result.destinasi_id == list_itinerary[0].destinasi_id
        assert result.lokasi == list_itinerary[0].lokasi
        assert result.tanggal == list_itinerary[0].tanggal
        assert result.waktu_mulai == list_itinerary[0].waktu_mulai
        assert result.waktu_selesai == list_itinerary[0].waktu_selesai
        assert result.biaya == list_itinerary[0].biaya
        assert result.transportasi == list_itinerary[0].transportasi
        assert result.catatan == list_itinerary[0].catatan

    # def test_get_destinasi_detail(self):
    #     result = self.controller.get_destinasi_detail()

    # def test_get_destinasi_detail_by_tanggal(self):
    #     result = self.controller.get_destinasi_detail()

    # def test_get_lokasi_by_tanggal(self):
    #     result = self.controller.get_destinasi_detail()

    # def test_get_tanggal_itinerary(self):
    #     result = self.controller.get_destinasi_detail()

    def test_add_itinerary(self):
        query = self.controller.add_itinerary(2, "Upno", "2024-06-11", "05:00:00", "09:10:00", 10000, "mobil", "minumannya recommended")
        result = self.controller.get_itinerary_by_id(query)
        self.assertEqual(result.destinasi_id, 2)
        self.assertEqual(result.lokasi, "Upno")
        self.assertEqual(result.tanggal, date(2024, 6, 11))
        self.assertEqual(result.waktu_mulai, time(5,0,0))
        self.assertEqual(result.waktu_selesai, time(9,10,0))
        self.assertEqual(result.biaya, 10000)
        self.assertEqual(result.transportasi, "mobil")
        self.assertEqual(result.catatan, "minumannya recommended")
    
    def test_edit_itinerary(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_itinerary(entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"])
        
        itinerary_id = 2
        updated_itinerary = {"destinasi_id": 1, "lokasi": "Library", "tanggal": "2023-06-15", "waktu_mulai": "18:00:00", "waktu_selesai": "18:10:00", "biaya": 10000, "transportasi": "motor", "catatan": "mahal"}
        self.controller.edit_itinerary(itinerary_id, updated_itinerary["destinasi_id"], updated_itinerary["lokasi"], updated_itinerary["tanggal"], updated_itinerary["waktu_mulai"], updated_itinerary["waktu_selesai"], updated_itinerary["biaya"], updated_itinerary["transportasi"], updated_itinerary["catatan"])
        updated_result = self.controller.get_itinerary_by_id(itinerary_id)
        self.assertEqual(updated_result.lokasi, updated_itinerary["lokasi"])

    def test_delete_itinerary(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_itinerary(entry["destinasi_id"], entry["lokasi"], entry["tanggal"], entry["waktu_mulai"], entry["waktu_selesai"], entry["biaya"], entry["transportasi"], entry["catatan"])
        
        itinerary_id = 2
        self.controller.delete_itinerary(itinerary_id)
        result = self.controller.get_itinerary_by_id(itinerary_id)
        self.assertEqual(result, None)