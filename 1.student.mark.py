#pc1

#inp student
n=int(input("Amount of student: "))
student=[]

for i in range(n):
        print("ID, Name, Dob: ",end='')
        k=map(str, input().split(", "))
        student.append(list(k))

#inp course
n=int(input("Amount of courses: "))
course=[]

for i in range(n):
        print("ID, Name: ",end='')
        k=map(str, input().split(", "))
        course.append(list(k))

#inp points
mark=[]
for i in student:
        point=[]
        for j in course:
            k=float(input(j[1]+" score of student "+i[1]+": "))
            point.append(k)
        mark.append(point)

#show marks
for i in range(len(student)):
        print("\n"*2)
        print(student[i][1])
        for j in range(len(course)):
            print(str(course[j][0]),end=' ')
            print(str(course[j][1])+":",end=' ')
            print(mark[i][j])
