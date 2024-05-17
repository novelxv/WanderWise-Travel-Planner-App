from datetime import date
from unittest import TestCase

from src.controller.destinasi_controller import DestinasiController
from src.controller.itinerary_controller import ItineraryController
from src.models.destinasi import Destinasi
from src.database.database import clear_db

class TestDestinasiController(TestCase):
    def setUp(self):
        self.controller = DestinasiController()
        self.tests = [{"nama":"Paris", "kategori" : "Plan", "tanggal_mulai": "2023-06-15", "tanggal_selesai" : "2023-06-20", "budget": 5000000, "tabungan" : 1000000},
                {"nama":'Singapore', "kategori" : 'Booked',  "tanggal_mulai": '2004-05-07',"tanggal_selesai" : '2004-09-07', "budget": 1000000,"tabungan" : 300000}]

    def tearDown(self) -> None:
        clear_db()

    def test_get_all_destinasi(self):
        list_destinasi = []
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
            list_destinasi.append(Destinasi(i+1, entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"]))
        result = self.controller.get_all_destinasi()
        self.assertEqual(result[0].destinasi_id, 1)
        assert result[0].nama == "Paris"
        assert result[0].tanggal_mulai == date(2023, 6, 15)
        assert result[0].tanggal_selesai == date(2023, 6, 20)
        assert result[0].budget == 5000000
        assert result[0].tabungan == 1000000

    def test_get_destinasi_by_id(self):
        list_destinasi = []
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
            list_destinasi.append(Destinasi(i+1, entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"]))
        
        result = self.controller.get_destinasi_by_id(1)
        self.assertEqual(result.destinasi_id, list_destinasi[0].destinasi_id)
        self.assertEqual(result.nama, list_destinasi[0].nama)
        self.assertEqual(result.kategori, list_destinasi[0].kategori)
        self.assertEqual(result.tanggal_mulai, list_destinasi[0].tanggal_mulai)
        self.assertEqual(result.tanggal_selesai, list_destinasi[0].tanggal_selesai)
        self.assertEqual(result.budget, list_destinasi[0].budget)
        self.assertEqual(result.tabungan, list_destinasi[0].tabungan)

    def test_get_destinasi_by_kategory(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
        result = self.controller.get_destinasi_by_kategory("Plan")
        self.assertEqual(result.nama, self.tests[0]["nama"])
        self.assertEqual(result.kategori, self.tests[0]["kategori"])

    def test_add_destinasi(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
        destinasi_id = 2
        self.controller.delete_destinasi(destinasi_id)
        result = self.controller.get_destinasi_by_id(destinasi_id)
        self.assertEqual(result, None)
    
    # def test_edit_destinasi(self):
    #     for i,entry in enumerate(self.tests):
    #         self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
    #     destinasi_id = 1
    #     updated_destinasi = {"nama": "Montenegro", "kategori": "Booked", "tanggal_mulai": "2023-07-01", "tanggal_selesai": "2023-07-10", "budget": 6000000, "tabungan": 1500000}
    #     self.controller.edit_destinasi(destinasi_id, updated_destinasi["nama"], updated_destinasi["kategori"], updated_destinasi["tanggal_mulai"], updated_destinasi["tanggal_selesai"], updated_destinasi["budget"], updated_destinasi["tabungan"])

    def test_delete_destinasi(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
        destinasi_id = 2
        self.controller.delete_destinasi(destinasi_id)
        result = self.controller.get_destinasi_by_id(destinasi_id)
        self.assertEqual(result, None)

    def test_get_destinasi_detail_by_tanggal(self):
        for i,entry in enumerate(self.tests):
            self.controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        
        result = self.controller.get_destinasi_by_id(1)
        Itinerary_controller = ItineraryController()
        Itinerary_controller.add_itinerary(result.destinasi_id, "Upno", result.tanggal_mulai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        Itinerary_controller.add_itinerary(result.destinasi_id, "Waterboom", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "motor", "mahal")
        Itinerary_controller.add_itinerary(result.destinasi_id, "Museum", result.tanggal_selesai, "18:00:00", "18:10:00", 10000, "mobil", "mahal")
        destinasidetail = Itinerary_controller.get_destinasi_detail_by_tanggal(result.destinasi_id, result.tanggal_mulai)
        print(destinasidetail)