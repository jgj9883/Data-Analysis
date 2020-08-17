# 회원들의 친구 수의 평균 구하기 (보통 몇명의 친구를 가지고 있을까?)

from __future__ import division # 더 정확히 계산

array_friends = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3, 3, 50, 25, 25, 11, 2, 3, 3, 2]

def mean(x) :
    c= sum(x)/len(x)
    return c

avgOfFriends = mean(array_friends)
print(avgOfFriends)

