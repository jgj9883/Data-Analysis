import collections

# Q. 동일한 친구수를 가진 사람들을 보여주며 보통 몇명의 친구들을 가지고 있는가 ??

array_friends = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3, 3, 50, 25, 25, 11, 2, 3, 3]
friends_counts = collections.Counter(array_friends)
print("friends : ", friends_counts)
