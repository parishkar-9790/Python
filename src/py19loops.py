# while loop
count = 0
while (count < 3):
    count = count + 1
    print("this is loop ", count)

# else loop
hey = 0
while (hey < 3):
    hey = hey + 1
    print("this is executing")
else:
    print("the loop is executed")

# one line while loop
count1 = 0
while (count1 < 2):
    print("hey parishkar singh ")
    count1 = count1 + 1

# for loop
n = 4
for i in range(0, n):
    print(i)

# list iteration
print("list iteration")
l = ["parishkar singh", "rajawat", "hey there"]
for i in l:
    print(i)

# tuple iteration
print("this is tuple iteration")
t = ("geeks", "for ", "geeks")
for i in t:
    print(i)

# iterationg over a string
print("string iteration")
s = "geeks"
for i in s:
    print(i)

# iterating over dictionary
print("dictionary iteratoin")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

# iterating using list
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

# combining else with for loop
list = ["Geeks ", "for ", "geeks ", "parishkar"]
for index in range(len(list)):
    print(list[index])
else:
    print("else block")
