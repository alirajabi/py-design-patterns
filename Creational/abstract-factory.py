#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# Stuff that our factory makes

class DogFood(object):
    def __str__(self):
        return 'Dog Food'


class CatFood(object):
    def __str__(self):
        return 'Cat Food'


class Dog(object):
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return DogFood()


class CatFactory(object):
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


if __name__ == "__main__":

    for i in range(3):
        shop = PetShop(random.choice([DogFactory, CatFactory])())
        shop.show_pet()
