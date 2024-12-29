import numpy as np 

# dizi1 = np.array([1,2,3])
# dizi2 = np.array([4,5,6])

# birlesik_dizi = np.concatenate((dizi1,dizi2))
# print(birlesik_dizi)  # [1 2 3 4 5 6 ]

dizi1 = np.array([[1,2,3],[4,5,6]])
dizi2 = np.array([[7,8,9],[10,11,12]])

birlesik_dizi = np.hstack((dizi1,dizi2))
print(birlesik_dizi)    
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

birlesik_dizi1 = np.vstack((dizi1,dizi2))
print(birlesik_dizi1)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Dizi bolme
dizi = np.array([1,2,3,4,5,6])
bolunmus_dizi = np.split(dizi,3)
print(bolunmus_dizi)