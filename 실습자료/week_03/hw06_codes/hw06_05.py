import numpy as np
from matplotlib import pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

x = np.arange(-2, 2, 0.01)
print(x)
y = sigmoid(x)
print(y)

plt.plot(x, y, 'b')
plt.title('Sigmoid')
plt.grid()
plt.show()