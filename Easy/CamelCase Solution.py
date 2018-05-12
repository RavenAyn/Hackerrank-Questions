s = input()
lower = s.lower()
j = 0
for i in range(len(s)):
    while lower[i] in s:
        s = s.replace(lower[i], "")
print(len(s)+1)
