# Problem Description

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#### Input Format

The first line contains a single integer, _n_ denoting the number of rows and columns in the matrix _a_. 
The next _n_ lines denote the matrix 's rows, with each line containing  space-separated integers describing the columns.

#### Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Solution
```python
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

```
