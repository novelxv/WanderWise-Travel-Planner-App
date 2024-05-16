from database.database import *
from models.itinerary import *

class ItineraryController:
    def __init__(self):
        # Itinerary class constructor,connects instance to database
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor

    def get_all_itinerary(self):
        self.cursor.execute('''SELECT * FROM t_itinerary''')
        itinerary_list = self.cursor.fetchall()
        return itinerary_list
    
    def get_itinerary_by_id(self, id):
        self.cursor.execute('SELECT * FROM t_itinerary WHERE itinerary_id=?', (id,))
        itinerary = self.cursor.fetchone()
        return itinerary
    
    def get_destinasi_detail(self, id):
        self.cursor.execute('SELECT * FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=?', (id,))
        destinasidetail = self.cursor.fetchone()
        return destinasidetail
    
    def get_destinasi_detail_by_tanggal(self, id, tanggal):
        self.cursor.execute('SELECT * FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=? AND tanggal=?', (id,tanggal,))
        destinasidetail = self.cursor.fetchone()
        return destinasidetail
    
    def add_itinerary(self, destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan):
        self.cursor.execute(
            '''INSERT INTO t_itinerary (destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan)
              VALUES (?,?,?,?,?,?,?,?)''', (destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan,)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def delete_itinerary(self, id):
        self.cursor.execute('DELETE FROM t_itinerary WHERE itinerary_id=?', (id,))
        self.conn.commit()

    def edit_itinerary(self, destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan):
        self.cursor.execute('UPDATE t_itinerary SET nama=?, kategori=?, tanggal_mulai=?, tanggal_selesai=?, budget=?, tabungan=?', (destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan,))
        self.conn.commit()
        return id
