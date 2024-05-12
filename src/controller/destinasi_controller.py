from database import *
from models.destinasi import *

class DestinasiController:
    def __init__(self):
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor
    
    # get all destinasi from t_destinasi
    def get_all_destinasi(self):
        self.cursor.execute('''SELECT * FROM t_destinasi''')
        destinasi_list = self.cursor.fetchall()
        return destinasi_list
    
    # get all destinasi from t_destinasi with destinasi_id=id
    def get_destinasi_by_id(self, id):
        self.cursor.execute('SELECT * FROM t_destinasi WHERE destinasi_id=?', (id,))
        destinasi = self.cursor.fetchone()
        return destinasi
    
    # get all destinasi from t_destinasi with the corresponding kategori
    def get_destinasi_by_kategory(self, kategori):
        self.cursor.execute('SELECT * FROM t_destinasi WHERE kategori=?', (kategori,))
        destinasi = self.cursor.fetchone()
        return destinasi
    
    def add_destinasi(self, nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan):
        self.cursor.execute(
            '''INSERT INTO t_destinasi (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan)
              VALUES (?,?,?,?,?,?)''', (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan,)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def delete_destinasi(self, id):
        self.cursor.execute('DELETE FROM t_destinasi WHERE destinasi_id=?', (id,))
        self.conn.commit()

    def edit_destinasi(self, nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan):
        self.cursor.execute('UPDATE t_destinasi SET nama=?, kategori=?, tanggal_mulai=?, tanggal_selesai=?, budget=?, tabungan=?', (nama, kategori, tanggal_mulai, tanggal_selesai, budget, tabungan,))
        self.conn.commit()
        return id
        