import random
import time
import pickle


def play():
    a = int(input("Enter the Number of units you want to play with : "))
    if a <= 3:
        for i in range(a):
            name = int(input("""#--------------------#
| Units              |    
+--------------------+
| 1) Warrior         |
|    
| 2) Tanker          |
#--------------------#
| Enter Choice : """))
            if name == 1:
                unitlst.append(plylst[0])
            elif name == 2:
                unitlst.append(plylst[1])
            else:
                print("Wrong Choice, Choose Again.")
                play()
            print("#--------------------#")
    else:
        print("Sorry, You can't play with more than 3 units.")
        play()
    keep_playing = True
    print("#=====================#")
    print("| Your Units -        |")
    for i in unitlst:
        print(f"-> {i}")
    print("#=====================#")
    while (keep_playing is True):
        print()
        nme = random.choice(unitlst)
        slst.append(nme)
        print("""#=====================#
| Total Score :
#=====================#""")
        print("#=====================#")
        print(f"- {nme} : {human_wins}")
        print(f"- AI : {computer_wins}")
        print("#=====================#")
        pl = ["computer", "human"]
        name = input("Name Your Unit : ")
        rounds(pl[0], name, slst)
        slst.pop(0)
        print("======================================")
        response = input("Play another round? (Y/N) : ")
        print("======================================")
        if (response.lower() == "n"):
            main()
        else:
            continue


def computer_move(health):
    sleep_time = random.randrange(2, 3)
    print("....Opponent's Turn....")
    time.sleep(sleep_time)
    if (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 2)


def rounds(computer, human, slst):
    global warrexp, tankexp, warrlvl, tanklvl, human_wins, computer_wins
    u1 = {'name': f'AI'+str(random.randrange(10, 99)), 'health': 100}
    u2 = {'name': f'AI'+str(random.randrange(10, 99)), 'health': 100}
    u3 = {'name': f'AI'+str(random.randrange(10, 99)), 'health': 100}
    in_progress = True
    current_player = computer
    computer_health = 100
    human_health = 100
    rcn = random.randrange(10, 99)
    chop = int(input(f"""
Choose The First Opponent Unit To Attack On -
1. {u1['name']}
2. {u2['name']}
3. {u3['name']}
==========
Enter Choice : """))
    if chop == 1:
        atk = u1
    elif chop == 2:
        atk = u2
    elif chop == 3:
        atk = u3
    else:
        print("Wrong Choice, Try Again.")
        rounds(computer, human, slst)
    computer = atk['name']
    computer_health = atk['health']
    while in_progress:
        if atk == {}:
            print("This unit is already defeated. please choose another one.")
            break
        # swap the current player each round
        if current_player == computer:
            current_player = human
        else:
            current_player = computer
        print()
        print("#=====================#")
        print("| Current Score -     |")
        print("#=====================#")
        print(f"""| {human} : {human_health} 
| {computer} : {computer_health}""")  # atk is the unit which player will choose to attack on
        print("#=====================#")
        print()
        if current_player == human:
            chop = int(input(f"""Choose Oppponent Unit To Attack On -
1. {u1['name']}
2. {u2['name']}
3. {u3['name']}
==========
Enter Choice : """))
            if chop == 1:
                atk = u1
            elif chop == 2:
                atk = u2
            elif chop == 3:
                atk = u3
            else:
                print("Wrong Choice, Try Again.")
                continue
            computer = atk['name']
            atk['health'] = computer_health
            print("#================================#")
            print("| Available Attacks :    ")
            print("""| 1) Attack
| 2) Heal""")
            print("#================================#")
            move = int(input("Enter Choice : "))
        else:
            move = computer_move(computer_health)
        if (move == 1):
            damage = random.randrange(5, 20)
            damage2 = random.randrange(1, 18)
            damage3 = random.randrange(1, 10)
            if (current_player == human):
                if "Warrior" in slst:
                    computer_health = computer_health - damage
                    warrexp += random.randrange(6, 30)
                else:
                    computer_health = computer_health - damage3
                    tankexp += random.randrange(6, 25)
            else:
                human_health = human_health - damage2
        elif (move == 2):
            heal = random.randrange(15, 25)
            healcomp = random.randrange(5, 15)
            if (current_player == human):
                human_health = human_health + heal
            else:
                if computer_health < 15:
                    computer_health = computer_health + healcomp
                else:
                    continue
        else:
            print()
            print("Wrong Choice, Please Try Again!")
            print()

        if (human_health < 0):
            print("+==================+")
            print("| Sorry, you lose! |")
            print("+==================+")
            unitlst.remove(slst[0])
            computer_wins += 1
            game_in_progress = False
            break

        if (computer_health < 0):
            print("+==========================================+")
            print("| Congratulations!, you beat the opponent! |")
            print("+==========================================+")
            human_wins += 1
            game_in_progress = False
            atk.clear()
            break
    if warrexp >= 100:
        print("======================================")
        print(f"Congratulations! Warrior Level Up!")
        warrlvl += 1
        warrexp -= 100
    if tankexp >= 100:
        print("======================================")
        print(f"Congratulations! Tanker Level Up!")
        tanklvl += 1
        tankexp -= 100
    info = open("warrior.dat", "ab+")
    info2 = open("tanker.dat", "ab+")
    info3 = open("win.dat", "ab+")
    d1 = {'Name': 'Warrior', 'Level': warrlvl, 'Exp': warrexp}
    d2 = {'Name': 'Tanker', 'Level': tanklvl, 'Exp': tankexp}
    d3 = {"Unit's Wins": human_wins, "AI Wins": computer_wins}
    pickle.dump(d1, info)
    pickle.dump(d2, info2)
    pickle.dump(d3, info3)
    info.close()
    info2.close()
    info3.close()


def players():
    try:
        info = open("warrior.dat", "rb+")
        lo = pickle.load(info)
        showlst = []
        showlst2 = []
        showlst.append(lo)
        info2 = open("tanker.dat", "rb+")
        lo2 = pickle.load(info2)
        showlst.append(lo2)
        info3 = open("win.dat", "rb+")
        lo3 = pickle.load(info3)
        showlst2.append(lo3)
        for k in showlst:
            while k['Exp'] > 100:
                k['Exp'] -= 100
                k['Level'] += 1
            print(k)
        for i in showlst2:
            print(i)
        info.close()
        info2.close()
        info3.close()
    except:
        print("No Data Available.")
        print("==================")
    print("#========================================#")
    input("Press any key to continue....")
    main()


def main():
    print("                  ---                 ")
    print("""#=====================================#
| 1. Play Game                        |
|-------------------------------------|
| 2. View Information                 |
|-------------------------------------|
| 3. Quit                             |
#=====================================#""")
    ma = int(input("| Enter Your Choice : "))
    print("#=====================================#")
    print()
    if ma == 1:
        play()
    elif ma == 2:
        players()
    elif ma == 3:
        quit()
    else:
        print("Wrong Choice, Try Again!")
        print()
        main()
    print()


print("#=====================================#")
print("|  Welcome To Turn-Based Battle Game  |")
print("#=====================================#")
warrexp = 0
tankexp = 0
warrlvl = 0
tanklvl = 0
plylst = ["Warrior", "Tanker"]
unitlst = []
slst = []
computer_wins = 0
human_wins = 0
main()
("\nThank you for playing!\nMade by - Karan Jaswani\n")