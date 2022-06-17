import json

def printChild(data):
    print("The Found labourer's are:- ")
    for i in data['empDetails']:
        if int(i['age']) < 18:
            print(i['eid'], i['ename'], i['age'])


def printEmps(data):
    for i in data['empDetails']:
        print(i['eid'], i['ename'], i['age'])


def printEmp(data):
    x = int(input('Enter the EMP id--> '))
    for i in data['empDetails']:
        if i['eid'] == x:
            print(i['eid'], i['ename'], i['age'])
            break
    else:
        print("Not Found")


if __name__ == '__main__':
    with open('X:\\Python\\src\\Assignments\\4_16June\\Employee.json') as f:
        data = json.load(f)
        while True:
            x = input(
                "Enter choice  1.Found Child Labourers  2.Display Employee Data  3.Display all employees--> ")
            if x == '1':
                printChild(data)
            elif x == '2':
                printEmp(data)
            elif x == '3':
                printEmps(data)
