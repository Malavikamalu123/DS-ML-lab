import numpy as np
def create_matrix(mc):
    print("\nEnter the array"+str(mc)+"Elements:")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("\nEnter the array" + str(mc) + "row column:")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("\nrow and column size not match with total elements!! retry")
        return create_matrix(mc)
    array_1 = array_1.reshape(row, column)
    print("\narray"+str(mc))
    print(array_1)
    print("\nrank : ")
    return array_1


print(np.linalg.matrix_rank(create_matrix(1)))
