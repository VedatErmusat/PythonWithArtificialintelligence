import numpy as np

dizi1 = np.array([1,2,3,5])
dizi2 = np.array([3,4,12,5])

# toplam = dizi1 + dizi2
# cikarma = dizi1 - dizi2
# carpma = dizi1 * dizi2
# bolme = dizi1 / dizi2
# print("Toplam: ", toplam)
# print("Fark: ", cikarma)
# print("Çarpım: ", carpma)
# print("Bölüm: ", bolme)

# TOPLAMA FONKSİYONU

toplam = np.sum(dizi1)
print("Toplam: ", toplam)  # 11

# ÇARPIM FONKSİYONU
carpim = np.prod(dizi2) 
print("Çarpım: ", carpim)  # 360

# FARK FONKSİYONU
fark = np.subtract(dizi1, dizi2)
print("Fark: ", fark)  # [-2  -2  1

# BOLME FONKSİYONU
bolme = np.divide(dizi1, dizi2)
print("Bölüm: ", bolme)
# [-0.        -0.5       0.08333333]

# KARE ALMA FONKSİYONU

kareal = np.sqrt(dizi1)
print("Kareleri: ", kareal)  

# ARİTMETİK ORTALAMA ALMA
ortalama = np.mean(dizi1)
print("Ortalama: ",ortalama)  # 2.5

# VARYANS ALMA
varyans = np.var(dizi1)
print("Varyans: ",varyans)  # 2.916666666666667
# Varyans nedir?
# Varyans, bir veri kümesindeki veri noktalarının ortalama değerinden sapmalarının  karesinin ortalamasıdır. Varyans, veri dağılımının homojenlik derecesini gösterir. Varyansın artması, veri dağılımının homojenlik derecesinin artması demektir.

# MEDYAN ALMA
medyan = np.median(dizi1)
print("Medyan: ",medyan)  # 2.5

# STANDART SAPMA
standartsapma = np.std(dizi1)
print("Standart Sapma: ",standartsapma)  # 1.581138

# ÜS ALMA
us = np.power(dizi1, 2)
print("Üs: ",us)  # [ 1  4  9 25]

