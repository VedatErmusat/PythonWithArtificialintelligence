# Kümülatif nedir, Kümülatif, bir dizi olayın veya olayların birbiri ardına gerçekleşmesi ve bu olayların toplam etkisinin veya sonucu olarak ortaya çıkan bir kavramdır.
import numpy as np

dizi = np.array([1,2,3,4,65])
maks = np.max(dizi)
print("Dizideki en yüksek değere sahip veri: ",maks) # 65
print("-"*41)
min = np.min(dizi)
print("Dizideki en düşük değere sahip veri: ",min) # 1
print("-"*41)
toplam = sum(dizi)
print("Dizideki tüm değerlerin toplamı: ",toplam) # 75
print("-"*41)
kume_toplam = np.cumsum(dizi)
print("Dizideki her bir elemanın kümülatif toplamı: ",kume_toplam)
