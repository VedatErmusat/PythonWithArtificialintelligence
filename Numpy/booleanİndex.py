import numpy as np
dizi = np.array([10,20,30,40,50,65,75,95,12,24,7,35])

# boolean_mask = dizi > 50
# print(boolean_mask) #True False False False False False False False False False False False

# secilmis = dizi[boolean_mask]
# print("50'den büyük olan elemanlar: ",secilmis)

boolean_mask = (dizi>30) & (dizi<80)
print("30 ile 80 arasındaki elemanlar: ", dizi[boolean_mask])

