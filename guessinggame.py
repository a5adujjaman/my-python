secret_word = "ashu"
guess = "" #here we created a guess variable using guess = "" as a string
guess_count = 0
guess_limit = 3
out_of_guesses = False #as default as boolean we keep it false

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
    #if we start the print here then it will just print without while loop condition
    #so we have to mind it the formatting and allignment
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses You loose")
else:
    print("You Win!")
