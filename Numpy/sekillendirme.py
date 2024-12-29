import numpy as np
dizi = np.array([1,2,3,4,5,6])

# yeni_dizi = dizi.reshape((2,3))
# print(yeni_dizi) # 2 satır 3 sütun

matris = np.array([[1,2],[3,4],[5,6]])
tek_boyut = matris.reshape(-1)
print(tek_boyut)  # [1 2 3 4 5]

print("-"*30)

dizi2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
yeni_dizi = dizi2.reshape(3,-1) # (3,4)
print(yeni_dizi) 

