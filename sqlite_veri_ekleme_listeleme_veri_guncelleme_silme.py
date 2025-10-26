import sqlite3

conn = sqlite3.connect("urunler.db")
cursor = conn.cursor()

# Veri ekleme
cursor.execute("INSERT INTO urun (isim, fiyat) VALUES (?, ?)", ("Kalem", 5.0))
cursor.execute("INSERT INTO urun (isim, fiyat) VALUES (?, ?)", ("Defter", 15.0))

conn.commit()

# Veri listeleme
cursor.execute("SELECT * FROM urun")
veriler = cursor.fetchall()
for veri in veriler:
    print(veri)
  
  # Fiyat güncelleme
cursor.execute("UPDATE urun SET fiyat = ? WHERE isim = ?", (6.0, "Kalem"))

# Veri silme
cursor.execute("DELETE FROM urun WHERE isim = ?", ("Defter",))

conn.close()
