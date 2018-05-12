# Problem Desciption

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#### Input Format

A single line of five space-separated integers.

# Solution
```python
p=[]
maxx = max(arr)
arr.remove(maxx)
p.append(sum(arr))
arr.append(maxx)
arr.remove(min(arr))
p.append(sum(arr))
print(p[0],p[1])    
```
