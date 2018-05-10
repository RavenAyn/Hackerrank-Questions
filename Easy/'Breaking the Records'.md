# Problem Description

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array _score_ = [12,24,10,24]. Scores are in the same order as the games played. She would tabulate her results as follows:

```
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
 ```

 
Given Maria's array of _scores_ for a season of _n_ games, find and print the number of times she breaks her records for most and least points scored during the season.

Input Format

The first line contains an integer _n_, the number of games. 
The second line contains _n_ space-separated integers describing the respective values of _score[0], ... , score[n-1]_

# Solution

```python
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
```

