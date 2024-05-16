from datetime import date
from typing import Union

class Destinasi():
    destinasi_id    : int
    nama            : str
    kategori        : str
    tanggal_mulai   : Union[date, str]
    tanggal_selesai : Union[date, str]
    budget          : int
    tabungan        : int

    def __init__(self, destinasi_id, nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan):
        self.destinasi_id = destinasi_id
        self.nama = nama
        self.kategori = kategori
        if isinstance(tanggal_mulai, str):
            self.tanggal_mulai = date.fromisoformat(tanggal_mulai)
        else:
            self.tanggal_mulai = tanggal_mulai
        if isinstance(tanggal_selesai, str):
            self.tanggal_selesai = date.fromisoformat(tanggal_selesai)
        else:
            self.tanggal_selesai = tanggal_selesai
        self.budget = budget
        self.tabungan = tabungan

    @property
    def progress_tabungan(self):
        selisih = self.budget - self.tabungan 
        return (selisih/self.budget) * 100