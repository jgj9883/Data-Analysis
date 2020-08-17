import numpy as np

# Numpy 배열에 곱하기
array1 = np.random.randint(1,10,size=4).reshape(2, 2)
#print(array1)

result_array = array1 * 3
#print(result_array)

# Numpy의 연산과 함수 (1)
array2 = np.arange(4).reshape(2,2) # (2 * 2) 배열
array3 = np.arange(2) # (1 * 2) 배열
print(array2)
print(array3)

array4 = array2 + array3
print(array4)

# Numpy의 연산과 함수 (2)
array1 = np.arange(0,8).reshape(2, 4)
array2 = np.arange(0,8).reshape(2, 4)
array3 = np.concatenate([array1,array2], axis= 0)
array4 = np.arange(0, 4).reshape(4, 1 ) # (4x1)

print(array3 + array4)






