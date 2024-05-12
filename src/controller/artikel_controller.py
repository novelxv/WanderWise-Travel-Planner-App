from database import *
from models.artikel import *

class ArtikelController:
    def __init__(self):
        conn,cursor = connect_db()
        self.conn = conn
        self.cursor = cursor
    
    def get_all_artikel(self):
        self.cursor.execute('''SELECT * FROM t_artikel''')
        artikel_list = self.cursor.fetchall()
        return artikel_list
    
    def get_artikel_by_id(self, id):
        self.cursor.execute('SELECT * FROM t_artikel WHERE artikel_id=?', (id,))
        artikel = self.cursor.fetchone()
        return artikel
    