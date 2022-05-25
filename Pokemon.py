#!/usr/bin/python3
import sys
from numpy import random


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

    def showpoints(self, other):
        while (self.health > 0) and (other.health > 0):
            # imprimir los puntos de salud de cada pokemon
            print(f"\n{self.name}\tPoints of health\t{self.health}")
            print(f"\n{other.name}\tPoints of health\t{other.health}")

        self.attack(other)
        self.printP1()
        self.printP2(other)


    def showdown(self, other):

        print("-----POKEMONE BATTLE-----")

        print("Name: ", self.name)
        print("Number: ", self.number)
        print("Type: ", self.typeP)
        print("Color: ", self.color)
        print("Height: ", self.height)
        print("Attack: ", self.attack)
        print("Weight: ", self.weight)
        print("HP: ", self.health)

        print("-----VS!!!-----")

        print("Name: ", other.name)
        print("Type: ", other.typeP)
        print("Color: ", other.color)
        print("Weight: ", other.weight)
        print("Health: ", other.health)
        print("Attack: ", other.attack)
        print("Number: ", other.number)
        print("Height: ", other.height)

        while (self.health > 0) and (other.health > 0):
            print(self.name, " is attacking to ", other.name)
            
            rng_damage = self.attack * random.randinit(5)
            other.health -= rng_damage
            print(self.name, " did ", rng_damage, " to ", other.name)
            
            print("the health of ", other.name, " has been reduced to:", other.health)

            if other.health <= 0:
                print("\n..." + other.name + ' fainted. :(')
                break
            print("now is the turn of ", other.name)

            print(other.name, " is attacking to ", self.name)
           
            rng_damage = other.attack * random.randinit(5)
            self.health -= rng_damage
            print(other.name, " did ", rng_damage, " to ", self.name)
            
            print("the health of ", self.name, " has been reduced to:", self.health)

            if self.health <= 0:
                print("\n..." + self.name + ' fainted. :(')
                break

if __name__ == '__main__':
    piph = input("insert the attack amount between 5 or 1 \n")
    piplup = pokemon("Piplup", 389, 0.4, 5.2, piph, "Water", "Blue", 20)

    chart = input("insert the attack amount between 5 or 1 \n")
    charmander = pokemon("Charmander", 4, 0.6, 8.5, chart, "Fire", "Red", 20)

    piplup.showdown(charmander)