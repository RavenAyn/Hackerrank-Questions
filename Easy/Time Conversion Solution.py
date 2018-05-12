def timeConversion(s):
    if s[-2:] == "AM" and s[0:2] == "12":
        h24 = "00"+ s[2:-2]
    elif s[-2:] == "PM" and s[0:2] != "12":
        h24 = str(int(s[0:2])+12)+ s[2:-2]

    else:
        h24 = s[0:-2]
    return h24
    
    
s = input()
result = timeConversion(s)
print(result)
