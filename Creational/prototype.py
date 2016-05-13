#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class Car(object):
    def __init__(self):
        self.color = 'red'
        self.engine = '1.6'
        self.name = 'BMW'

    def clone(self, **attr):
        """Clone a prototype and update inner attributes dictionary"""
        # important
        obj = copy.deepcopy(self)
        obj.__dict__.update(attr)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    @property
    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


if __name__ == '__main__':
    dispatcher = PrototypeDispatcher()
    car = Car()

    mbw_x1 = car.clone()
    mbw_x1_plus = car.clone(color='white', engine='1.8')
    mbw_taxi = car.clone(color='yellow', is_taxi=True)

    dispatcher.register_object('bmw_x1', mbw_x1)
    dispatcher.register_object('mbw_x1_plus', mbw_x1_plus)
    dispatcher.register_object('mbw_taxi', mbw_taxi)

    if id(dispatcher.get_objects.get('bmw_x1').color) == id(dispatcher.get_objects.get('mbw_x1_plus').color):
        print "Same"
    else:
        print "Different car obj"

    print([{'Name': name, 'Engine': car.engine, 'Color': car.color} for name, car in dispatcher.get_objects.items()])
