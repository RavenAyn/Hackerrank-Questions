# Problem Description

Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

- Its length is at least .
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
```
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
```
##### Input Format

The first line contains an integer _n_ denoting the length of the string.

The second line contains a string consisting of _n_ characters, the password typed by Louise. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

# Solution

```python
n = int(input().strip())
password = input().strip()
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
check = []
for i in range(10):
    if numbers[i] in password:
        check.append(1)
        break
for i in range(26):
    if lower_case[i] in password:
        check.append(1)
        break 
for i in range(26):
    if upper_case[i] in password:
        check.append(1)
        break
for i in range(len(special_characters)):
    if special_characters[i] in password:
        check.append(1)
        break 
missing_check = length = 4 - sum(check)
if len(password) < 6:
    missing_let = 6 - len(password)
    if missing_let > missing_check:
        length = missing_let
    elif missing_let < missing_check:
        length = missing_check
    else:
        length = missing_check
        
print(length)
```
