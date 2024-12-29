import numpy as np

dizi = np.array([10,20,30,40,50])
# eleman = dizi[1]
# print(eleman) # 20
dilim = dizi[2:5]
print(dilim) # [30 40 50]

matris = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(matris[2,2]) # 9
print(matris[-1,-3]) # 7

alt_matris = matris[0:2,1:3]
print(alt_matris) # [[2 3]
# [5 6]]


