def cheese_and_crackers(cheese_count, boxes_of_crackers):

    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers} boxes of crackres")
    print("Man that's enough for a party")
    print("Get a blanket.\n")


#we can directly put value in function arguments like this
print("we can just give the functions number directly:") #for the code output will start from here
cheese_and_crackers(20,30) #for this code all the thing will print from here

print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_cracker = 50

#we have replaced the value as new by new variables amount_of_cheese, amount_of_cracker
cheese_and_crackers(amount_of_cheese, amount_of_cracker)

#we can do math inside function arguments
print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_cracker + 1000)


#my practice here

def myfunction(prothom, ditio):

    print(f"ekhane print hobe j argument1 e ki ache seta holo {prothom}")
    print(f"ekhane print hobe j argument2 te ki ache seta holo {ditio}")

print("ekhane ami funciton ta call korlam jate function er vitore ki ache segulo kaj kore")
prothom = 50
ditio = 40
myfunction(prothom,ditio)

print("ebar ei duita jog kore dibo")
myfunction(prothom + 5, ditio + 4) # er mane funciton e ja ache segulo print hobe abong argument gulor value change koray segulow change hobe
