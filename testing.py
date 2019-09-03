x=10
y=5
arr = [[0 for a in range(x)] for b in range(y)]
for i in range(x):
    for j in range(y):
        arr[i:j]= [i,2j]


for i in range(x):
    for j in range(y):
        print(arr[i][j])