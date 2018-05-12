# Problem Description

HackerLand University has the following grading policy:

Every student receives a _grade_ in the inclusive range 0 from 100 to .
Any _grade_ less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's _grade_ according to these rules:

- If the difference between the _grade_ and the next multiple of 5 is less than 3, round _grade_up to the next multiple of 5.
- If the value of _grade_ is less than 38, no rounding occurs as the result will still be a failing grade.
For example, _grade_ = 84 will be rounded to 85 but_grade_ = 29  will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of _grade_ for each of Sam's  students, write code to automate the rounding process. Complete the function solve that takes an integer array of all grades, and return an integer array consisting of the rounded grades. For each _grade[i]_, round it according to the rules above and print the result on a new line.

#### Input Format

The first line contains a single integer denoting _n_ (the number of students). 
Each line  of the  subsequent lines contains a single integer, _grade[i]_, denoting student i's grade.

# Solution

```python

def gradingStudents(grades):
    for i in range(n):
        if grades[i] >= 38:
            next_mult = grades[i]//5 +1
            diff = abs(next_mult*5 - grades[i])
            if diff < 3: 
                grades[i] = next_mult*5
              
    return(grades)
n = int(input())
grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
result = gradingStudents(grades)
print(result)
    return(grades)
```
