#arbitary arguments
def args(*kudos):
    print("the value the 3nd passed argument is "+ kudos[2])

args("parishkar","singh","rajawat")

#keyword arguments 
def function222(child3,child2,child1):
    print("the youngest child is "+ child3)
    
function222(child1="emily",child2="parishkar",child3="lmao")

def my_function(**kid):
    print("His last name is " + kid["lname"])

#arbitary keywords arguments **kwargs
my_function(fname = "Tobias", lname = "Refsnes")