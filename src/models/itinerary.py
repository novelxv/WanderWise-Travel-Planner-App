from datetime import date, time
from typing import Union

class Itinerary():
    itinerary_id    : int
    destinasi_id    : int
    lokasi          : str
    tanggal         : Union[date, str] 
    waktu_mulai     : Union[time, str]
    waktu_selesai   : Union[time, str]
    biaya           : int
    transportasi    : str
    catatan         : str
    def __init__(self, itinerary_id, destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan):
        self.itinerary_id = itinerary_id
        self.destinasi_id = destinasi_id
        self.lokasi = lokasi
        self.tanggal = tanggal
        self.waktu_mulai = waktu_mulai
        self.waktu_selesai = waktu_selesai
        if isinstance(waktu_mulai, str):
            self.waktu_mulai = time.fromisoformat(waktu_mulai)
        else:
            self.waktu_mulai = waktu_mulai
        if isinstance(waktu_selesai, str):
            self.waktu_selesai = time.fromisoformat(waktu_selesai)
        else:
            self.waktu_selesai = waktu_selesai
        self.biaya = biaya
        self.transportasi = transportasi
        self.catatan = catatan