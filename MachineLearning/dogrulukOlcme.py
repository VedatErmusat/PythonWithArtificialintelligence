import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\MachineLearning\\karar_agaci_veri_100.xlsx")

X = df[['Yas','Kan_Basinci','Kolesterol']] # Girdi verileri
y = df['Hastalik'] # Çıktı verileri


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Modeli Eğitme
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Modeli Test etme
y_pred = classifier.predict(X_test)


cm = confusion_matrix(y_pred, y_test)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title('Matrix - Karar Ağacı')
plt.show()

