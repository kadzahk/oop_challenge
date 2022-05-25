import sys

import numpy as np


class pokemon:

    def __init__(self, name, number, height, weight, attack, typeP, color, health):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.attack = attack
        self.typeP = typeP
        self.color = color
        self.health = health

# names of pokemons
def name(self, other):
    self.name = "piplup"
    other.name = "charmander"

# Here is the  height
def height(self, other):
    self.height = 0.4
    other.height = 0.6

# Here are the types
def typep(self, other):
    self.typep = "Water"
    other.typep = "Fire"

# colors of pokemons
def color(self, other):
    self.color = "blue"
    other.color = "red"

# here is the weight of pokemons
def weight (self, other):
    self.weight = 5.2
    other.weight = 8.5

# here us the health
def health(self, other):
    self.health = 15
    other.health = 15

# here is number of identification
def number(self, other):
    self.number = 3-9-3
    self.other = 0-0-4



""" Aqui va el ataque y resta de vida   """

def attack(self, other):
    if self.typeP == other.typeP:
        try:
            self.health -= other.attack
            other.health -= self.attack
        except:
            pass


def printP1 (self):

    print("Name: " + self.name)
    print("Number: " + self.number)
    print("Type: " + self.typeP)
    print("Color: " + self.color)
    print("Height: " + self.height)
    print("Attack: " + self.attack)
    print("Weight: " + self.weight)
    print("HP: " + self.health)

def printP2(other):

    print("Name: " + other.name)
    print("Type: " + other.typep)
    print("Color: " + other.color)
    print("Weight: " + other.weight)
    print("Health: " + other.health)
    print("Attack: " + other.attack)
    print("Number: " + other.number)
    print("Height: " + other.height)
