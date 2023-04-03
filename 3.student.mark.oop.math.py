#pc2
#import library
import math
import numpy as np
import sys,os
import curses

#UI Des
def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        #stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "example"[:width-1]
        curses.echo()# Enable echoing of characters
        # Get a 15-character string, with the cursor on the top line
        s = stdscr.getstr(0,0, 15)
        subtitle = "Just a demo"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

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
                point.append(math.floor(k))
            mark.append(point)

class Showing:
    def show_full_marks():
        #show marks
        Showing.get_GPA()
        for i in range(len(student)):
            print("\n"*2)
            print(student[i])
            for j in range(len(course)):
                print(str(course[j][0]),end=' ')
                print(str(course[j][1])+":",end=' ')
                print(mark[i][j])
            print("GPA: ")
            print(gpa[i])

    def get_GPA():
        #show marks
        for i in range(len(student)):
            tong = 0;
            for j in range(len(course)):
                tong += mark[i][j]
            gpa.append(tong/len(course))
    
    def showing_GPA():
        print("Descending")
        #show marks
        for i in reversed(range(len(sorted_gpa))):
            print("\n")
            print(sorted_gpa[i])

#var
student=[]
course=[]
mark=[]
gpa = []
sorted_gpa = []

def main():
    #UI init
    curses.wrapper(draw_menu)
    #inp student
    n=int(input("Amount of student: "))
    Students.student_input(n, student)
    n=int(input("Amount of courses: "))
    Courses.course_input(n, course)
    Courses.score_input(n, student, course, mark)
    Showing.show_full_marks()
    sorted_gpa = np.array(gpa)
    np.sort(sorted_gpa)
    #sorted_gpa = temp
    Showing.showing_GPA()

if __name__ == "__main__":
    main()
