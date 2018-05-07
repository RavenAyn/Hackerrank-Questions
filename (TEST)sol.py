def solve(n, s, d, m):
    checker = 0 
    for i in range(n):
        seg = []
        j=i-1
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
