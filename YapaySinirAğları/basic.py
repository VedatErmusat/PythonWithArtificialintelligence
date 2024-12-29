import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

# Giriş verileri(XOR problemi olarak al)
X = np.array([[0,0],[0,1],[1,0],[1,1]]) # İkisi de 0 veya 1 ise çıktı 0 olur ama birbirinden farklıysa çıktı 1 olur
y = np.array([[0],[1],[1],[0]])

# Basit model
model = Sequential()
model.add(Dense(3, input_dim=2, activation='relu')) # Dense(4) demek 4 farklı kaynaktan problemin cevabını aramak. input_dim=2 ise her iki değer için 4 defa arama yapmasını istiyoruz. activation='relu' ise soruların cevaplarını doğru ve yanlış olarak filtreler.
model.add(Dense(1,activation='sigmoid')) # Sigmoid çıktımı 0 ile 1 arasında oluşturur.

# Modeli Derleme
model.compile(loss='binary_crossentropy',optimizer='adam', metrics = ['accuracy']) # loss='binary_crossentropy' hataları kendi içinde küçük parçalara böl ben üzerinde işlem yapıcam demek. optimizer='adam' bu ise loss='binary_crossentropy' 'deki parçaları düzeltmek. metrics = ['accuracy'] verilerin doğruluk oranını yüzdesel olarak gösterir.

#Modeli Eğitme
model.fit(X,y,epochs=200,verbose=1) # epochs=200, model.compile işlemi kaç defa çalışmalı demek. verbose=1 bu ise her çıktıda bir cevap versin diye

tahmin = model.predict(X)
print('Tahminler:\n',tahmin) # Tahmin edilen değerleri ekrana bastırır.