import pandas as pd
import numpy as np

# Excel dosyasını oku
df = pd.read_excel("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\Pandas\\teknolojik_urunler1.xlsx")

# Rastgele tarih damgaları oluşturma
df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'),size= len(df)))

# Çıktıyı al
print(df)

df.to_excel('teknolojik_urunler_zamanli.xlsx', index=False)
print('Veri dosyaya aktarıldı')