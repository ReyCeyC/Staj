import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.title("İlk Tkinter Pencerem")
pencere.geometry("300x200")

etiket = tk.Label(pencere, text="Merhaba Dünya!", font=("Arial", 14))
etiket.pack(pady=20)

def mesaj_goster():
    messagebox.showinfo("Bilgi", "Butona tıklandı!")

buton = tk.Button(pencere, text="Tıkla", command=mesaj_goster)
buton.pack()

pencere.mainloop()
