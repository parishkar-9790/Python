# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Storing the following info
# ...............................................................


def addcourse(course):
    cc = input("enter the Course code to add: ")
    m1, m2, m3 = input(
        "Enter the Course Name, Faculty name, Number of registrations: ").split()
    course[cc] = [m1, m2, int(m3)]


def MAXreg(course):
    maxcourse = ""
    maxreg = 0
    for cc in course:
        if course[cc][2] > maxreg:
            maxreg = course[cc][2]
            maxcourse = cc
    print(
        f"The course {maxcourse} has the maximum number of registrations {maxreg}")


def coursedetailes(course):
    cc = input("Enter the course code of the subject : ")
    if cc in course:
        print(
            f"Course code: {cc}  Course Name:{course[cc][0]}  Faculty Name : {course[cc][1]}  Number of Registrations: {course[cc][2]} ")


def display(course):
    for cc in course:
        print(
            f"Course code: {cc}  Course Name:{course[cc][0]}  Faculty Name : {course[cc][1]}  Number of Registrations: {course[cc][2]} ")


if __name__ == '__main__':
    course = {'18CSL46': ['python', 'sfr', 200], '18CSL36': ['web', 'PVT', 30]}
    while True:
        x = int(input(
            "\nMenu\n1.Show Course Details using Course code \n2.Course with highest number of registrations \n3.Add course\n4.Show all course  \nEnter your choice-> "))
        if x == 1:
            coursedetailes(course)
        elif x == 2:
            MAXreg(course)
        elif x == 3:
            addcourse(course)
        elif x == 4:
            display(course)
