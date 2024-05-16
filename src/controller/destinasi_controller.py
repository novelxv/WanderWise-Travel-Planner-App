from database.database import *
from models.destinasi import *

class DestinasiController:
    def __init__(self):
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor
    
    # get all destinasi from t_destinasi
    def get_all_destinasi(self):
        result = self.cursor.execute('''SELECT * FROM t_destinasi''').fetchall()
        destinasi_list = []
        for row in result:
            destinasi_list.append(Destinasi(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return destinasi_list
    
    # get all destinasi from t_destinasi with destinasi_id=id
    def get_destinasi_by_id(self, id):
        result = self.cursor.execute('SELECT * FROM t_destinasi WHERE destinasi_id=?', (id,)).fetchone()
        if result is not None:
            return Destinasi((result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        else:
            return None
    
    # get all destinasi from t_destinasi with the corresponding kategori
    def get_destinasi_by_kategory(self, kategori):
        result = self.cursor.execute('SELECT * FROM t_destinasi WHERE kategori=?', (kategori,)).fetchone
        if result is not None:
            return Destinasi(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        else:
            return None

    # add new destinasi 
    def add_destinasi(self, nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan):
        self.cursor.execute(
            '''INSERT INTO t_destinasi (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan)
              VALUES (?,?,?,?,?,?)''', (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan,)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    # delete destinasi from the existing db
    def delete_destinasi(self, id):
        self.cursor.execute('DELETE FROM t_destinasi WHERE destinasi_id=?', (id,))
        self.conn.commit()

    # update destinasi of the existing db
    def edit_destinasi(self, destinasi_id, nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan):
        self.cursor.execute('UPDATE t_destinasi SET nama=?, kategori=?, tanggal_mulai=?, tanggal_selesai=?, budget=?, tabungan=? WHERE destinasi_id=?', (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan, destinasi_id,))
        self.conn.commit()
        return destinasi_id
        