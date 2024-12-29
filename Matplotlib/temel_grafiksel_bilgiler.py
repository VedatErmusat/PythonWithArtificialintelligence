import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Örnek veri
df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\Pandas\\teknolojik_urunler_zamanli.xlsx")
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True) # Tarihe göre sıralamasını istiyoruz, eğer indeksleme yapmazsak çalışmaz.

# Satışların zaman içerisindeki değişimini gösteren bir zaman grafiği
# df['Satış'].plot(title='Satışların Zaman İçerisindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
# df['Fiyat (TL)'].plot(title='Satışların Zaman İçerisindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
# plt.show()

#Zaman İçerisindeki Aylık Satışları Gösteren Bar Grafiği
aylik_satis = df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='bar', title='Aylık ToplamSatışlar', xlabel='Ay', ylabel='Toplam Satış')
# plt.show()

# Pasta Grafiği
# kategori_satis = df.groupby('Kategori')['Satış'].sum()
# kategori_satis.plot(kind='pie', autopct='%1.1f%%',title='Kategoriye Göre Toplam Satışlar') #  autopct='%1.1f%%' bunu kullanmamızın sebebi virgülden sonra 1 basamağı benim için al yeterli
# plt.ylabel('')  # Y eksenini gizle
# plt.show()

# Scatter yani fiyat ve satış miktarı arasındaki dağılımı göster
# df.plot(kind='scatter', x='Fiyat (TL)', y='Satış', title='Fiyat ve Satış İlişkisi')
# plt.show()

# df['Fiyat (TL)'].plot(kind='hist', bins = 10, title='Fiyat Dağılımı')
# plt.xlabel('Fiyat (TL)')
# plt.show()

# Aylık satış trendi
# aylik_satis = df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='line', title='Aylık Satış Miktarları')
# plt.xlabel('Ay')
# plt.ylabel('Satış Miktarı')
# plt.show()


# Eksik ve sonsuz değerleri temizle
# df = df.dropna()
# df = df[np.isfinite(df['Fiyat (TL)']) & np.isfinite(df['Satış'])]

# Fiyat ve satış ilişkisinin grafiği
# df.plot(kind='scatter', x='Fiyat (TL)', y='Satış', title='Fiyat ve Satış İlişkisi')

# Polinom fonksiyonu ve trend çizgisi
# z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1) # Polinom fonksiyonu kullandık, Fiyat ve satışı karşılaştırıp aralarına '1' tane çizgi atılacak
# p = np.poly1d(z) # 1. dereceden bir polinomu analiz et
# plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
# plt.show()

# Dağıtım ve Kategorizasyonu analiz ederken
# bins = [0,2000,5000,10000,20000,30000]
# labels = ['Düşük','Orta','Yüksek','Çok Yüksek','Lüks']
# df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins= bins, labels=labels) # 'df fiyat' içerisindeki veriyi cut fonksiyonuyla 'df fiyat kategorisine' çekiyoruz
# Fiyat kategorisine göre fiyat dağılımı
# df.groupby('Fiyat Kategorisi', observed=False)['Satış'].sum().plot(kind='bar', title='Fiyat Kategorisine Göre Toplam Satışlar')
# plt.xlabel('Fiyat Kategorisi')
# plt.ylabel('Toplam Satış')
# plt.show()