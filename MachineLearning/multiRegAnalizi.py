import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # Sürekli model seçmek için model_selection ve verileri hem eğitip hem test etmek için train_test_split
from sklearn.linear_model import LinearRegression # Doğrusal model içindeki Linear Regression modeli
from sklearn.metrics import mean_squared_error # Modelin ne kadar iyi çalıştığını ölçmek için metrics (Ne kadar hatamız var onu ölçmek için)

# Veriyi hazırlama
data = {
    'Ev_Buyukluğu': [120,250,175,300,220],
    'Oda_Sayisi':[3,5,4,6,4],
    'Fiyat': [2400000,5000000,3500000,6000000,4400000]
}
df = pd.DataFrame(data) # Veriyi data frame'e çevir

X = df[['Ev_Buyukluğu','Oda_Sayisi']] # Girdi
y = df['Fiyat'] # Çıktı

# Modeli Eğitme
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state= 42) 

model = LinearRegression()
model.fit(X_train, y_train)

# Modeli Test Etme
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)

# print(f'Ortalama Kare Hatası (MSE): {mse}')

ev_buyuklugu = float(input("Lütfen evin büyüklüğünü(m²) girin: "))
oda_sayisi = float(input("Lütfen evin odasını sayısını girin: "))
tahmini_fiyat = model.predict([[ev_buyuklugu,oda_sayisi]])
print(f'Ev büyüklüğüne göre tahmini fiyat: {tahmini_fiyat[0]:.3f} TL')