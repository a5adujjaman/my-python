from sys import argv
#we have to open this code by python3 ex15.py ex15_sample.txt
script, filename = argv

txt = open(filename)
print(f"here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
