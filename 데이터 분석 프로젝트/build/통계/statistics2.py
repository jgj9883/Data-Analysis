import  collections
import  matplotlib.pyplot as plt

array_friends = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3, 3, 50, 25, 25, 11, 2, 3, 3]
friends_counts = collections.Counter(array_friends)
print("friends : ", friends_counts)


#가시화
xs = range(101)
ys = [friends_counts[x] for x in xs]

plt.bar(xs, ys)
plt.title("Practice")
plt.axis([0, 101, 0, 25])
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()