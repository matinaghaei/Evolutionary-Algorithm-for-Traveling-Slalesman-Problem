import copy

a = [[1], 2]
b = a[0:2]

a[0][0] = 0
a[1] = 3

print(b)

print(a)

