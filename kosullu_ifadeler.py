yas = int(input("Yaşınızı girin: "))
mezun_mu = input("Mezun musunuz? (evet/hayır) ").lower() == "evet"

if yas >= 18 and mezun_mu:
    print("Başvuru yapabilirsiniz.")
elif yas >= 18 and not mezun_mu:
    print("Yaş uygun ama mezun değilsiniz.")
else:
    print("Yaşınız uygun değil.")
