import numpy as np


# numpy 마스킹 연산
array1 = np.arange(16).reshape(4,4)
print(array1)
array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)


# numpy의 집계 함수

array1 = np.arange(16).reshape(4,4)
print("최대값 : ", np.max(array1), axis=0 ) # axis=0이면 열에 따라 계산 ,=1 이면 행에 따라 계산
print("최솟값 : ", np.min(array1))
print("평균 : ", np.average(array1))
print("합 : ", np.sum(array1))



