import sqlite3

class Urun:
    def __init__(self, isim, fiyat):
        self.isim = isim
        self.fiyat = fiyat

    def veritabani_ekle(self):
        conn = sqlite3.connect("urunler.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urun (isim, fiyat) VALUES (?, ?)", (self.isim, self.fiyat))
        conn.commit()
        conn.close()

    @staticmethod
    def listele():
        conn = sqlite3.connect("urunler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM urun")
        veriler = cursor.fetchall()
        conn.close()
        return veriler

u1 = Urun("Silgi", 3.0)
u2 = Urun("Cetvel", 7.5)

u1.veritabani_ekle()
u2.veritabani_ekle()

print(Urun.listele())
