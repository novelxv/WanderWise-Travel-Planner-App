from datetime import date
from unittest import TestCase

from src.controller.artikel_controller import ArtikelController
from src.models.artikel import Article
from src.database.database import clear_db

class TestArtikelController(TestCase):
    def setUp(self):
        self.controller = ArtikelController()
        self.tests = [{"judul":"Things to bring in your vacation", "konten" : "Hello", "penulis": "J.K.Rowling", "tanggal_rilis" : "2023-06-20"},
                {"judul":'Travel Guide to Chicago', "konten" : 'Hi',  "penulis": 'Diana',"tanggal_rilis" : '2004-09-07'}]
 
    def tearDown(self) -> None:
        clear_db()

    def test_get_all_artikel(self):
        list_artikel = []
        for i,entry in enumerate(self.tests):
            self.controller.add_artikel(entry["judul"], entry["konten"], entry["penulis"], entry["tanggal_rilis"])
            list_artikel.append(Article(i+1, entry["judul"], entry["konten"], entry["penulis"], entry["tanggal_rilis"]))
        result = self.controller.get_all_artikel()
        assert result[0].judul == "Things to bring in your vacation"
        assert result[0].konten == "Hello"
        assert result[0].penulis == "J.K.Rowling"
        assert result[0].tanggal_rilis == date(2023, 6, 20)

    def test_get_artikel_by_id(self):
        list_artikel = []
        for i,entry in enumerate(self.tests):
            self.controller.add_artikel(entry["judul"], entry["konten"], entry["penulis"], entry["tanggal_rilis"])
            list_artikel.append(Article(i+1, entry["judul"], entry["konten"], entry["penulis"], entry["tanggal_rilis"]))
        result = self.controller.get_artikel_by_id(1)

        self.assertEqual(result.judul, list_artikel[0].judul)
        self.assertEqual(result.konten, list_artikel[0].konten)
        self.assertEqual(result.penulis, list_artikel[0].penulis)
        self.assertEqual(result.tanggal_rilis, list_artikel[0].tanggal_rilis)