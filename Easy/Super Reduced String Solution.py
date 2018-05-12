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
