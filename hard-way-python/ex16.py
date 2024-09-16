#reading and writing files
#we have to print this file by ex16.py test.txt

from sys import argv
script, filename = argv
#here below it will just print the lines that what we are working on
print(f"We're going to erase {filename}.")
print("if you don't want that, hit CTRL=C (^C).")
print("IF you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. GOodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") #it will take user input from the user and will store it .txt file
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file. ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()
