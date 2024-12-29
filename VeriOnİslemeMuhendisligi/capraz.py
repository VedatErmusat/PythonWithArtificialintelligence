import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, accuracy_score

# Veriyi yükle
df = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\VeriOnİslemeMuhendisligi\\veri_on_isleme_ve_ozellik_muhendisligi.xlsx')
# Eksik verileri doldur
df.fillna(df['Gelir'].mean(), inplace=True)
# Cinsiyet ve Meslek sütunlarını sayısal hale getir
le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
df['Meslek'] = le.fit_transform(df['Meslek'])
# Girdi ve çıktı verilerini ayıralım
X = df[['Yaş', 'Meslek', 'Cinsiyet']]  # Girdiler
y = df['Gelir']  # Çıktı (Tahmin edilecek)
# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Ölçeklendirme
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#modeli oluştur ve capraz olarak değerlendir cv=5

linear_model = LinearRegression()
cv_scores = cross_val_score(linear_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
cv_rmse_scroes = (-cv_scores) ** 0.5
print(f'Linear Reg 5 Katmanlı Cross Val Puanı :{cv_rmse_scroes.mean():.2f}')

#random forest madeli ile capraz doğrulama performansını ölçelim

def forestmode():
    rf_model = RandomForestRegressor(n_estimators=100 , random_state=1)
    cv_scroes_rf = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error' )
    cv_rmse_scroes_rf = (-cv_scroes_rf) ** 0.5
    print(f'Random Forest 5 Katmanlı Cross Val Puanı :{cv_rmse_scroes_rf.mean():.2f}')

