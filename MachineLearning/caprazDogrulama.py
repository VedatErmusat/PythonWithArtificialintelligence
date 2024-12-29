import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\MachineLearning\\karar_agaci_veri_100.xlsx")

X = df[['Yas','Kan_Basinci','Kolesterol']] # Girdi verileri
y = df['Hastalik'] # Çıktı verileri


# Modeli Eğitme
classifier = DecisionTreeClassifier(max_depth=3, min_samples_split=4, min_samples_leaf=2) # Derinlik, sorulan soru(Ayrıldığı dallar) ve yaprak düğümü
classifier.fit(X,y)
#Modeli Test etme
# cross_val_scores = cross_val_score(classifier, X, y, cv=5)
# print(f"Model doğruluk oranları: {cross_val_scores}")
# print(f"Model doğruluk oranları ortalaması : {cross_val_scores.mean():.2f}") 

# Kullanıcıdan veri alma
print("Lütfen tahmin için aşağıdaki bilgileri giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
kan_basinci = int(input("Kan basıncınızı giriniz: "))
kolesterol = int(input("Kolesterol seviyenizi giriniz: "))

# Kullanıcıdan alınan veriyi modelin anlayacağı hale getir
yeni_veri = pd.DataFrame([[yas,kan_basinci,kolesterol]],columns=['Yas','Kan_Basinci','Kolesterol'])
tahmin = classifier.predict(yeni_veri)

if tahmin[0] == 1:
    print("Tahmin: Hastalık Var!")
else:
    print("Tahmin: Hastalık Yok!")