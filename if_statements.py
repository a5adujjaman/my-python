#here we will compare if statement for boolean value

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):  #not funciton for tall
    print("You are a short male")
elif not(is_male) and is_tall:   # not funciton for male
    print("You are a tall but not male")
else:
    print("You are either not male or not tall")
