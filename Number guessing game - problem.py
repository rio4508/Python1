"""
Create a number guessing game.
The user gets 10 chances to guess a number.
"""
import random
correct_number = random.randint(1,50)
limit = 10
attempt = 0
is_guess_correct = False
print("This is number guessing game.\nThe correct number is in between 1 to 50, and you have 10 guesses.")
while attempt <= limit:
    guess = int(input("Guess a number: "))
    if guess == correct_number:
        print("Correct you have successfully guessed the number.\n Game over!!")
        is_guess_correct = True
        break
    else:
        remaining_chances= limit - attempt


        if guess < correct_number:
            higher_or_lower="higher"

        elif guess > correct_number:
            higher_or_lower ="lower"
        print(f"Your guessing is wrong.Try {higher_or_lower} number.")


        attempt += 1
        remaining_chances-= 1
        print(f"you have {remaining_chances} left")


print(f"the secret number is {correct_number}.Game over!!")
if not is_guess_correct:
    print("better luck next time")



