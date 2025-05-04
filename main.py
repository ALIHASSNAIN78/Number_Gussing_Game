import random

def game(attempt):
    while (attempt > 0):
        num = int(input("Please enter a number between 1 and 100: "))
        if num < rd:
            print("Your guess is too low.")
            attempt -= 1

        elif num > rd:
            print("Your guess is too high.")
            attempt -= 1
        else:
            print("Congratulations! You guessed the number!")
            break

    if attempt == 0:
        print("Sorry, you have used all your attempts. The number was:", rd)


rd = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I have selected a random number between 1 and 100.")
attempt = int(input("Please Select the number of attempts you want to make: "))
game(attempt)

while True:
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        rd = random.randint(1, 100)
        attempt = int(input("Please Select the number of attempts you want to make: "))
        game(attempt)
    elif play_again == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


print("Thank you for playing!")
