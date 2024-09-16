number = int(input("Enter your number: ")) #must add the type of the inputed value
#otherwise it won't work
if number%2 == 0 :
    print("Its an Even Number")
else :
    print("Its an Odd Number")

rock = int(input("enter your input: "))
if rock+2 >= 8 and rock+2 <30: #for two condition at once and will use
    print("its fair")
elif rock+2 >= 30 and rock+2 <50: #here it will be elif not else if as c
    print("its big")


# Simple Python program to understand elif statement
marks = int(input("Enter the marks? "))
# Here, we are taking an integer marks and taking input dynamically
if marks > 85 and marks <= 100:
# Here, we are checking the condition. If the condition is true, we will enter the block
   print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
# Here, we are checking the condition. If the condition is true, we will enter the block
   print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
# Here, we are checking the condition. If the condition is true, we will enter the block
   print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
# Here, we are checking the condition. If the condition is true, we will enter the block
   print("You scored grade C ...")
else:
   print("Sorry you are fail ?")
