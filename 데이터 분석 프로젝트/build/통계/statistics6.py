# 친구 수의 중앙값은(median)?

from __future__ import division # 더 정확히 계산

array_friends = [1200, 15, 10, 10, 9, 4, 3, 3, 2, 1]

def mean(x) :
    c= sum(x)/len(x)
    return c

avgOfFriends = mean(array_friends)
print("평균값 : ",avgOfFriends)

def median(v) :
    c= len(v)
    sorted_v = sorted(v)
    midpoint = c // 2 # //로 나누면 int 형, /로 나누면 float

    if c % 2 ==1:
        return sorted_v(midpoint) # 리스트가 홀 수면 가운데 값
    else :
        lo = midpoint -1 # 짝수면 가운데의 2개의 값의 평균
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) /2


midianOfFriends = median(array_friends)
print("중앙값 : ", midianOfFriends)

