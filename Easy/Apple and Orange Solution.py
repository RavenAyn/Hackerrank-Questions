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
