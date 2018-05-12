# Problem Description

You are choreograhing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

- The first kangaroo starts at location _x[1]_ and moves at a rate of _v[1]_ meters per jump.
- The second kangaroo starts at location _x[2]_ and moves at a rate of _v[2]_ meters per jump.
You have to figure out a way to get both kangaroos at the same location as part of the show.

Complete the function kangaroo which takes starting location and speed of both kangaroos as input, and return _Yes_ or _No_ appropriately. Can you determine if the kangaroos will ever land at the same location at the same time? The two kangaroos must land at the same location after making the same number of jumps.

#### Input Format

A single line of four space-separated integers denoting the respective values of _x[1], v[1], x[2], and v[2].

# Solution:


```python
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
```
