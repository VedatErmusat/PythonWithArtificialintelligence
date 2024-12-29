import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Veriyi yükle
df = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\VeriOnİslemeMuhendisligi\\veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

# Eksik verileri doldur
df.fillna(df['Gelir'].mean(), inplace=True)

# İlgili sütunları seçelim (Yaş ve Gelir üzerinden kümeleme yapalım)
X = df[['Yaş', 'Gelir']]

# Veriyi ölçeklendirelim (Kümeleme algoritması için veriyi ölçeklendirmek önemlidir)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means Modeli
kmeans = KMeans(n_clusters=3, random_state=42)  # 3 küme
kmeans.fit(X_scaled)

# Kümeleri tahmin edelim
df['Küme'] = kmeans.labels_

# Orijinal verilerle kümeleri görselleştirelim (Ölçeklendirilmiş yerine orijinal yaş ve gelir verilerini kullanıyoruz)
plt.figure(figsize=(8, 6))
plt.scatter(df['Yaş'], df['Gelir'], c=df['Küme'], cmap='viridis')
plt.title('K-Means Kümeleme (Orijinal Yaş ve Gelir)')
plt.xlabel('Yaş')
plt.ylabel('Gelir')
plt.show()
