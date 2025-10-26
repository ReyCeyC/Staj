# For döngüsü
for i in range(1, 6):
    print(f"Sayı: {i}")

# While döngüsü
toplam = 0
n = 1
while n <= 5:
    toplam += n
    n += 1
print(f"Toplam: {toplam}")

def selamla(isim="Ziyaretçi"):
    print(f"Merhaba {isim}!")

def toplam(*sayilar):
    return sum(sayilar)

selamla("Ali")
print("Toplam:", toplam(1, 2, 3, 4))
# Liste
liste = [1, 2, 3]
liste.append(4)
print("Liste:", liste)

# Tuple
tup = (10, 20, 30)
print("Tuple:", tup)

# Sözlük
sozluk = {"isim": "Ali", "yas": 25}
print("Sözlük:", sozluk)

# Set
kume = set([1, 2, 2, 3])
print("Küme:", kume)
