#"format": it's called an "f-string" and looks like this
#f"some stuff here {a variable}"
#f"some another stuff here {another variable}"

types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I said: '{y}'")

w = "This is the left side of ... "
e = "a string with a right side."

print(w+e)
