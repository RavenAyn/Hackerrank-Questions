# Problem Description
Steve has a string of lowercase characters in range `ascii[‘a’..’z’]`. He wants to reduce the string to its shortest length by doing a series of operations in which he selects a pair of adjacent lowercase letters that match, and then he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String

Steve performs the following sequence of operations to get the final string:
```
aaabccddd → abccddd → abddd → abd
```
#### Input Format

A single string,_s_ .

#### Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0
```
aaabccddd
```
Sample Output 0
```
abd
```

Sample Input 1
```
aa
```
Sample Output 1
```
Empty String
```
Sample Input 2
```
baab
```
Sample Output 2
```
Empty String
```
Explanation 2
```
baab → bb → Empty String
```

# Solution
```python
def super_reduced_string(s):
    doubles_present = 1
    while doubles_present == 1:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                sremove = s[i]+s[i+1]
                s = s.replace(sremove ,"00")
        s = s.replace("0","")
        doubles_present = 0
        for i in range (len(s)-1):
            if s[i] == s[i+1]:
                doubles_present = 1
    if len(s) == 0:
        s = "Empty String"
    return(s) 
s = input().strip()
result = super_reduced_string(s)
print(result)
```
