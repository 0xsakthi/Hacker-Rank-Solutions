#!/usr/bin/python3

total =[] #total-nested-list-name-with-marks
grade =[] #students-grades
n = int(input()) #input number of students
for i in range(n):
    name = input()
    marks = float(input())
    total.append([name,marks]) 
    grade.append(marks)
#print(total,grade)
x = sorted(set(grade))
#print(x)
y = x[1] #to find second lowest value 
#print(y)

finalanswer = []

for value in total:
    if y==value[1]:
        finalanswer.append(value[0]) #appending the name equal to y
finalanswer.sort() #sorting a name

for nm in finalanswer:
    print(nm)
    






