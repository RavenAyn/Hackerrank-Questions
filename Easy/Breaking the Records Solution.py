n = int(input())
score = list(map(int, input().rstrip().split()))

def breakingRecords(score):
    min_score = score[0] 
    max_score = score[0]
    min_counter = 0
    max_counter = 0
    for i in range(1,len(score)):
        if score[i] < min_score:
            min_counter += 1
            min_score = score[i]
        elif score[i] > max_score:
            max_counter += 1
            max_score = score[i]
            
    return(max_counter,min_counter)


result = breakingRecords(score)
print(result)
