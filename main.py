
def rehberiOku():
    rehber = []
    with open("rehber.txt", "r") as dosya:
        for satir in dosya:
            ad, telefon= satir.strip().split(",")
            rehber.append({"ad": ad[3:], "telefon": telefon[8:]})  # telefon yazısından hemen sonrası için 8 dedik
    return rehber

def rehberiYaz(rehber):
    # rehberde yapılan değişiklikler dosyaya düzenli bir şekilde yazılır ve her çalıştırmada güncel verileri elde ederiz.
    with open("rehber.txt", "w") as dosya:
        for kisi in rehber:
            dosya.write(f"Ad:{kisi['ad']},Telefon:{kisi['telefon']}\n")


def kisiEkleme(rehber):
    ad=input("Eklemek istediğiniz kisinin adi: ")
    telefon=int(input("Eklemek istediğiniz numara: "))

    kisi = {"ad": ad, "telefon": telefon}
    rehber.append(kisi)

    rehberiYaz(rehber)  # Rehberi dosyaya yaz


def kisiDuzenleme(rehber):
    ad=input("Duzenlemek istediğin kisinin adini gir: ")
    for kisi in rehber:
        if kisi['ad'] == ad:
            yeni_ad = input("Yeni adı girin (eski adı korumak için boş bırakabilirsiniz): ")
            yeni_telefon = input("Yeni telefon numarasını girin (eski numarayı korumak için boş bırakabilirsiniz): ")

            if yeni_ad:
                kisi['ad'] = yeni_ad
            if yeni_telefon:
                kisi['telefon'] = yeni_telefon

            print("Kişi başarıyla düzenlendi!")
            rehberiYaz(rehber)  # Rehberi dosyaya yaz

            return

    print("Kişi bulunamadı!")


def kisiSilme(rehber):
    ad=input("Silmek istediğin kisinin adini girin: ")

    for kisi in rehber:
        if kisi["ad"]==ad:
            rehber.remove(kisi)
            print("Kişi başarıyla silindi!")
            rehberiYaz(rehber)  # Rehberi dosyaya yaz
            return
    print("Kişi bulunamadı!")


def kisiListele(rehber):
    print("Rehberdeki Kişiler:")
    for kisi in rehber:
        print(f"Ad: {kisi['ad']}, Telefon: {kisi['telefon']}")

def kisiArama(rehber):
    aranan = input("Aranacak kişinin adını veya telefon numarasını girin: ")
    for kisi in rehber:
        if aranan in kisi["ad"] or aranan in kisi["telefon"] :
            print(f"Sonuçlar: Ad: {kisi['ad']}, Telefon: {kisi['telefon']}")

        else:
            print("Aranan kisi bulunamadı!!!")

def cikis():
    print("Rehberden çıkılıyor görüşürüz...")


def rehber():
    rehber = rehberiOku()

    while True:

        print("---Rehberdesiniz---")
        print("""
1-Kişi Ekleme
2-Kişi Düzenleme
3-Kişi Silme
4-Rehberdeki Kişileri Listeleme
5-Kişi Arama
6-Cikis """)

        islem = int(input("\n Bir işlem seciniz: "))

        if islem==1:
            kisiEkleme(rehber)

        elif islem==2:
            kisiDuzenleme(rehber)

        elif islem==3:
            kisiSilme(rehber)

        elif islem==4:
            kisiListele(rehber)

        elif islem==5:
            kisiArama(rehber)

        elif islem==6:
            cikis()
            break

        else:
            print("Lütfen 1-7 arası bir işlem seciniz")



rehber()


"""strip() bir dize (string) metodu olup, metnin başındaki ve sonundaki boşlukları,
 geçiş karakterlerini (newline, tab vb.) ve belirtilen karakterleri kaldırır."""