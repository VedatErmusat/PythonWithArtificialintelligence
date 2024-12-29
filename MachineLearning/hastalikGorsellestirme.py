import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\MachineLearning\\karar_agaci_veri_100.xlsx")

# Yaş ile hastalık arasındaki ilişkiyi görselleştirme
# plt.figure(figsize=(10,6))
# sns.histplot(data=df, x='Yas', hue='Hastalik', multiple='stack', kde=False) 
# plt.title("Yaş Dağılımı ve Hastalık Durumu")
# plt.xlabel("Yaş")
# plt.ylabel("Kişi Sayısı")
# plt.show()

# Kan Basıncı ile Hastalık arasındaki ilişki
# plt.figure(figsize=(10,6))
# sns.histplot(data=df, x='Kan_Basinci', hue='Hastalik', multiple='stack', kde=False) 
# plt.title("Kan Basıncı ve Hastalık Durumu")
# plt.xlabel("Kan Basıncı")
# plt.ylabel("Kişi Sayısı")
# plt.show()

# Kolesterol ile Hastalık arasındaki ilişki
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kolesterol', hue='Hastalik', multiple='stack', kde=True) 
plt.title("Kolesterol ve Hastalık Durumu")
plt.xlabel("Kolesterol")
plt.ylabel("Kişi Sayısı")
plt.show()