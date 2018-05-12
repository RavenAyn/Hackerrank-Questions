def diagonalDifference(a):
    arr_sum_1 = []
    arr_sum_2 = []
    for i in range(n):
        arr_sum_1.append(a[i][i])
    for i in range(n):
        arr_sum_2.append(a[i][(n-1)-i])
    diag_1 = sum(arr_sum_1)
    diag_2 = sum(arr_sum_2) 
    return abs(diag_2 - diag_1)

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(a)
print(result)
