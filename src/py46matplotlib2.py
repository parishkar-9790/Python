from matplotlib import pyplot as plt
roll = [x for x in range(1, 11)]
marks = [y*y+2 for y in range(11, 21)]
# print (marks)
plt.plot(roll, marks)
plt.xlabel('Roll Number')
plt.ylabel('marks')
plt.title('Student data')
plt.show()
