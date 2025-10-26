import tkinter as tk

def listeye_ekle():
    veri = giris.get()
    if veri:
        liste.insert(tk.END, veri)
        giris.delete(0, tk.END)

def temizle():
    liste.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("Listbox Örneği")
pencere.geometry("300x250")

giris = tk.Entry(pencere)
giris.pack(pady=5)

ekle_buton = tk.Button(pencere, text="Ekle", command=listeye_ekle)
ekle_buton.pack(pady=5)

temizle_buton = tk.Button(pencere, text="Temizle", command=temizle)
temizle_buton.pack(pady=5)

liste = tk.Listbox(pencere)
liste.pack(pady=10, fill=tk.BOTH, expand=True)

pencere.mainloop()
