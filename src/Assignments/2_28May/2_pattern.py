# Question 2 Pattern Printing

def printPattern():
    for i in range(1, 5):

        print('\t', '\t'*(4-i), end='')
        if i == 4:
            for j in range(1, i+2):
                print('*', end='')
                if j in (2, 3):
                    print(end='\t'+' '*(j+1))
                else:
                    print(end='\t\t')
        else:
            for j in range(1, i+1):
                print('*', end='\t\t')
        print('\n')


if __name__ == '__main__':
    printPattern()
