#!/usr/bin/env python
# -*- coding: utf-8 -*-


# python 3.4
# class Animal(Enum):
#    DOG = 1
#    CAT = 2


class Animal:
    Dog = 1
    Cat = 2


class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


class PetShop:
    def __init__(self):
        pass

    @staticmethod
    def get_pet(animal):
        """The factory method"""
        if animal == Animal.Dog:
            return Dog("Hope")
        if animal == Animal.Cat:
            return Cat("Peace")
        assert 0, "Bad pet creation: " + type


d = PetShop.get_pet(Animal.Dog)

print(d.speak())

c = PetShop.get_pet(Animal.Cat)

print(c.speak())

# print (PetShop.get_pet('Parrot'))
