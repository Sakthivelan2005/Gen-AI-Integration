import numpy as np
a = np.arange(16)
b = a.reshape(2,8) # 2D array
c = a.reshape(2,2,2,2) # 3D array (2 splits, 2 rows and 5 columns)
print(a[-1])

#Aggrigate functions
print("Aggrigate Functions: ")
print(b)
print("\nMax: ",b[-1:].max())
print("\nmin: ", b[-1:].min())
print("\nAvg: ", b[-1:].mean())
print("\nCount: ", b[-1:].sizej)
