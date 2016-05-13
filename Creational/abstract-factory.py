#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# Stuff that our factory makes

class DogFood:
    def __init__(self):
        pass

    def __str__(self):
        return 'Dog Food'


class CatFood:
    def __init__(self):
        pass

    def __str__(self):
        return 'Cat Food'


class Dog:
    def __init__(self):
        pass

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class Cat:
    def __init__(self):
        pass

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:
    def __init__(self):
        pass

    def get_pet(self):
        return Dog()

    def get_food(self):
        return DogFood()


class CatFactory:
    def __init__(self):
        pass

    def get_pet(self):
        return Cat()

    def get_food(self):
        return CatFood()


class PetShop:
    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


for i in range(3):
    shop = PetShop(random.choice([DogFactory, CatFactory])())
    shop.show_pet()
