sayi1 = 10
sayi2 = 3

print("Toplama:", sayi1 + sayi2) # 13
print("Çıkarma:", sayi1 - sayi2) # 7
print("Çarpma:", sayi1 * sayi2) # 30
print("Bölme:", sayi1 / sayi2) # 3.333...
print("Mod alma:", sayi1 % sayi2) # 1


yas = int(input("Yaşınızı girin: "))
mezun_mu = input("Mezun musunuz? (evet/hayır) ").lower() == "evet"


if yas >= 18 and mezun_mu:
    print("Başvuru yapabilirsiniz.")
elif yas >= 18 and not mezun_mu:
    print("Yaş uygun ama mezun değilsiniz.")
else:
    print("Yaşınız uygun değil.")
