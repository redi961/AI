import numpy as np

a = np.ones((6, 4))*2
b = np.eye(6, 4)*2 + 1

mul1 = a * b
# mul2 = np.dot(a, b)

print(np.dot(a.transpose(), b))
print(np.dot(a, b.transpose()))

# print(a)
# print(b)