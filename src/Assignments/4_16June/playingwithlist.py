from operator import itemgetter
list = [['market', 2,7], ['nice', 1,4], ['jquery', 4,567], ['hey', 3,200], ['hello', 6,23]]
# sorted(list,key=itemgetter(1))
list.sort(key=lambda x: x[2])
print(list[-1])
record.sort(key=lambda x: (len(x[9]), x[9]))