import numpy as np
from matplotlib import pyplot as plt

f1 = open('C:\\Users\\user\\Desktop\\AIP\\hw06\\vError.txt', 'r')
v1 = [eval(line.rstrip()) for line in f1]
f1.close()

f2 = open('C:\\Users\\user\\Desktop\\AIP\\hw06\\tError.txt', 'r')
v2 = [eval(line.rstrip()) for line in f2]
f2.close()

print(v1)
print(v2)

plt.plot(v1)
plt.plot(v2)
plt.xlabel('Model Complexity')
plt.ylabel('Error Rate')
plt.grid()
plt.show()