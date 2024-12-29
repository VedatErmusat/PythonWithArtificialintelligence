import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Veriyi hazırlama: Yaş, kan basıncı, kolestrol ve hastalık durumu
# data = {
#     'Yas': [25,50,45,30,60],
#     'Kan_Basinci':[120,140,130,110,150],
#     'Kolesterol':[180,240,200,160,220],
#     'Hastalik_Durumu': [0,1,1,0,1] # 0 hayır , 1 evet
# }

# df = pd.DataFrame(data)

df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\MachineLearning\\karar_agaci_veri_100.xlsx")

X = df[['Yas','Kan_Basinci','Kolesterol']] # Girdi verileri
y = df['Hastalik'] # Çıktı verileri


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Modeli Eğitme
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Modeli Test etme
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# print(f"Model doğruluk oranı: {accuracy}")

# Kullanıcıdan veri alarak tahmin yapma
yas = int(input("Yaşınızı girin: "))
kan_basinci = int(input("Kan basıncınızı girin: "))
kolesterol = int(input("Kolesterol seviyenizi girin: "))

# Tahmin oluştur
kullanici_verisi = pd.DataFrame([[yas, kan_basinci, kolesterol]], columns=['Yas', 'Kan_Basinci', 'Kolesterol'])
tahmin = classifier.predict(kullanici_verisi) # tahmin = classifier.predict([[yas, kan_basinci, kolesterol]])
sonuc = "Hastalık var" if tahmin[0]==1 else "Hastalık yok"
print(f"Tahmin: {sonuc}")
