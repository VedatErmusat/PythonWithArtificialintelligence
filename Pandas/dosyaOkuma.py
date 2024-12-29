import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\Pandas\\teknolojik_urunler1.xlsx")

# İlk birkaç satırı oku
# print(df.head())

# Tüm satırları oku
# print(df)

# Ortalama fiyat
# ortalama_fiyat = df['Fiyat (TL)'].mean()
# print(f"Ortalama Fiyat: {ortalama_fiyat} TL")

# En çok gelir getiren ürünü sırala
# kategori_bazli_satis = df.groupby('Kategori')['Satış'].sum()
# print(kategori_bazli_satis)

# En çok gelir getiren ürün
# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En çok gelir getiren ürün: \n{max_gelir}")

# Belli bir fiyatın üstündeki verileri çek
# fiyat_ust_urunler = df[df['Fiyat (TL)'] > 4000]
# print("Fiyatı 4000 TL'nin üstünde olanlar: \n",fiyat_ust_urunler)

# Yeni bir excel dosyasına söylenen verileri aktar
# fiyat_ust_urunler.to_excel('fiyatı_4000_üstü_olanlar.xlsx', index=False)

# Kategori ve Toplam fiyat verilerini çek
kategori_toplam_fiyat = df.groupby('Kategori')['Toplam Fiyat (TL)'].sum()
print("Kategoriler ve Toplam Fiyatları: \n",kategori_toplam_fiyat)
