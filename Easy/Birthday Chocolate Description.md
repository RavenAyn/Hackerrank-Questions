## Problem Description:

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment mathches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, _s=[2, 2, 1, 3, 2]_ . She wants to find segments summing to Ron's birth day, _d=4_ , with a length equalling his birth month, _m = 2_ . In this case, there are two segments meeting her criteria: _[2, 2]_ and _[1, 3]_.
#### Input Format:

The first line contains an integer , the number of squares in the chocolate bar. 
The second line contains  space-separated integers , the numbers on the chocolate squares where . 
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.

#### Output Format

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

Sample Input 0

5
1 2 1 3 2
3 2

Sample Output 0

2


# Solution

```python
def solve(n, s, d, m):
    checker = 0 
    for i in range(n):
        seg = []
        j = i-1
        while len(seg) < m and j < n-1:
            j += 1
            seg.append(s[j])
        if sum(seg) == d:
            checker += 1
    return checker


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

```
