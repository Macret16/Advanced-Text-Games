import time
import random


def game():
    # Asking name of the user to save the score
    name = input("Enter You Name : ").title()
    print("Hello, " + name.title(), "Let's Start The Game!")
    time.sleep(1)
    print("Start Guessing...\n")
    time.sleep(0.5)
    # A List Of Secret Words to guess
    words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror', 'computer', 'adventure']
    word = random.choice(words)
    guesses = ""
    turns = 5
    score = 0
    while turns > 0:
        fail = 0
        for char in word:
            if char in guesses:
                # If guessed word is right it will be printed
                print(char, end="")
                score += 1
            else:
                # if guessed word is not right, it will be blank
                print("_", end=""),
                fail += 1
        if fail == 0:
            print("\nYou Won!!!")
            break
        guess = input("\nGuess a character : ")
        guesses += guess
        # if your guessed character not in the word which you are guessing
        if guess not in word:
            turns -= 1
            print("\nWrong Guess!")
            print("You have", + turns, 'more guesses')
            # If turns are 0, the game will be over
            if turns == 0:
                print("The Word was :", word)
                print("===== Game Over! =====")
    print("Your Total Score :", score)
    # opening the text file to write and save the score
    file = open("scores.txt", "a+")
    # if score is more than 0 then only it will be saved in the text file
    if score > 0:
        file.writelines(name + " : " + str(score)+"\n")
    else:
        pass
    file.close()


def score():
    time.sleep(1)
    print()
    # opening the score text file to fetch the saved scores
    file = open("scores.txt", "r")
    a = file.read()
    # displaying all the scores
    print("=== All Scores ===")
    print(a)
    file.close()


print("#--------------------#")
print("| Welcome To Hangman |")
print("#--------------------#")
# Main menu
while True:
    print()
    print("===== Main Menu =====")
    print("""1. Play Game
2. See All Scores
3. Exit Game""")
    print()
    ch = int(input("Enter Choice : "))
    if ch == 1:
        game()
    elif ch == 2:
        score()
    elif ch == 3:
        exit()
    else:
        print("Wrong Choice, Try Again!")
        continue


