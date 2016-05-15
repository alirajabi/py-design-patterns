#!/usr/bin/python
# -*- coding : utf-8 -*-


# Director
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_phone()
        self.builder.build_screen()
        self.builder.build_os()

    def get_phone(self):
        return self.builder.phone


# Abstract Builder
class Builder(object):
    def __init__(self):
        self.phone = None

    def new_phone(self):
        self.phone = Phone()

    def build_screen(self):
        raise NotImplementedError

    def build_os(self):
        raise NotImplementedError


# Concrete Builder
class ApplePhone(Builder):
    def build_screen(self):
        self.phone.screen = 'Retina Touch Screen 4.7 Inch!'

    def build_os(self):
        self.phone.os = 'IOS'


class SamsungPhone(Builder):
    def build_screen(self):
        self.phone.screen = 'Touch Screen 5.2 Inch!'

    def build_os(self):
        self.phone.os = 'Android'


# Product
class Phone(object):
    def __init__(self):
        self.screen = None
        self.os = None

    def __repr__(self):
        return 'Screen: {0.screen} | OS: {0.os}'.format(self)


# Client
if __name__ == "__main__":
    director = Director()
    director.builder = ApplePhone()
    director.construct_building()
    iphone = director.get_phone()
    print(iphone)
    director.builder = SamsungPhone()
    director.construct_building()
    samsung = director.get_phone()
    print(samsung)
