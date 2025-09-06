import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    

    number = random.randint(1, 100)
    

    difficulty = input("Choose difficulty: 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == "easy" else 5
    
    while attempts > 0:
        guess = int(input(f"Make a guess ({attempts} attempts left): "))
        
        if guess == number:
            print(f"🎉 Correct! The number was {number}. You win!")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts -= 1
    
    print(f"❌ You've run out of attempts. The number was {number}.")

if __name__ == "__main__":
    number_guessing_game()
