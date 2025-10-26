import sqlite3

# Veritabanı bağlantısı oluşturuldu (dosya yoksa oluşturulur)
conn = sqlite3.connect("urunler.db")
cursor = conn.cursor()

# Tablo oluşturuldu
cursor.execute("""
CREATE TABLE IF NOT EXISTS urun (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT NOT NULL,
    fiyat REAL NOT NULL
)
""")

conn.commit()
conn.close()
