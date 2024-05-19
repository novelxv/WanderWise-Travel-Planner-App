from src.database.database import *
from src.models.itinerary import *

class ItineraryController:
    def __init__(self):
        # Itinerary class constructor,connects instance to database
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor

    def get_all_itinerary(self):
        result = self.cursor.execute('SELECT * FROM t_itinerary').fetchall()
        itinerary_list = []
        for row in result:
            itinerary_list.append(Itinerary(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return itinerary_list
    
    def get_itinerary_by_id(self, id):
        result = self.cursor.execute('SELECT * FROM t_itinerary WHERE itinerary_id=?', (id,)).fetchone()
        if result is not None:
            return Itinerary(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
        else:
            return None
    
    def get_destinasi_detail(self, id):
        result = self.cursor.execute('SELECT * FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=?', (id,)).fetchall()
        print(result) # debug
        itinerary_list = []
        for row in result:
            itinerary_list.append(Itinerary(row[7], row[0], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))
        print(itinerary_list) # debug
        return itinerary_list 

    
    def get_destinasi_detail_by_tanggal(self, id, tanggal):
        result = self.cursor.execute('SELECT * FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=? AND tanggal=?', (id,tanggal,)).fetchall()
        itinerary_list = []
        for row in result:
            itinerary_list.append(Itinerary(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return itinerary_list
    
    def get_lokasi_by_tanggal(self, id, tanggal):
        self.cursor.execute('SELECT lokasi FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=? AND tanggal=?', (id,tanggal,))
        lokasi = self.cursor.fetchall()
        return lokasi
    
    def get_tanggal_itinerary(self, id):
        self.cursor.execute('SELECT tanggal FROM t_destinasi NATURAL JOIN t_itinerary WHERE destinasi_id=?', (id,))
        tanggals = self.cursor.fetchall()
        tanggal = [t[0] for t in tanggals]
        return tanggal
    
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

    def edit_itinerary(self, itinerary_id, destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan):
        self.cursor.execute('UPDATE t_itinerary SET destinasi_id=?, lokasi=?, tanggal=?, waktu_mulai=?, waktu_selesai=?, biaya=?, transportasi=?, catatan=? WHERE itinerary_id=?', (destinasi_id, lokasi, tanggal, waktu_mulai, waktu_selesai, biaya, transportasi, catatan, itinerary_id, ))
        self.conn.commit()
        return itinerary_id
