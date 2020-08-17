# 두번째 또는 세번째 많은 친구 수
array_friends = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3, 3, 50, 25, 25, 11, 2, 3, 3, 2]

sorted_values = sorted(array_friends)
second_smallest_value = sorted_values[1] # 두번째로 작은 갑
second_largest_value = sorted_values[-2] # 두번째로 큰 값, 파이선에서 -1은 가장 뒤

print(sorted_values)
print("두번째로 작은 값", second_smallest_value)
print("두번째로 큰 값", second_largest_value)