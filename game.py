import random           

guessed_nums = []           
allowed_guesses = 0         
difficulty = 0

#Difficulty Selection
while True:
    selection = input("Select EASY/MEDIUM/HARD: ")
    if selection == "EASY":
        print("You have 6 guesses")
        allowed_guesses = 6
        difficulty = 10
        break
    if selection == "MEDIUM":
        print("You have 4 guesses")
        allowed_guesses = 4
        difficulty = 20
    else:
        if selection == "HARD":
            print("You have 3 guesses")
            allowed_guesses = 3
            difficulty = 50
    break

rand_num = random.randint(1, difficulty)



while len(guessed_nums) < allowed_guesses:          
#make sure this section updates based on difficulty selection.
    guess = input("Guess a number between 1 and {}. \n".format(difficulty))    #user guesses number

    try:                            
        player_num = int(guess)
    except:
        print("That's not a whole number!")
        break
#mthis section updates based on difficulty selection.
    if not player_num > 0 or not player_num <= difficulty:
        print("Please guess a number between 1 and {}".format(difficulty))
        continue

    guessed_nums.append(player_num)

    if player_num == rand_num:              
        print("You got it right!".format(rand_num))
        print("It took you {} tries.".format(len(guessed_nums)))
        break
    else:
        print("That was wrong. Guess #{}".format(len(guessed_nums)))
        continue

if not rand_num in guessed_nums:                
    print("Game over! My number was {}".format(rand_num))
