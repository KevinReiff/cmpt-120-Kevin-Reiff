
def start():
    answer = "cat"  
    guess_limit = 3
    guess_count = 0

    print("Please guess the animal I am thinking of, you get 3 guesses")
    while guess_count < guess_limit:
        guess = input("Guess an animal: ").lower()
        guess_count += 1 
        if guess == answer:
            print("You got it!")
            break
        elif guess == "quit":
            guess == quit
            break
        else:
            print("That wasn't right, try again")

    return None 

start()