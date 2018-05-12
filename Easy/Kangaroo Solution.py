def kangaroo(x1, v1, x2, v2):
    a= "undefined"
    if x1 > x2 and v1 >= v2:
        a= "NO"
    elif x1 > x2 and v1 < v2:
        j = 0
        while x1 > x2:
            x1 = x1 + v1
            x2 = x2 + v2
            j +=1
        if x1 == x2:
            a= "YES"  
        else:
            "NO"
    elif x2 > x1 and v2 >= v1:
        a="NO"
    elif x2 > x1 and v2 < v1:
        j = 0
        while x2 > x1:
            x1 = x1 + v1
            x2 = x2 + v2
            j +=1
        if x1 == x2:
            a= "YES"
        else:
            a="NO"
    elif x1 == x2:
            a= "YES"
    else: 
        a = "error"

    return a
            

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
