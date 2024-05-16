from datetime import date
from typing import Union

class Article():
    artikel_id      :int
    judul           :str
    konten          :str
    penulis         :str
    tanggal_rilis   :Union[date, str]
    def __init__(self, artikel_id, judul, konten, penulis, tanggal_rilis):
        self.artikel_id = artikel_id
        self.judul = judul
        self.konten = konten
        self.penulis = penulis
        if isinstance(tanggal_rilis, str):
            self.tanggal_rilis = date.fromisoformat(tanggal_rilis)
        else:
            self.tanggal_rilis = tanggal_rilis