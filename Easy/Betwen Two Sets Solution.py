def getTotalX(a, b):    
    num_div_by_a = list(range(1,101))  
    all_num_list = list(range(1,101))  
    num_div_b = []
    comb_list = []
    for i in range(len(a)):       #finding all numbers divisible by a
        for j in range(len(num_div_by_a)):
            if num_div_by_a[j]%a[i] != 0:
                num_div_by_a[j] = 101
    for i in range(len(b)):       #finding all numbers that divide into b
        j = 0
        while j < len(all_num_list):
            if b[i]%all_num_list[j] != 0:
                num_div_b.append(all_num_list[j]) 
            j += 1
    for i in range(len(num_div_by_a)):    #finding the common numbers from previous steps
        if num_div_by_a[i] not in num_div_b:
            comb_list.append(num_div_by_a[i])
    while 101 in comb_list: 
        comb_list.remove(101)
    return(len(comb_list))



nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
total = getTotalX(a, b)
print(total)
