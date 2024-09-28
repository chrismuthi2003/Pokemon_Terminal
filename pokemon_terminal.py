import os
from time import sleep
import random
import sys

os.system("clear")

name = input("Name your Pokémon: ").strip()
enemy_pokemon_list = ["Ligma", "Sugma", "Trigma", "Yomama", "Joe", "Obama", "League Of Legends", "Nunu", "Xicor, The World Annihilator"]

os.system("clear")

class Pokemon:

    def __init__(self, name, lvl, exp, hp, maxhp, defence, tackle, leer):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.hp = hp
        self.maxhp = maxhp
        self.defence = defence
        self.tackle = tackle
        self.leer = leer

    def stats(self):
        return f"Name: {self.name}\nLVL: {self.lvl}\nHP: {self.hp}/{self.maxhp}"


p1 = Pokemon(name, 5, 0, 25, 25, 10, 40, 3)


class Menu:

    def choice(self):
        print("Choose option")
        print("1. Fight wild Pokémon")
        print("2. Heal in Pokécenter")
        print("3. Quit")
        print("")
        chosen = int(input("> "))
        return chosen
    
def BattleScreen(p1, p2):
    while(p1.hp > 0 and p2.hp > 0):
        print("")
        print("1. Tackle")
        print("2. Leer")
        print("")
        move = int(input("> "))
        
        if(move == 1):
            damage = 10 - int(p2.defence)
            p2.hp = p2.hp - damage
            print(p1.name + " used Tackle!")
            sleep(1)
            print(p1.name + " did " + str(damage) + " to " + p2.name + "!")
            sleep(1)
            print(p2.name + " now has " + str(p2.hp) + "/" + str(p2.maxhp) + "hp")
            sleep(1)

            if(p2.hp <= 0):
                print(f"{p2.name} has fainted!")

        if(move == 2):
            p2.defence = p2.defence - 3
            if(p2.defence < 0):
                print(p2.name + "'s defence can't fall any further")
                sleep(1)

            print(p1.name + " used Leer!")
            sleep(1)
            print(p2.name + "'s defence fell!")
            sleep(1)

   

def Chosen1(p1):
    print("Wild Pokémon found!")
    sleep(1)
    name = random.choice(enemy_pokemon_list)
    print("Fighting: " + name + "!")
    p2 = Pokemon(name, 2, 0, 10, 10, 6, 40, 3)
    print(p1.stats())
    print("")
    print(p2.stats())

    BattleScreen(p1, p2)

def Chosen2(p1):
    p1.hp = p1.maxhp
    os.system("clear")
    sleep(1)
    print("Pokémon healed!")
    sleep(1)
    print(p1.name + " is now at full health!")
    sleep(1)
    os.system("clear")

while(True):
    menu = Menu()
    chosen = menu.choice()

    os.system("clear")

    if(chosen == 1):
        Chosen1(p1)

    elif(chosen == 2):
        Chosen2(p1)

    elif(chosen == 3):
        sys.exit()
