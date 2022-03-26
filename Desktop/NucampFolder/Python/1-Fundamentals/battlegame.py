while True:

    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 125

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 115

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("5) Exit")
        choice = input("Choose your character: ").lower()
        if choice == "1" or choice == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif choice == "2" or choice == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif choice == "3" or choice == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif choice == "4" or choice == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif choice == "5" or choice == "exit":
            print("Exiting the game.")
            exit()
        else:
            print("Unknown character")

    print(f"You have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")

    while True:
        dragon_hp = dragon_hp - my_damage
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp} \n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break

        my_hp = my_hp - dragon_damage
        print(f"The Dragon strikes back at the {character}")
        print(f"The {character}'s hitpoints are now: {my_hp}\n")
        if my_hp <= 0:
            print(f"The {character} has lost the battle.\n")
            break

    repeat = input("Do you want to play again? ").lower()
    if repeat == "y" or repeat == "yes":
        continue
    else:
        print("Exiting the game.")
        break
