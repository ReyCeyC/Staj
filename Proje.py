import tkinter as tk
from tkinter import messagebox
import sqlite3

class Urun:
    def __init__(self, isim, fiyat, miktar):
        self.isim = isim
        self.fiyat = fiyat
        self.miktar = miktar

    def veritabani_ekle(self):
        conn = sqlite3.connect("stok.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS urun (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                fiyat REAL NOT NULL,
                miktar INTEGER NOT NULL
            )
        """)
        cursor.execute("INSERT INTO urun (isim, fiyat, miktar) VALUES (?, ?, ?)",
                       (self.isim, self.fiyat, self.miktar))
        conn.commit()
        conn.close()

    @staticmethod
    def listele():
        conn = sqlite3.connect("stok.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM urun")
        veriler = cursor.fetchall()
        conn.close()
        return veriler

def veritabani_olustur():
    conn = sqlite3.connect("stok.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urun (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            fiyat REAL NOT NULL,
            miktar INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def liste_guncelle():
    liste.delete(0, tk.END)
    toplam = 0
    for veri in Urun.listele():
        liste.insert(tk.END, f"{veri[0]} | {veri[1]} - {veri[2]} TL x {veri[3]} adet")
        toplam += veri[2] * veri[3]
    toplam_label.config(text=f"Toplam Stok Değeri: {toplam} TL")

def urun_ekle():
    isim = isim_giris.get()
    fiyat = fiyat_giris.get()
    miktar = miktar_giris.get()
    if isim and fiyat and miktar:
        try:
            u = Urun(isim, float(fiyat), int(miktar))
            u.veritabani_ekle()
            liste_guncelle()
            isim_giris.delete(0, tk.END)
            fiyat_giris.delete(0, tk.END)
            miktar_giris.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Hata", "Lütfen geçerli bir fiyat ve miktar girin.")

def urun_ara():
    ara = ara_giris.get()
    liste.delete(0, tk.END)
    conn = sqlite3.connect("stok.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urun WHERE isim LIKE ?", ('%' + ara + '%',))
    veriler = cursor.fetchall()
    toplam = 0
    for veri in veriler:
        liste.insert(tk.END, f"{veri[0]} | {veri[1]} - {veri[2]} TL x {veri[3]} adet")
        toplam += veri[2] * veri[3]
    toplam_label.config(text=f"Toplam Stok Değeri: {toplam} TL")
    conn.close()

def urun_duzelt():
    secili = liste.curselection()
    if secili:
        secili_satir = liste.get(secili[0])
        urun_id = secili_satir.split(" | ")[0]
        yeni_isim = isim_giris.get()
        yeni_fiyat = fiyat_giris.get()
        yeni_miktar = miktar_giris.get()
        if yeni_isim and yeni_fiyat and yeni_miktar:
            try:
                conn = sqlite3.connect("stok.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE urun SET isim=?, fiyat=?, miktar=? WHERE id=?",
                               (yeni_isim, float(yeni_fiyat), int(yeni_miktar), urun_id))
                conn.commit()
                conn.close()
                liste_guncelle()
            except ValueError:
                messagebox.showwarning("Hata", "Lütfen geçerli bir fiyat ve miktar girin.")

def urun_sil():
    secili = liste.curselection()
    if secili:
        secili_satir = liste.get(secili[0])
        urun_id = secili_satir.split(" | ")[0]
        conn = sqlite3.connect("stok.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM urun WHERE id=?", (urun_id,))
        conn.commit()
        conn.close()
        liste_guncelle()

def liste_temizle():
    liste.delete(0, tk.END)
    toplam_label.config(text="Toplam Stok Değeri: 0 TL")


pencere = tk.Tk()
pencere.title("Stok Takip Uygulaması")
pencere.geometry("500x450")

tk.Label(pencere, text="Ürün İsmi:").pack()
isim_giris = tk.Entry(pencere)
isim_giris.pack()

tk.Label(pencere, text="Fiyat (TL):").pack()
fiyat_giris = tk.Entry(pencere)
fiyat_giris.pack()

tk.Label(pencere, text="Miktar:").pack()
miktar_giris = tk.Entry(pencere)
miktar_giris.pack()

tk.Label(pencere, text="Ürün Ara:").pack()
ara_giris = tk.Entry(pencere)
ara_giris.pack()

tk.Button(pencere, text="Ekle", command=urun_ekle).pack(pady=3)
tk.Button(pencere, text="Ara", command=urun_ara).pack(pady=3)
tk.Button(pencere, text="Düzelt", command=urun_duzelt).pack(pady=3)
tk.Button(pencere, text="Sil", command=urun_sil).pack(pady=3)
tk.Button(pencere, text="Listeyi Temizle", command=liste_temizle).pack(pady=3)
tk.Button(pencere, text="Tüm Listeyi Göster", command=liste_guncelle).pack(pady=3)

liste = tk.Listbox(pencere)
liste.pack(fill=tk.BOTH, expand=True, pady=10)

toplam_label = tk.Label(pencere, text="Toplam Stok Değeri: 0 TL")
toplam_label.pack()

veritabani_olustur()
liste_guncelle()

pencere.mainloop()
