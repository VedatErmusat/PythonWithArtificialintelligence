import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot  as plt
import seaborn as sns


df = pd.read_csv('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\KalpKriziRiskiAnalizi\\heart.csv')

# print(df.describe())
#histogram analizi
df.hist(figsize=(18,12) , bins=20 , edgecolor = 'black')
plt.suptitle('Veri Dağılımı')
# plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=df , x='Age' , y='Cholesterol' , hue='HeartDisease')
plt.title('Yaş ve Kolesterol Arasında İlişki')
# plt.show()


# Korelasyon matrisini çizebilmek için tüm verileri sayısal değere çevirme
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['ChestPainType'] = label_encoder.fit_transform(df['ChestPainType'])
df['RestingECG'] = label_encoder.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = label_encoder.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = label_encoder.fit_transform(df['ST_Slope'])

# Korelasyon matrisini çizme
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Korelasyon Isı Haritası')
# plt.show()


plt.figure(figsize=(6,6))
sns.countplot(x='HeartDisease' , data=df)
plt.title('Kalp Hastalığına Yakalanma Oranları')
#plt.show()

