import random

a = random.randint(1, 500)

for j in range(2, 12):
    b = int(input("Guess The Number : "))
    if b > a:
        print("Please Try A Smaller Number Than", b) 
    if b < a:
        print("Please Try A Bigger Number Than", b)
    f = j - 1
    if a != b:
        print(f, "Chances Used Out Of 10.")
    if a == b:
        print("Congrats You Guessed The Right Number!, It Was", str(a)+".")
        break
    f = j - 1
    if f == 10 and a != b:
        print("Game Over!, The Number Was", str(a)+".")
        break
print("\nThanks for playing!\nMade by - Karan Jaswani\n")