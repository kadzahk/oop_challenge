#!/usr/bin/python3
import sys
import random
import time


class pokemon:

    def __init__(self, name, number, height, weight, attack, typeP, color, health = 20):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.attack = attack
        self.typeP = typeP
        self.color = color
        self.health = health


    def showdown(self, other):

        print("-----POKEMONE BATTLE-----")
        time.sleep(1.5)

        print("Name: ", self.name)
        print("Number: ", self.number)
        print("Type: ", self.typeP)
        print("Color: ", self.color)
        print("Height: ", self.height)
        print("Attack: ", self.attack)
        print("Weight: ", self.weight)
        print("HP: ", self.health)
        time.sleep(1.5)
        print("-----VS!!!-----")
        time.sleep(1.5)
        print("Name: ", other.name)
        print("Type: ", other.typeP)
        print("Color: ", other.color)
        print("Weight: ", other.weight)
        print("Health: ", other.health)
        print("Attack: ", other.attack)
        print("Number: ", other.number)
        print("Height: ", other.height)

        while (self.health > 0) and (other.health > 0):
            time.sleep(1.5)
            print(self.name, " is attacking to ", other.name)
            time.sleep(1.5)
            rng_damage1 = self.attack * random.randint(0,5)
            other.health -= rng_damage1
            print(self.name, " did ", rng_damage1, " to ", other.name)
            time.sleep(1.5)
            print("the health of ", other.name, " has been reduced to:", other.health)

            if other.health <= 0:
                time.sleep(2)
                print("\n..." + other.name + ' fainted. :(')
                break
            time.sleep(1.5)
            print("now is the turn of ", other.name)
            time.sleep(1.5)
            print(other.name, " is attacking to ", self.name)
           
            rng_damage2 = other.attack * random.randint(0,5)
            self.health -= rng_damage2
            time.sleep(1.5)
            print(other.name, " did ", rng_damage2, " to ", self.name)
            time.sleep(1.5)
            print("the health of ", self.name, " has been reduced to:", self.health)

            if self.health <= 0:
                time.sleep(2)
                print("\n..." + self.name + ' fainted. :(')
                break

if __name__ == '__main__':
    piph = int(input("insert the attack amount of piplup between 5 or 1 \n"))
    piplup = pokemon("Piplup", 389, 0.4, 5.2, piph, "Water", "Blue", 20)

    chart = int(input("insert the attack amount of charmander between 5 or 1 \n"))
    charmander = pokemon("Charmander", 4, 0.6, 8.5, chart, "Fire", "Red", 20)

    piplup.showdown(charmander)