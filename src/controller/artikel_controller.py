from src.database.database import *
from src.models.artikel import *

class ArtikelController:
    def __init__(self):
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor
    
    def get_all_artikel(self):
        result = self.cursor.execute('''SELECT * FROM t_artikel''').fetchall()
        artikel_list = []
        for row in result:
            artikel_list.append(Article(row[0], row[1], row[2], row[3], row[4]))
        return artikel_list
    
    def get_artikel_by_id(self, id):
        result = self.cursor.execute('SELECT * FROM t_artikel WHERE artikel_id=?', (id,)).fetchone()
        if result is not None:
            return Article(result[0], result[1], result[2], result[3], result[4])
        else:
            return None
    
    def add_artikel(self, judul, konten, penulis, tanggal_rilis):
        self.cursor.execute(
            '''INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
              VALUES (?,?,?,?)''', (judul, konten, penulis, tanggal_rilis,)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    