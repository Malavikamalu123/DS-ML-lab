import numpy as np
import os
x=np.arange(16).reshape(4,4)
print("array")
print(x)
header='C1 C2 C3 C4'
np.savetxt('array.txt',x,fmt="%d",header=header)
print("\n after loading,content of the file:")
print(np.loadtxt('array.txt'))