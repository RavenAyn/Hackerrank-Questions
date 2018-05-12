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
