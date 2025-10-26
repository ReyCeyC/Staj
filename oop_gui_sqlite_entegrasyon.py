import tkinter as tk
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

def urun_ekle():
    isim = isim_giris.get()
    fiyat = fiyat_giris.get()
    if isim and fiyat:
        u = Urun(isim, float(fiyat))
        u.veritabani_ekle()
        liste_guncelle()
        isim_giris.delete(0, tk.END)
        fiyat_giris.delete(0, tk.END)
        
def liste_guncelle():
    liste.delete(0, tk.END)
    for veri in Urun.listele():
        # veri[0]=id, veri[1]=isim, veri[2]=fiyat
        liste.insert(tk.END, f"{veri[1]} - {veri[2]} TL")

pencere = tk.Tk()
pencere.title("OOP + GUI + SQLite")
pencere.geometry("400x350")

tk.Label(pencere, text="Ürün İsmi:").pack()
isim_giris = tk.Entry(pencere)
isim_giris.pack()

tk.Label(pencere, text="Fiyat:").pack()
fiyat_giris = tk.Entry(pencere)
fiyat_giris.pack()

tk.Button(pencere, text="Ekle", command=urun_ekle).pack(pady=5)

liste = tk.Listbox(pencere)
liste.pack(fill=tk.BOTH, expand=True, pady=10)

liste_guncelle()
pencere.mainloop()
