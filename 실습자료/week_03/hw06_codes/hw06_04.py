import numpy as np

m = np.random.randint(0, 10, size=(4, 5))

print(m)

A, _ = np.where(m == 1)
print(len(A))

rows, cols = m.shape

cnt = 0
for c in range(cols):
    for r in range(rows):
        print('r: {}, c: {}'.format(r, c))
        if m[r, c] == 1:
            cnt += 1

print('Num ones : {}'.format(cnt))


# l[1][2]
l = [[1, 2, 3], [4, 5, 6]]
print(l[1][1])



print('Done')