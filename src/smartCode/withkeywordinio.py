# f = open("D:\\C++\\Python\\src\\smartCode\\smart.txt", "w")
# f.write("hello there")
# f.close()

# instead of above code
with open("D:\\C++\\Python\\src\\smartCode\\smart.txt", "w") as f:
    f.write("THis is more efficient way then before ")
