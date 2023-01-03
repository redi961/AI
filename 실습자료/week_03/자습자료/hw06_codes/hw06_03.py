import numpy as np
import random

a = np.ones((4, 4))
b = np.eye(4, 4)
# c = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
c = [list(np.random.randint(0, 10, size=(4))) for _ in range(4)]

print(a)
print(b)
print(c)

sum_ = a + b
sub = a - c
mean_sum_ = np.mean(sum_)

print(sum_)
print(sub)
print(mean_sum_)

