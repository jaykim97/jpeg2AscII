n=4
m=5
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = [i,j]
for row in a:
    print(' '.join([str(elem) for elem in row]))