
    a, b, c = map(int, input("Enter the 3 Sides : ").split())
    if(checktriangle(a, b, c)):
        print("The sides represents a triangle %4.3f" % computerarea(a, b, c))