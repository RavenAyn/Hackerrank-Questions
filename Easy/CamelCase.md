# Problem Description
Alice wrote a sequence of words in CamelCase as a string of letters, _s_, having the following properties:

- It is a concatenation of one or more words consisting of English letters.
- All letters in the first word are lowercase.
- For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given _s_, print the number of words in _s_ on a new line.


# Solution
```python
s = input()
lower = s.lower()
j = 0
for i in range(len(s)):
    while lower[i] in s:
        s = s.replace(lower[i], "")
print(len(s)+1)
```
