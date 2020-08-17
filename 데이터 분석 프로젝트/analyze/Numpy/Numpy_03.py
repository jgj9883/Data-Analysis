import numpy as np

# Numpy 원소 오름차순 정렬
array = np.array([5,9,10,3,1])
array.sort()
print(array)

# 내림차순
print(array[::-1])

# 각 열을 기준으로 정렬
array = np.array([[5,9,10,3,1],[8,3,4,2,5]])
print(array)
array.sort(axis=0)
print(array)
