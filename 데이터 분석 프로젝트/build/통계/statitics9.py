# 분산 데이터들 사이에 얼마나 차이가 큰가?
import math

array_friends = [100, 15, 10, 10, 9, 4, 3, 3, 2, 1]

def mean(x) :
    return sum(x)/len(x)
def dot(v,w) :
    return sum(v_i* w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v) :
    return dot(v,v)

def de_mean(x) : # 요소들과 평균의 차이
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)   # n으로 나누기보다 n-1로 나누어야 정확하게 보정됨

print("분산", variance(array_friends))


def standard_deviation(x) :
    return math.sqrt(variance(x))

print("표준편차", standard_deviation(array_friends))