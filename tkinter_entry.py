import tkinter as tk
from tkinter import messagebox

def selamla():
    isim = giris.get()
    messagebox.showinfo("Merhaba", f"Merhaba {isim}!")

pencere = tk.Tk()
pencere.title("Kullanıcı Girişi")
pencere.geometry("300x150")

etiket = tk.Label(pencere, text="İsminizi giriniz:")
etiket.pack()

giris = tk.Entry(pencere)
giris.pack(pady=5)

buton = tk.Button(pencere, text="Gönder", command=selamla)
buton.pack(pady=10)

pencere.mainloop()
