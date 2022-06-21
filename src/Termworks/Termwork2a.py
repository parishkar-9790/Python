# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Termwork 3 Implimentation of Dictionaries
# ...............................................................
def add(student):
    usn = input("Enter USN : ")
    m1, m2, m3 = map(int, input("Enter the three marks: ").split())
    stud[usn] = (m1, m2, m3)


def delete(student):

    usn = input("Enter USN to be deleted : ")
    if usn in stud:
        stud.pop(usn)
        print(usn, " deleted")
    else:
        print(usn, " does not exit")


def computeStudent(student):
    usn = input("Enter USN to compute average : ")
    if usn in student:
        (m1, m2, m3) = (student[usn][0], student[usn][1], student[usn][2])
        best = max(m1, m2)+max(m2, m3)
        avg = max/2
        print("USN : ", usn)
        print("Marks are : ", m1, m2, m3)
        print("Average marks : ", avg)
    else:
        print(usn, " does not exist ")


def display(student):
    print("Student Details : ")
    for usn, data in student.items():
        print("USN: ", usn, " Marks: ", data[0], data[1], data[2])


stud = {}
while True:
    print("\n1: Add Student 2: Delete Student 3: Compute Avg 4: Display Details 5:Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        add(stud)
    elif ch == 2:
        delete(stud)
    elif ch == 3:
        computeStudent(stud)
    elif ch == 4:
        display(stud)
    elif ch == 5:
        break
    else:
        print("Invalid choice!!..Try Again.... ")
