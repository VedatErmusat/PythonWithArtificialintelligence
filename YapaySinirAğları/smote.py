import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore

# Veri setini yükleme
df = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\YapaySinirAğları\\kredi_onay_verisi_1000.xlsx')
X = df[['Yaş','Gelir']].values
y = df[['Kredi Onayı']].values

# Veriyi test ve eğitim olarak bölme
X_train , X_Test , y_train, y_test = train_test_split(X,y, test_size=0.2 , random_state=42)

# Smote ile veri dengesini sağlama
smote = SMOTE(random_state=42)
X_train_smote , y_train_smote = smote.fit_resample(X_train,y_train)

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train_smote_scaled = scaler.fit_transform(X_train_smote)
X_test_scaled = scaler.transform(X_Test)

# Modeli oluşturma 
model = RandomForestClassifier(random_state = 42)
model.fit(X_train_smote_scaled, y_train_smote)

# Tahminleme
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)



# Modelin Doğruluk Oranını Artırmak İçin Yaptığımız İşlemler

# Yapay sinir ağları 
nn_model = Sequential()
nn_model.add(Dense(3, input_dim=2 , activation='relu'))
nn_model.add(Dense(1,  activation='sigmoid'))

# Modeli derle
optimizer = Adam(learning_rate = 0.001)
nn_model.compile(loss='binary_crossentropy', optimizer = optimizer , metrics=['accuracy'])

# Modeli eğitelim
nn_model.fit(X_train_smote_scaled, y_train_smote , epochs=100 , batch_size=32 , verbose=1)

# Yapay sinir ağı tahminleme ve doğruluk oranı ölçümü
y_pred_nn = (nn_model.predict(X_test_scaled) > 0.5).astype('int32')
nn_accuracy = accuracy_score(y_test , y_pred_nn)
print(f'Test Doğruluk Oranı :{accuracy * 100:.2f}%')
print(f'Yapay Sinir Ağı Test Doğruluk Oranı :{nn_accuracy* 100:.2f}%')