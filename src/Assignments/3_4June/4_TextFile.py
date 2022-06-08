# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# opens a text file and counts all the word whose first letter is s and last is r
# ...............................................................


with open('D:\\C++\\Python\\src\\Assignments\\3_4June\\Story.txt') as f:
    words = f.read().split(' ')
    count = 0
    srWords = []
    for i in words:
        if i[0].lower() == 's' and i[len(i)-1].lower() == 'r':
            count += 1
            srWords.append(i)
    print('The words which contains first letter `s` and last letter `r` are: -> ', end=' ')
    for i in srWords:
        print(i, end=' ')
    print()
    print('Number of words which start with s and r --> ', count)
    print('The Total Number of words is ---> ', len(words))
