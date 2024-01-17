import random
import time


def start():
    print()
    print("""You wake up in an initially dark room,
lying on the floor. You feel dizzy and weak and have no idea where you are.
Suddenly, the room starts to glow blue. You finally start to see more clearly.
You notice one big door with a hamster painted on it.
""")
    time.sleep(10)
    print("""Looking around a little bit more, you notice 
a purple STAR shaped figure, but one edge is actually missing. 
Seeing that weird symbol, you start to realize that 
you have seen this thing before.""")
    time.sleep(8)
    print()
    print("What would you like to do?")
    print("""1. Go through the door
2. Take a closer look at the figure
""")
    ch = int(input(">>> "))
    if ch == 1:
        intpuzzle()
    elif ch == 2:
        figure()
    else:
        print("Wrong Choice, Try Again")
        start()


def figure():
    time.sleep(1)
    print()
    print("""You approach the figure and take it in your hands.
Especially the missing edge seems to bother you. You turn the star
around and try to find something useful. Suddenly a small arrow
flies out of the missing edge, hitting you in the arm.""")
    time.sleep(10)
    print()
    print("""You are in shock and try to instantly pull out the arrow.
You realize the arrow has a green tip and a weird smell
and figure out that you have been poisoned.""")
    time.sleep(5)
    print()
    ch = input("Do you want to go through the door? (y/n): ")
    if "y" in ch:
        intpuzzle()
    else:
        print("""The room was being filled with smoke,
you couldn't breathe and you died.
Game Over!""")


def intpuzzle():
    time.sleep(1)
    print()
    print("""You go through the door which as a hamster on it. You notice a big desk
with a laptop on it. You also notice two chairs, but one is missing one leg.
You do not really care about the lost leg at the moment and approach the laptop.
The screen of the laptop shows the following message :""")
    time.sleep(10)
    print()
    print("""INTELLIGENCE PUZZLE Starts Here, just a random question
with an easy answer. If your answer is correct, the next door opens.
Otherwise you will die!""")
    time.sleep(8)
    q1 = ["How Much Cores Does A Quad-Core Processor Has?", "4", "four"]
    q2 = ["What Is Called The Brain Of A Computer?", "cpu"]
    lst = [q1[0], q2[0]]
    ques = random.choice(lst)
    print(ques)
    ans = input(">>> ").lower()
    if ques == q1[0] and ans in q1:
        dexpuzzle()
    elif ques == q2[0] and ans in q2:
        dexpuzzle()
    else:
        print("""The answer was wrong and the laptop exploded
Game Over!""")
        exit()


def dexpuzzle():
    time.sleep(1)
    print()
    print("""You were able to solve the puzzle and the next door
slightly cracks and seems to open. After entering the door you
immediately see another door, which has a keypad attached to it.
Moreover, you can notice a letter lying the floor. The letter is covered
in sweat and you realize that someone has been here not too long ago.""")
    time.sleep(7)
    print()
    print("""What do you want to do :
1. Go to the keypad
2. Read the letter
""")
    ch = int(input(">>> "))
    if ch == 1:
        keypuzzle()
    elif ch == 2:
        letter()
    else:
        print("Wrong Choice, Type Again.")
        dexpuzzle()


def keypuzzle():
    time.sleep(1)
    print()
    print("""* Instructions on the display *
Rewrite the following sentence as quickly as you can. Before you
know what is going on, a timer appears on the display 
starting immediately at 30 seconds.
""")
    time.sleep(7)
    print()
    print("Do You Want To Read The letter? (y/n)")
    print("Type n if you have read it already.")
    ch = input(">>> ").lower()
    if "y" in ch:
        letter()
    elif "n" in ch:
        pass
    else:
        print("""The time is over and the room exploded.
Game Over!""")
    a = "SEVEN FROGS ARE ONE TOO MANY"
    print()
    sen = input("Write The Sentence Here : ").upper()
    print()
    if sen == a:
        time.sleep(3)
        print("""You've successfully typed in the correct sentence within 
the time frame. Another door opens. You do not have a good
feeling about that next door, but you pull yourself
together and walk through the next door.""")
        time.sleep(10)
        lastroom()
    else:
        print("The sentence is wrong. Game Over!")


def letter():
    time.sleep(1)
    print()
    print("SEVEN FROGS ARE ONE TOO MANY")
    keypuzzle()


def lastroom():
    time.sleep(1)
    print()
    print("""As you enter the room, you realize that the room 
is filled with water. Thinking back to your last chemistry class,
you realize how much you hate it. You were never able
to memorize the chemical formula.""")
    time.sleep(7)
    print()
    print("""After wandering with your thoughts about happier times,
you see a first aid kit hanging on the wall.
Besides the first aid kit is, of course, another door.""")
    print()
    print("""What do you want to do :
1. Approach the first aid kit
2. Approach the door
""")
    ch = int(input(">>> "))
    if ch == 1:
        print("""You take the first aid kit and 
heal on your wounds with the bandages""")
        time.sleep(3)
        print("and you open the door and successfully complete the Game!")
    elif ch == 2:
        print("You open the door and successfully complete the Game!")
    else:
        print("Wrong Choice, Try Again")
        lastroom()


start()
print("\nThanks for playing!\nMade by - Karan Jaswani")