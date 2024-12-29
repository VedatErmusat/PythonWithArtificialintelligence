import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Veriyi yükle
df = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\VeriOnİslemeMuhendisligi\\teknolojik_urunler_zamanli.xlsx')
#fiyat ve satış sutunlarını seç
X = df[['Fiyat (TL)','Satış']]
#veriyi ölçeklendirelim
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#Kümeleme
kmeans = KMeans(n_clusters=3 , random_state=42)
df['Küme'] = kmeans.fit_predict(X_scaled)
#görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(df['Fiyat (TL)'], df['Satış'], c=df['Küme'], cmap='viridis')
plt.title('Ürünler için K-Means Kümeleme')
plt.xlabel('Fiyat (TL)')
plt.ylabel('Satış')

for i in range(len(df)):
    urun_adi_tarih_satis = f"{df['Ürün Adı'][i]} ({df['Tarih'][i].strftime('%d-%m-%Y')}) [{df['Satış'][i]} adet] {df['Fiyat (TL)'][i]} TL"
    plt.text(df['Fiyat (TL)'][i] + 220, df['Satış'][i] + 0.5 , urun_adi_tarih_satis, fontsize=9 , ha='right')
plt.show()

