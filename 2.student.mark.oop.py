#pc2

#class student
class Students:
    #student in4 input
    def student_input(n, student):
        for i in range(n):
            print("ID, Name, Dob: ",end='')
            k=map(str, input().split(", "))
            student.append(list(k))

class Courses:
    #inp course
    def course_input(n, course):
        for i in range(n):
            print("ID, Name: ",end='')
            k=map(str, input().split(", "))
            course.append(list(k))
    #inp points
    def score_input(n, student, course, mark):
        for i in student:
            point=[]
            for j in course:
                k=float(input(j[1]+" score of student "+i[1]+": "))
                point.append(k)
            mark.append(point)
def show():
    #show marks
    for i in range(len(student)):
        print("\n"*2)
        print(student[i])
        for j in range(len(course)):
            print(str(course[j][0]),end=' ')
            print(str(course[j][1])+":",end=' ')
            print(mark[i][j])

#var
student=[]
course=[]
mark=[]

#inp student
n=int(input("Amount of student: "))
Students.student_input(n, student)
n=int(input("Amount of courses: "))
Courses.course_input(n, course)
Courses.score_input(n, student, course, mark)
show()
