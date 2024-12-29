import numpy as np 

# Kitap Fiyatları
kitap_fiyatlari = np.array([25,45,20,35,50,40,30])

# Satılan Kitap Adetleri 
satis_adetleri = np.array([100,150,200,120,130,80,110])

# Kitap Kategorileri
kategoriler = np.array(["Roman","Bilim","Çocuk","Tarih","Roman","Bilim","Çocuk"])


# toplam_gelir = kitap_fiyatlari*satis_adetleri
# print("Toplam Gelir: ",toplam_gelir)

# ortalama_fiyat = np.mean(kitap_fiyatlari)
# print("Ortalama Fiyat: ", ortalama_fiyat, 'TL')

# max_fiyat = np.max(kitap_fiyatlari)
# print("Max Fiyat: ", max_fiyat, 'TL')

# min_fiyat = np.min(kitap_fiyatlari)
# print("Min Fiyat: ", min_fiyat, 'TL')


romanlar = kitap_fiyatlari[kategoriler == "Roman"]
print("Roman Fiyatları: ", romanlar)

roman_satislari = satis_adetleri[kategoriler == "Roman"]
print("Roman Satış Adetleri: ", roman_satislari)

roman_toplam_satislari = np.sum(romanlar*roman_satislari)
print("Roman Toplam Satışları: ", roman_toplam_satislari)

print("-"*40)

veri = np.array([kitap_fiyatlari, satis_adetleri])
veri_reshaped = np.reshape(veri,(2,7))
print("Verilerin Şekillendirilmiş Hali: ",veri_reshaped)
