import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from sklearn.preprocessing import StandardScaler # Standart sapma yapabilmek için
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""
data = {
    'Yaş': [25, 30, 45, 50, 28, 35, 40, 60],
    'Gelir': [2000, 4000, 10000, 3000, 3500, 5000, 8000, 12000],
    'Medeni Durum': ['Bekar', 'Evli', 'Evli', 'Bekar', 'Bekar', 'Evli', 'Evli', 'Bekar'],
    'Meslek': ['Mühendis', 'Doktor', 'Öğretmen', 'Avukat', 'Mühendis', 'Doktor', 'Avukat', 'Öğretmen'],
    'Eğitim Durumu': ['Lisans', 'Lisans', 'Yüksek Lisans', 'Doktora', 'Lisans', 'Lisans', 'Yüksek Lisans', 'Doktora'],
    'Kredi Onayı': [0, 1, 1, 0, 1, 1, 1, 0]
}
"""
data = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\YapaySinirAğları\\genisletilmisveri.xlsx')

# Pandas veri çerçevesi
df = pd.DataFrame(data)

# Sahte değişkenler oluştur
df = pd.get_dummies(df , columns=['Medeni Durum', 'Meslek','Eğitim Durumu'] , drop_first=True)

# Kesme işlemi
X = df.drop('Kredi Onayı', axis=1).values
#Çıkış Verisis 
y = df['Kredi Onayı'].values

# Veriyi ikiye böl, test ve eğitim olarak
X_train , X_Test , y_train, y_test = train_test_split(X,y, test_size=0.4 , random_state=42)

# Modeli oluştur
model = Sequential()
model.add(Dense(3 , input_dim=X.shape[1] , activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Modeli derleme
optimizer = Adam(learning_rate=0.002)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Veriyi ölçeklendirelim
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_Test_scaled = scaler.transform(X_Test)

# Modeli eğitme
model.fit(X_train_scaled, y_train, epochs=350, verbose=1)

# Tahminleme
y_pred = model.predict(X_Test_scaled)
y_pred = (y_pred > 0.5).astype(int) 

# Doğruluk oranını ölç
accuracy = accuracy_score(y_test, y_pred)
print(f'Test Doğruluk Oranı : {accuracy * 100:.2f}%')

# Kullanıcıdan veri alma

while True:
    user_input_1 = float(input('Yaşınızı Giriniz : '))
    user_input_2 = float(input('Maaşınızı Giriniz : '))
    user_input_3 = input('Medeni Durumunuzu Giriniz(Bekar, Evli):')
    user_input_4 = input('Mesleğiniz (Mühendis, Doktor, Öğretmen, Avukat):')
    user_input_5 = input('Eğitim Durumunuzu Giriniz (Lisans, Yüksek Lisans, Doktora):')

    user_data = pd.DataFrame({
        'Yaş': [user_input_1],
        'Gelir': [user_input_2],
        'Medeni Durum_' + user_input_3:[1],
        'Meslek_' + user_input_4:[1],
        'Eğitim Durumu_' + user_input_5:[1]
    })

    user_Data = user_data.reindex(columns=df.drop('Kredi Onayı', axis=1).columns , fill_value=0)

    # Veriyi ölçeklendirme
    user_data_scaled = scaler.transform(user_Data)
    # Tahminleme
    prediction = model.predict(user_data_scaled)
    print(f'Tahmin Sonucu :{prediction[0][0]:.4f}')