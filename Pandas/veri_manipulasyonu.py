import pandas as pd

df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\Pandas\\teknolojik_urunler1.xlsx")

# Eksik verileri çek
# eksik_veriler = df.isnull()
# print(eksik_veriler)

# Değeri bulunmayan veri satırını sil
# eksik_veri_sil = df.dropna()
# print(eksik_veri_sil)

# Boş olan yerlere istediğin veriyi yazdırma
# bos_olan_yere_veri_yaz = df.fillna("Değer Yok")
# print(bos_olan_yere_veri_yaz)

# Herhangi bir veriyi integer değere çevirme
# df["Fiyat (TL)"] = df["Fiyat (TL)"].astype('Int64')
# print(df.dtypes)

# Herhangi bir değeri float değere çevirme
# df["Fiyat (TL)"] = df["Fiyat (TL)"].astype(float)
# print(df.dtypes)

# Belli bir sütun veya satırı data frameden çıkarma
# df.drop("Fiyat (TL)", axis=1, inplace=True) 

# Belli bir sütun data frame'e ekleme
#df.insert(2, 'Yeni Sütun', [1,2,3,4,5]) # Eğer böyle dersek 20 satır olan veri kadar dolmaz bunun yerine df.insert(2, 'Yeni Sütun', range(1,21))
#print(df.head())

# Verileri büyükten küçüğe sırala
# df_dusuk = df.sort_values(by='Fiyat (TL)',ascending=False) # ascending=false dememizin sebebi verilere dokunma dememizdir.
# print(df_dusuk)

# 5000 Tl üzeri fiyata sahip ürünleri verir
# df_fiyat_ust = df[df['Fiyat (TL)'] > 5000]
# print(df_fiyat_ust)

# 5000 Tl üzeri ve Mobil cihazlar kategorisinde olan ürünler
# df_filtreli = df[(df['Fiyat (TL)'] > 5000) & (df['Kategorei'] == 'Mobil Cihazlar')]
# print(df_filtreli)

# Lock metodu sütün veya satır seçimi yapar
df_secili = df.loc[:,['Ürün Adı', 'Fiyat (TL)']] # İki nokta koyarak Ürün adı ve fiyat kategorisinden öncekileri yazdırmıyoruz
print(df_secili) # İstenilen kategoriler yazdırılır

# İndeks numarasına göre veri seçmek istersek
df_ilk = df.iloc[:5,:] # Baştan ilk beşini ver gerisini verme 
print(df_ilk) # İlk 5 indeksin verilerini yazdırır

# SQL tarzı sorgulama
df_sorgu = df.query('Satış > 10')
# df_sorgu = df.query('Kategori == Televizyonlar')
print(df_sorgu) # Satış 10'dan fazla olan verileri verir.

#kategoriler içinde istediğimizi aramak için kullanıyoruz.
df_kategoriler = df[df['Kategoriler'].isin(['Bilgisayarlar','Mobil Cihazlar'])]
print(df_kategoriler) # Bilgisayarlar ve Mobil Cihazlar kategorilerindeki ürünlerin verilerini gösterir.

