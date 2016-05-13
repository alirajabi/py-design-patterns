#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


dog = get_pet("dog")

print(dog.speak())

cat = get_pet("cat")

print(cat.speak())

# wrong_name = get_pet("dogg")
