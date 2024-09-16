

def say_hi(): #the colon means that its actually a function
    print("Hello User")

print("Top") #this line will just simply print
say_hi()
print("Bottom")

#here used function parameter and we can change the value
def parameter(name, age):
    print("Hello " + name + " your age is " + age)
    #here we can also change the type of the each value like
    #here we changed the age value as string
    print("Hello " + name + " your age is " + str(age))

parameter("mike", "35")
parameter("john", "40")