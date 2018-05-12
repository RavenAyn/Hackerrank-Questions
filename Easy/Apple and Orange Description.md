# Problem Description

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where _s_ is the start point, and _t_ is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point _a_, and the orange tree is at point _b_.

![alt text](https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png)

When a fruit falls from its tree, it lands  units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell _d_ units to the tree's left, and a positive value of _d_ means it falls _d_ units to the tree's right.

Complete the function ```countApplesAndOranges```,

where,

_s_ Starting point of Sam's house location. 
_t_ Ending location of Sam's house location. 
_a_ Location of the Apple tree. 
_b_ Location of the Orange tree. 
_m_ Number of apples that fell from the tree. 
_apples_ Distance at which each apple falls from the tree. 
_n_ Number of oranges that fell from the tree. 
_oranges_ Distance at which each orange falls from the tree.

Given the value of _d_ for _m_ apples and _n_ oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.

Input Format

- The first line contains two space-separated integers denoting the respective values of _s_ and _t_. 
- The second line contains two space-separated integers denoting the respective values of _a_ and _b_.
- The third line contains two space-separated integers denoting the respective values of _m_ and _n_. 
- The fourth line contains _m_ space-separated integers denoting the respective distances that each apple falls from point _a_. 
- The fifth line contains _n_ space-separated integers denoting the respective distances that each orange falls from point _b_.

# Solution

```python
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0
    for i in range(len(apples)):
        if s <= (apples[i] + a) <=t:
            apples_on_house +=1
    print(apples_on_house)
    for i in range(len(oranges)):
        if s <= (oranges[i] + b) <=t:
            oranges_on_house +=1
    print(oranges_on_house)
        
    
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apple = list(map(int, input().rstrip().split()))
orange = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apple, orange)
```
