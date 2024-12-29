import random
import time
kullanicilar = list()

def kullanici_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz!")
    ekle = input("Lütfen eklenecek kullanıcıyı yazınız: ")
    kullanicilar.append(ekle)
    input("Devam etmek için Enter tuşuna basınız!")
    

def kullanici_gör(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say) + "-Kullanıcı adı: ", i)
        say+=1
    print("-"*30)
    input("Devam etmek için Enter tuşuna basınız!")

def sec(x):
    say = 1
    kisi_sec = int(input("Kaç kişi seçilsin? "))
    rastgele_sec = random.sample(x,kisi_sec)

    for i in rastgele_sec:
        print(str(say) + "-Kullanıcı adı: ", i)
        say+=1
        print("Diğer kişi sistemden seçiliyor...")
        time.sleep(3)
    print("-"*30)
    input("Devam etmek için Enter tuşuna basınız!")

def karistir(x):
    say = 1
    random.shuffle(x) 
    for i in x:
        print(str(say) + "-Kullanıcı adı: ", i)
    print("-"*30)
    input("Devam etmek için Enter tuşuna basınız!")

while True:
    print("-"*30)
    print("****ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ!****")
    secim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n"))

    if secim == 1:
        kullanici_ekle(kullanicilar)
    elif secim == 2:
        kullanici_gör(kullanicilar)
    elif secim == 3:
        karistir(kullanicilar)
    elif secim == 4:
        print("Kişi seçme alanı bekleniyor...")
        time.sleep(2)
        sec(kullanicilar)
    else:
        print("Hatalı Seçim! Lütfen tekrar deneyiniz.")