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
