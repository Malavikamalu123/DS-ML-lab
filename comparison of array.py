import numpy as np
x=np.array([3,5,1,2,3])
y=np.array([2,5,3,2,1])
print("array A")
print(x)
print("\n array B")
print(y)
print("\n A>B")
print(np.greater(x,y))
print("\n A>=B")
print(np.greater_equal(x,y))
print("A<B")
print(np.less(x,y))
print("\n A<=B")
print(np.less_equal(x,y))