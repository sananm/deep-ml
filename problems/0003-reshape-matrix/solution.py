import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    if len(a)*len(a[0]) != new_shape[0]*new_shape[1]:
        return []

    flat = np.ravel(a).tolist()
    reshaped_matrix = []

    for i in range(0,len(flat),new_shape[1]):
        reshaped_matrix.append(flat[i:i+new_shape[1]])
    
    return reshaped_matrix
