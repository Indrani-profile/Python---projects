import random

LIMIT =1000

def play_game():
    number = random.randint(1, LIMIT)
    print(" My guess number is from 1 to " + str(LIMIT) + "\n")
    count = 1
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low. ")
            count +=1
        elif guess > number:
            print("Too high.")
            count +=1
        elif guess == number:
            print(f'congrats!.')
            print("You guessed it in " + str(count) + " tries.\n")
            return
        
def main():
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("would you like to play again? (y/n): ")
        print()
    print("Bye!")
    
if __name__ == "__main__":
    main()
    