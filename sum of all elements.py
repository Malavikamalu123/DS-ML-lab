import numpy as np
x=np.array([[1,0],[0,1]])
print("array")
print(x)
print("\nsum of all elements")
print(np.sum(x))
print("\nsum of each column")
print(np.sum(x,axis=0))
print("\nsum of each row")
print(np.sum(x,axis=1))