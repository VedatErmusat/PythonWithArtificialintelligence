import numpy as np 

data = np.loadtxt("C:\\Users\\Vedat\\OneDrive\\Masaüstü\\vedat\\CODİNG\\AI_PYTHON\\Numpy\\File\\data.txt", delimiter=' ')
# print(data)

row_sums = np.sum(data, axis=1)
# print("Her satırın toplamı: ",row_sums)

# np.savetxt('output.txt', row_sums, fmt='%d') # Satır toplamları verilerini tam sayı halinde kaydeder.

output_data = np.column_stack((data, row_sums))
np.savetxt('output_with_sums.txt', output_data, fmt='%d', delimiter=' ')
print("Kayıt işlemi tamamlandı!")



