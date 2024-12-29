import numpy as np

# 1 ile 10 arasında rastgele 5 sayı üretme
rastgele_sayi = np.random.randint(1, 10, size=5)
print("1 ile 10 arasında 5 tane sayı dizisi: ",rastgele_sayi)  

print("-"*50)

normal_rakam = np.random.normal(0,1,5)
print("0 ile 1 arasında random sayı dizisi: ",normal_rakam)   # Bu normal dağılımı üretir.

print("-"*50)

rand_dizi = np.random.rand(3,3)*10
rand_dizi = rand_dizi.astype(int)
print("3'e 3'lük random sayılar dizisi: ",rand_dizi) 

