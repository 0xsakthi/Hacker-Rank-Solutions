if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n): #to add number of students in var n 
        name, *line = input().split() #spliting and print/add a value in one line so use *list
        scores = list(map(float, line)) #convert to float
        student_marks[name] = scores #convert to dictionary
    query_name = input() #to get marks to given format(name 
    marks = student_marks[query_name] #store a student marks
    print(format(sum(marks)/3,'.2f')) #sum and divided by 3 
