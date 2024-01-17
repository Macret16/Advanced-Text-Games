import time


def character():
    global inv
    print("#----------------------------------#")
    print("| Hello, Welcome To Heart of Gold. |")
    print("#----------------------------------#")
    print("\nSelect Your Race -\n")
    time.sleep(1)
    print("1) Demigod")
    time.sleep(1)
    print("2) Mortal")
    time.sleep(1)
    print("3) Arcane")
    time.sleep(1)
    print("4) Orge\n")
    choo = int(input(">>> "))
    if choo == 1:
        race = "Demigod"
    elif choo == 2:
        race = "Mortal"
    elif choo == 3:
        race = "Arcane"
    else:
        race = "Orge"
    print()
    time.sleep(1)
    # Weapon selection
    print("Select Your Weapon -\n")
    if race != "Arcane":
        time.sleep(1)
        print("""1) Long Range Bow
    - DMG 40
    - Evasion 30
    - Def 10
    - Speed 20\n""")
        time.sleep(1)
        print("""2) Heavy Axe
    - DMG 45
    - Parry 05
    - Armor 40
    - Speed 10\n""")
        time.sleep(1)
        print("""3) Sword & Shield
    - DMG 25
    - Parry 25
    - Armor 30
    - Speed 20\n""")
        time.sleep(1)
        print("""4) Long Sword
    - DMG 35
    - Parry 15
    - Armor 40
    - Speed 10\n""")
        time.sleep(1)
        print("""5) Spear
    - DMG 40
    - Parry 25
    - Armor 10
    - Speed 25\n""")
        time.sleep(1)
        print("""6) Metal Gloves
    - DMG 15
    - Parry 40
    - Armor 20
    - Speed 25\n""")
        time.sleep(1)
        print("""7) Dual Wielding Knives
    - DMG 20
    - Parry 30
    - Armor 10
    - Speed 40\n""")
        time.sleep(1)
        print("""8) Retractable Claw Gloves
    - DMG 30
    - Parry 25
    - Armor 10
    - Speed 35\n""")
        ch11 = int(input(">>> "))
        print()
        time.sleep(1)
        if ch11 == 1:
            print("You Picked Up Long Range Bow.")
            inv.append("Long Range Bow")
        elif ch11 == 2:
            print("You Picked Up Heavy Axe.")
            inv.append("Heavy Axe")
        elif ch11 == 3:
            print("You Picked Up Sword & Shield")
            inv.append("Sword & Shield")
        elif ch11 == 4:
            print("You Picked Up Long Sword.")
            inv.append("Long Sword")
        elif ch11 == 5:
            print("You Picked Up Spear")
            inv.append("Spear")
        elif ch11 == 6:
            print("You Picked Up Metal Gloves.")
            inv.append("Metal Gloves")
        elif ch11 == 7:
            print("You Picked Up Dual Wielding Knives.")
            inv.append("Dual Wielding Knives")
        else:
            print("You Picked Up Retractable Claw Gloves.")
            inv.append("Retractable Claw Gloves")
    else:
        time.sleep(1)
        print("""1) Elemental Amulet
    - MAGIC DMG 40        
    - Evasion 20
    - MAGIC DEF 30
    - Casting Speed 20\n""")
        time.sleep(1)
        print("""2) Elemental Staff
    - MAGIC DMG 50
    - Evasion 15
    - MAGIC DEF 25
    - Casting Speed 10\n""")
        time.sleep(1)
        print("""3) Elemental Bow
    - Magic DMG 20
    - Evasion 30
    - Magic Def 15
    - Casting Speed 35\n""")
        ch22 = int(input(">>> "))
        print()
        time.sleep(1)
        if ch22 == 1:
            print("You Picked Up Elemental Amulet.")
            inv.append("Elemental Amulet")
        elif ch22 == 2:
            print("You Picked Up Elemental Staff.")
            inv.append("Elemental Staff")
        elif ch22 == 3:
            print("You Picked Up Elemental Bow.")
            inv.append("Elemental Bow")
        else:
            time.sleep(1)
            print("Wrong Choice, Try Again.")
            character()
    print()
    return race


def farmer():
    global inv
    global drachma
    global obol
    global health
    time.sleep(1)
    print("The old farmer welcomes you.\n")
    time.sleep(1)
    print("""“Ah traveller, no doubt you are here on a
mission for the King. He has not been out of his palace
for a long time. We fear his time on this realm may end soon..
Blessed our beloved king. Are you interested in some food?”\n""")
    time.sleep(5)
    print("""1) Purchase a loaf of bread (+20 health)              (COST : 4 obol)
2) Purchase a bag of olives (+2 health)               (COST : 1 obol)
3) Purchase a batch variety of vegetables (+4 health) (COST : 1 drachma)\n""")
    chh1 = int(input(">>> "))
    print()
    if chh1 == 1:
        print("You Purchased a loaf of bread.")
        time.sleep(1)
        health += 20
        print("+20 Health")
        time.sleep(1)
        obol -= 4
        print(f"You paid 4 obol, Now you have {obol} obol left.\n")
    elif chh1 == 2:
        print("You Purchased a bag of olives.")
        time.sleep(1)
        health += 2
        print("+2 Health")
        time.sleep(1)
        obol -= 1
        print(f"You paid 1 obol, Now you have {obol} obol left.\n")
    else:
        print("You Purchased a batch variety of vegetables.")
        time.sleep(1)
        health += 4
        print("+4 Health")
        time.sleep(1)
        drachma -= 1
        print(f"You paid 1 drachma, Now you have {drachma} drachma left.\n")
        time.sleep(2)
    print("You traded with the old farmer and made your purchase.\n")
    time.sleep(1)
    print("Where to next?\n")
    time.sleep(1)
    print("""1) A butcher cutting meat into pieces
2) A lady laying flowers to sell
3) Continue to the palace\n""")
    time.sleep(2)
    chh2 = int((input(">>> ")))
    print()
    if chh2 == 1:
        butcher()
    elif chh2 == 2:
        flower_lady()
    else:
        palace()


def butcher():
    global inv
    global drachma
    global obol
    global health
    time.sleep(1)
    print("The butcher keeps chopping as you approach him.\n")
    time.sleep(1)
    print("“We only have pieces of chicken and lamb. Want anything?”\n")
    time.sleep(1)
    print("""1) Purchase raw chicken piece (to be used as ingredient or bait) (COST : 3 obol)
2) Purchase raw lamb piece (to be used as ingredient or bait)    (COST : 2 obol)
3) Purchase cooked chicken piece (+22 health)                    (COST : 2 drachma)
4) Purchase cooked lamb piece (+18 health)                       (COST : 2 drachma)\n""")
    chhh1 = int(input(">>> "))
    print()
    time.sleep(1)
    print("“Sure sure, I’ll get it for ya.”\n")
    if chhh1 == 1:
        time.sleep(1)
        print("You Purchased a piece of raw chicken.")
        inv.append("Raw Chicken")
        time.sleep(1)
        obol -= 3
        print(f"You paid 3 obol, Now you have {obol} obol left.\n")
    elif chhh1 == 2:
        time.sleep(1)
        print("You Purchased a piece of raw lamb.")
        inv.append("Raw Lamb")
        time.sleep(1)
        obol -= 2
        print(f"You paid 2 obol, Now you have {obol} obol left.\n")
    elif chhh1 == 3:
        time.sleep(1)
        print("You Purchased a piece of cooked chicken.")
        health += 22
        time.sleep(1)
        print("+22 Health")
        time.sleep(1)
        drachma -= 2
        print(f"You paid 2 drachma, Now you have {drachma} drachma left.\n")
    else:
        time.sleep(1)
        print("You Purchased a piece of cooked lamb.")
        health += 18
        time.sleep(1)
        print("+18 Health")
        time.sleep(1)
        drachma -= 2
        print(f"You paid 2 drachma, Now you have {drachma} drachma left.\n")
    time.sleep(1)
    print("You traded with the butcher and made your purchase.\n")
    time.sleep(1)
    print("Where to next?\n")
    time.sleep(1)
    print("""1) An old farmer swatting flies away from his produce
2) A lady laying flowers to sell
3) Continue to the palace\n""")
    time.sleep(2)
    chh3 = int((input(">>> ")))
    print()
    if chh3 == 1:
        farmer()
    elif chh3 == 2:
        flower_lady()
    else:
        palace()


def flower_lady():
    global inv
    time.sleep(1)
    print()
    print("""“Greetings, traveller. Welcome to our little humble town.
We have flowers to honour and flowers to mourn.
It is a grim time we live in..”\n""")
    time.sleep(1)
    print("""1) Flowers to honour
2) Flowers to mourn""")
    cho = int(input(">>> "))
    print()
    if cho == 1:
        time.sleep(1)
        print("""“Olympus remains quiet these days. If not the gods,
may I ask who you will honour?”\n""")
        time.sleep(2)
        print("My father... He was attacked by Daimons trying to save me.\n")
        time.sleep(2)
        print("""“Oh dear. Pray your father settles in Elysium for 
his heroism. Many have died here as well. Our once
prosperous town has seen many disappearances. 
The king remain silent about them yet he
lives within his riches. Despicable…”\n""")
    else:
        time.sleep(1)
        print("“My condolences. May I ask who you will mourn?”\n")
        time.sleep(2)
        print("My father... He was attacked by Daimons trying to save me.\n")
        time.sleep(2)
        print("""“Oh dear. Pray your father settles in Elysium for 
his heroism. Many have died here as well. Our once
prosperous town has seen many disappearances. 
The king remain silent about them yet he
lives within his riches. Despicable…”\n""")
        time.sleep(8)
    print("""1) Was King Midas not a great king? Many has told stories of his kind self.
2) You should have more respect for the king.\n""")
    ch = int(input(">>> "))
    print()
    if ch == 1:
        time.sleep(2)
        print("""“All truth. A once great king. Selfless yet his
greed loss several followers and trade partners. Many
merchants have left with the high tax on our poor village.
Maybe you could speak to the king if you have a chance 
to meet him. He sees a lot of travellers these days.”\n""")
        time.sleep(8)
    else:
        time.sleep(2)
        print("""“I humbly apologise.. It has been a tough time for all of us.
You must have travelled here from great distance to meet
with the king. I am happy for your business. Not a lot
of travellers stop by our village, even after receiving 
great rewards with our tax money. I even saw a 
caravan leave with a golden statue.”\n""")
        time.sleep(8)
    print("I must goo...\n")
    time.sleep(2)
    print("“Take care traveller.”\n")
    time.sleep(1)
    print("""1) An old farmer swatting flies away from his produce
2) A butcher cutting meat into peices
3) Continue to the palace\n""")
    time.sleep(2)
    chh4 = int((input(">>> ")))
    print()
    if chh4 == 1:
        farmer()
    elif chh4 == 2:
        butcher()
    else:
        palace()


def palace():
    global inv
    time.sleep(1)
    print("""As you passed the village make your way onto a dirt path,
you hear the ringing of a small bell. Your bag! It has 
been snatched. You looked around and nobody is there.
On the ground are a small foot prints towards the bushes.
The bushes are ruffling. Maybe a trickster nymph?\n""")
    time.sleep(8)
    print("You step down from your horse and demands the rustling bush.\n")
    time.sleep(3)
    print(f"“Out.. Now.” Pointing towards the bush with your {inv[0]}\n")
    time.sleep(2)
    print("""A kid in tattered clothes walked out.
“What are you doing? Give me back my bag.”\n""")
    time.sleep(4)
    print("""He remain silent. After a short pause, he takes a
few steps towards you and drops the bag on the 
ground next to your horse. You step off your 
horse and reach into your bag.\n""")
    time.sleep(6)
    print("""“Young one.. You shouldn’t do such a thing.
All you must do is ask politely and I will give.”\n""")
    time.sleep(3)
    print("""1) Take out a chunk of bread.
2) Take out a coupe of olives from the bag.
3) Take out a carrot.
4) Take out a cooked piece of chicken.
5) Take out a cooked piece of lamb.
6) Take out a chunk of cheese.\n""")
    time.sleep(2)
    chi = int(input(">>> "))
    print()
    time.sleep(1)
    print("Although hungry, the boy moves away from your hand.\n")
    time.sleep(2)
    print("“What is wrong?”\n")
    time.sleep(2)
    print("“Gold..” he replies. “Please don’t turn me into gold...”\n")
    time.sleep(2)


def part_1(race):
    global inv
    global drachma
    global obol
    global health
    if race == "Demigod":
        village = "Athens"
    elif race == "Mortal":
        village = "Sparta"
    elif race == "Arcane":
        village = "Thessaly"
    elif race == "Orge":
        village = "Delphi"
    time.sleep(3)
    print(f"""You leave your village {village} and head to the
palace of King Midas in North Phrygia, a palace made of gold so pure
King Midas must have made a deal with the gods. As the journey nears
to end, I was left to wonder the very sense of the surrounding.
The people of Midas City lived very poorly while beyond
the town lies a golden palace on the hill.\n""")
    time.sleep(10)
    print("I Thought to myself...")
    time.sleep(1)
    print("I Should stop in town to gather some supplies...\n")
    time.sleep(1)
    print("""1) Check Map
2) Take a Short Break
3) Stop in Town\n""")
    ch1 = int(input(">>> "))
    print()
    if ch1 == 1:
        time.sleep(1)
        print("""As you check the map, you find out that
ahead of you is the once prosperous city of Midas.
Named after the king himself.\n""")
    elif ch1 == 2:
        time.sleep(1)
        print("It has been a long journey. I must rest.\n")
        time.sleep(2)
        print("""You dismount your horse and sit at the base of a tree.
The shade covers you from the hot sun while your horse
is enjoying the soft grass beneath his hoofs..\n""")
        time.sleep(5)
        print("After 1 Hour...\n")
        time.sleep(2)
        print("A well rested break. I must reach the palace before sun down.\n")
    elif ch1 == 3:
        time.sleep(1)
        print("You Decided to Stop By in Town.\n")
        time.sleep(1)
        print("""A kid in tattered clothes ran across your path and bumps into you.
He gets knocked back and is terrified. He quickly 
looks at his hands and arms to make sure he is okay.\n""")
        time.sleep(5)
        print("“Are you alright, young man?”\n")
        time.sleep(1)
        print("""He jumps at your reply and runs quickly across the path.
You see him turn away at a distance and that 
was the last you saw. A strange encounter..\n""")
        time.sleep(4)
    time.sleep(1)
    print("You have arrived at the local market and see a couple stalls.\n")
    time.sleep(2)
    print("""1) An old farmer swatting flies away from his produce
2) A butcher cutting meat into pieces
3) A lady laying flowers to sell\n""")
    ch2 = int((input(">>> ")))
    if ch2 == 1:
        farmer()
    elif ch2 == 2:
        butcher()
    else:
        flower_lady()
    print()
    print("To Be Continued.....\n")
    time.sleep(1)
    print("---- Credits ----")
    time.sleep(1)
    print("==== Hades ====")
    time.sleep(1)
    print("==== Macret ====\n")
    print("--------------------------\n")
    time.sleep(3)
    print("And ya by the way....")
    time.sleep(1)
    print("Part 2 coming soon :)")
    print("---------------------------")
    return


inv = []
obol = 10
drachma = 10
health = 70
a = character()
part_1(a)
input("Press Enter Key To Exit.")