secret_number = int(input("Enter secret number: "))
while True:
    guess_number = int(input("Guess a number: "))
    if guess_number != secret_number:
        print("Try again!")
    else:
        break
print("Congratulations! You're guessed right!")
