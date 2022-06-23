m = int(input("请输入矩阵行数"))
n = int(input("请输入矩阵列数"))
matrix = [[0] * n] * m

for i in range(m):
    arr = input(f"请输入{n}位第{i+1}行矩阵的数字")
    arr = [int(i) for i in arr.split()]
    matrix[i] = arr

# 记录第i行第j列的零元素为true
row, column = [False] * m, [False] * n
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            row[i] = True
            column[j] = True

# 将第i行和第j列的元素变成0
for i in range(m):
    for j in range(n):
        if row[i] or column[j]:
            matrix[i][j] = 0
print(matrix)
