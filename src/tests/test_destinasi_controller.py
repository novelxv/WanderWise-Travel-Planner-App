import pytest
from unittest import TestCase

from src.controller.destinasi_controller import DestinasiController
from src.models.destinasi import Destinasi
from src.database.database import clear_db

class TestDestinasi(TestCase):
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
        self.assertEqual(len(result), 2)
        for i in range(len(result)):
            self.assertEqual(result[i].destinasi_id, list_destinasi[i].destinasi_id)
            self.assertEqual(result[i].nama, list_destinasi[i].nama)
            self.assertEqual(result[i].kategori, list_destinasi[i].kategori)
            self.assertEqual(result[i].tanggal_mulai, list_destinasi[i].tanggal_mulai)
            self.assertEqual(result[i].tanggal_selesai, list_destinasi[i].tanggal_selesai)
            self.assertEqual(result[i].budget, list_destinasi[i].budget)
            self.assertEqual(result[i].tabungan, list_destinasi[i].tabungan)