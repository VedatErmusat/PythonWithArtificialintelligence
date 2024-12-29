import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

#veriyi yükle
df = pd.read_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\VeriOnİslemeMuhendisligi\\veri_on_isleme_ve_ozellik_muhendisligi.xlsx')
#eksik gelir verilerini ortalama ile dolduralım
df.fillna(df['Gelir'].mean() , inplace=True)
# print(df)
le =LabelEncoder() # Kategorize verileri 0 ve 1 gibi sayısal değerlerle değiştiren sınıf(kadın-erkek 0-1)
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
# print(df)
scaler = StandardScaler() # Veri düzenleme-değiştirme için kullanılan sınıf(Hammadde ve üretim kategorileri arasında aşırı fark varsa bunları kullanabiliriz)
# df[['Yaş', 'Gelir']] = scaler.fit_transform(df[['Yaş', 'Gelir']])
# print(df)

df.drop('ID', axis=1, inplace=True) # ID sütununu siler
df['Gelir_Grubu'] = pd.cut(df['Gelir'] , bins=[0,3000,5000,7000], labels=['Düşük','Orta','Yüksek'])
df.to_excel('C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\VeriOnİslemeMuhendisligi\\Kategorik_Gelir.xlsx')


#görselleştirme

# plt.figure(figsize=(10,6))
# plt.hist(df['Meslek'] , bins=10 , color='skyblue' , edgecolor='black')
# plt.title('Yaş Dağılımı')
# plt.xlabel('Yaş')
# plt.ylabel('Frekans')
# plt.show()


# plt.figure(figsize=(10,6))
# sns.countplot(x='Gelir_Grubu', hue='Yaş', data=df)
# plt.title('Gelir Grubu ve Cinsiyet İlişkisi')
# plt.xlabel('Gelir Grubu')
# plt.ylabel('Kişi Sayısı')
# plt.show()


