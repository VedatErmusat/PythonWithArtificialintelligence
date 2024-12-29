import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # Sürekli model seçmek için model_selection ve verileri hem eğitip hem test etmek için train_test_split
from sklearn.linear_model import LinearRegression # Doğrusal model içindeki Linear Regression modeli
from sklearn.metrics import mean_squared_error # Modelin ne kadar iyi çalıştığını ölçmek için metrics (Ne kadar hatamız var onu ölçmek için)

# Veriyi hazırlama
data = {
    'Ev_Buyukluğu': [120,250,175,300,220],
    'Fiyat': [2400000,5000000,3500000,6000000,4400000]
}
df = pd.DataFrame(data) # Veriyi data frame'e çevir

X = df[['Ev_Buyukluğu']] # Girdi
y = df['Fiyat'] # Çıktı

# %20'sini test boyutu, %80'nini eğitmek için kullanıcaz
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state= 42) # random_state böldüğümüz parçaların ne denli birbirine eşit olduğunu temsil ediyor. 
# X_test, y_test arka planda oluşan olayları temsil ediyor, X_train ev büyüklüğünü temsil ediyor y_train ise Fiyatı temsil ediyor

# --Modeli eğitme--
model = LinearRegression()
model.fit(X_train, y_train) # Modeli eğitme, X_train ve y_train ile

# --Modeli test etme--
# y_pred = model.predict(X_test)
# Test verisiyle tahmin etmeye olanak sağlıyor predict, tahminlerin hataları ölçülür ve hata ne kadar küçük çıkarsa tahmin o kadar iyidir. veriler tutarlı mı değil mi diye test ettikten sonra yorum satırı yaptık

# --Modelin ne kadar iyi çalıştığını ölçmek için--
# mse = mean_squared_error(y_test, y_pred) # Modelin ne kadar iyi çalıştığını ölç

# rmse = np.sqrt(mse) 
# Ev büyüklüğü ile fiyat arasındaki uyum sağlanamadığı için karekök fonksiyonuyla sayının değerinin daha anlamlı hale gelmesini sağladı(Fakat değer yine büyük çıkıyor çünkü ev büyüküğü ile fiyat arasındaki fark uçurum), veriler tutarlı mı değil mi diye test ettikten sonra yorum satırı yaptık

# print(f'Ortalama Kare Hatası (MSE): {mse}') # MSE (Mean Squared Error) modelin ne kadar hatası olduğunu yazdırır. veriler tutarlı mı değil mi diye test ettikten sonra yorum satırı yaptık

ev_buyuklugu = float(input("Lütfen evin büyüklüğünü(m²) girin: "))

tahmini_fiyat = model.predict([[ev_buyuklugu]])
print(f'Ev büyüklüğüne göre tahmini fiyat: {tahmini_fiyat[0]:.2f} TL') # Son 0'dan sonra 2 veriyi yazdır diyoruz = {tahmini_fiyat[0]:.2f}