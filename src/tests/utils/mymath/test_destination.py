import pytest

import src.controller.destinasi_controller as destinasi_controller
import src.models.destinasi as destinasi
from src.database.database import clear_db

@pytest.fixture
def tearDown(request):
    clear_db()
    request.addfinalizer(clear_db)

@pytest.fixture
def controller():
    return destinasi_controller.DestinasiController()

@pytest.fixture
def tests():
    return [{"nama":"Paris", "kategori" : "Plan", "tanggal_mulai": "2023-06-15", "tanggal_selesai" : "2023-06-20", "budget": 5000000, "tabungan" : 1000000},
                {"nama":'Singapore', "kategori" : 'Booked',  "tanggal_mulai": '2004-05-07',"tanggal_selesai" : '2004-09-07', "budget": 1000000,"tabungan" : 300000}]

def test_get_all_destinasi(controller, tests, tearDown):
    list_destinasi = []
    for i,entry in enumerate(tests):
        controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
        list_destinasi.append(destinasi.Destinasi(i+1, entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"]))
    result = controller.get_all_destinasi()
    for i in range(len(result)):
        assert result[i].destinasi_id == list_destinasi[i].destinasi_id
        assert result[i].nama == list_destinasi[i].nama
        assert result[i].kategori == list_destinasi[i].kategori
        assert result[i].tanggal_mulai == list_destinasi[i].tanggal_mulai
        assert result[i].tanggal_selesai == list_destinasi[i].tanggal_selesai
        assert result[i].budget == list_destinasi[i].budget
        assert result[i].tabungan == list_destinasi[i].tabungan

def test_get_destinasi_by_id(controller, tests):
    for entry in tests:
        controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    
    destinasi_id = 0
    result = controller.get_destinasi_by_id(destinasi_id)
    assert result.nama == tests[0]["nama"]
    assert result.kategori == tests[0]["kategori"]

def test_get_destinasi_by_kategory(controller, tests):
    for entry in tests:
        controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    
    kategori = "Plan"
    result = controller.get_destinasi_by_kategory(kategori)
    assert result.nama == tests[0]["nama"]
    assert result.kategori == tests[0]["kategori"]

def test_edit_destinasi(controller, tests):
    for entry in tests:
        controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    
    destinasi_id = 1
    updated_destinasi = {"nama": "Montenegro", "kategori": "Booked", "tanggal_mulai": "2023-07-01", "tanggal_selesai": "2023-07-10", "budget": 6000000, "tabungan": 1500000}
    controller.edit_destinasi(destinasi_id, updated_destinasi["nama"], updated_destinasi["kategori"], updated_destinasi["tanggal_mulai"], updated_destinasi["tanggal_selesai"], updated_destinasi["budget"], updated_destinasi["tabungan"])
    
    result = controller.get_destinasi_by_id(destinasi_id)
    assert result.nama == updated_destinasi["nama"]
    assert result.kategori == updated_destinasi["kategori"]
    assert result.tanggal_mulai == updated_destinasi["tanggal_mulai"]
    assert result.tanggal_selesai == updated_destinasi["tanggal_selesai"]
    assert result.budget == updated_destinasi["budget"]
    assert result.tabungan == updated_destinasi["tabungan"]

def test_delete_destinasi(controller, tests):
    for entry in tests:
        controller.add_destinasi(entry["nama"], entry["kategori"], entry["tanggal_mulai"], entry["tanggal_selesai"], entry["budget"], entry["tabungan"])
    
    destinasi_id = 1
    controller.delete_destinasi(destinasi_id)
    
    result = controller.get_destinasi_by_id(destinasi_id)
    assert result is None