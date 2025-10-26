import tkinter as tk

class Urun:
    def __init__(self, isim, fiyat):
        self.isim = isim
        self.fiyat = fiyat

    def bilgi(self):
        return f"{self.isim} - {self.fiyat} TL"

def urun_ekle():
    isim = isim_giris.get()
    fiyat = fiyat_giris.get()
    if isim and fiyat:
        u = Urun(isim, fiyat)
        liste.insert(tk.END, u.bilgi())
        isim_giris.delete(0, tk.END)
        fiyat_giris.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("OOP + GUI")
pencere.geometry("350x300")

tk.Label(pencere, text="Ürün İsmi:").pack()
isim_giris = tk.Entry(pencere)
isim_giris.pack()

tk.Label(pencere, text="Fiyat:").pack()
fiyat_giris = tk.Entry(pencere)
fiyat_giris.pack()

tk.Button(pencere, text="Ekle", command=urun_ekle).pack(pady=5)

liste = tk.Listbox(pencere)
liste.pack(fill=tk.BOTH, expand=True, pady=10)

pencere.mainloop()
