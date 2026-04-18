import random
import time
Liste=["Alanyaspor",
    "Antalyaspor",
    "Başakşehir",
    "Beşiktaş",
    "Çaykur Rizespor",
    "Eyüpspor",
    "Fatih Karagümrük",
    "Fenerbahçe",
    "Galatasaray",
    "Gaziantep FK",
    "Gençlerbirliği",
    "Göztepe",
    "Kasımpaşa",
    "Kayserispor",
    "Kocaelispor",
    "Konyaspor",
    "Samsunspor",
    "Trabzonspor"]
Kelime=random.choice(Liste).lower()
Harfler="abcçdefgğhiıjklmnoöprsştuüvyz"
Sayı1 = 7
tahmin = ""
Kapatma = 0
yapılantahmin = ""
adam1= ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
--------"""]
print(
        "Merhaba Adam asmaca oyununa hoş geldiniz.Oyunda yedi can hakkına sahipsiniz.Oyunun konusu süperlig takımlarıdır.")
while Kapatma != 1:
    yanitrun = input(
        " Oyunu Başlatmak için 'Start',Çıkmak için 'Exit',Hakkındaya Girmek için ise 'About' yazınız(Konsola yazarken tırnak kullanmanız gerekmez!!).\n=====>").lower()
    if yanitrun == "start":
        while Sayı1>0:

            dogrukelime = ""

            for i in Kelime:
                if i in yapılantahmin:
                    dogrukelime += i
                else:
                    dogrukelime += "_"

            print(adam1[7 - Sayı1])
            print("Toplam", Sayı1, "canınız kaldı")
            print("Kelime:", " ".join(dogrukelime))

            if dogrukelime == Kelime:
                print("Tebrikler, yarışmayı kazandınız!")
                break

            yanit1 = input("Bir Harf Giriniz.\n=====>").lower()
            if yanit1 not in Harfler or len(yanit1) != 1:
                print("Lütfen geçerli bir harf giriniz!")
                continue
            if yanit1 in yapılantahmin:
                print("Bu harfi zaten tahmin ettiniz!")
                continue

            if yanit1 in Harfler:
                yapılantahmin += yanit1
                if yanit1 not in Kelime:
                    Sayı1 = Sayı1 - 1
            else:
                print("Lütfen geçerli bir harf giriniz!")

        else:
            print("Kaybettiniz!")
            print("Doğru kelime", Kelime)
            exit()
        yanitrun = ""
    elif yanitrun == "exit":
        print("Kapatılıyor...")
        time.sleep(3)
        Kapatma = 1
        exit()
    elif yanitrun == "about":
        print("Oyunu Geliştiren Krms13,\nOyunun sürümü Adamasmaca1.0")
        yanitrun = ""
    elif yanitrun == "easteregg":
        print("Easter Egg özelliğe Hoş Geldiniz")
        print("liste yükleniyor")
        time.sleep(3)
        print(Liste)
        yanitrun = ""
