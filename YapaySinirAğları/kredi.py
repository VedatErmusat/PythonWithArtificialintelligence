import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from sklearn.preprocessing import StandardScaler # Standart sapma yapabilmek için

# Giriş verileri (Yaş ve gelir)
X = np.array([[25,2000],[30,4000],[45,10000],[50,3000]])
y = np.array([[0],[1],[1],[0]])

# Basit model
model = Sequential()
model.add(Dense(6, input_dim = 2, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

# Modeli derleme
optimizer = Adam(learning_rate = 0.005) # öğrenme hızını düşürdük
model.compile(loss = 'binary_crossentropy', optimizer = optimizer, metrics = ['accuracy'])

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modeli eğitme 
model.fit(X_scaled, y, epochs = 200, verbose = 1)

tahminleme = model.predict(X_scaled)
print('Tahminler: \n', tahminleme)


while True:
    user_input_1 = float(input('Yaşınızı giriniz: '))
    user_input_2 = float(input('Maaşınızı giriniz: '))
    #  Kullanıcıdan alınan verileri modele uygun hale getirme
    user_data = np.array([[user_input_1,user_input_2]])
    # Kullanıcıdan alınan verileri ölçeklendir
    user_scaled = scaler.transform(user_data)
    # Tahmin oluştur
    prediction = model.predict(user_scaled)
    # Sonucu yazdırma
    print(f"Tahmin sonucu: {prediction[0][0]:.4f}")
