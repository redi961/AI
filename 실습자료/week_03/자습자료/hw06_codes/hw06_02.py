import numpy as np

data = [
    [1, 2104, 5, 1, 45, 460],
    [1, 1416, 3, 2, 40, 232],
    [1, 1544, 3, 2, 30, 315],
    [1, 852, 2, 1, 36, 178]
]

# print(data)

X = np.array(data)

# assert 여기가 True 이면 아무 일 없이 지나감
# assert 여기가 False 이면 ERROR 이고 프로그램 종료
print(X.shape) # 모양이 Tuple로 나옴!
assert X.shape == (4, 6), "모양이 잘못됨 (4, 6)만 됨!!"

print(X)

# X[ROW, COL]

P = X[:, 1:5]
print(P)
print(P.shape)

mean_value_row = np.mean(X, axis=0)
print(mean_value_row)

mean_value_col = np.mean(X, axis=1)
print(mean_value_col)