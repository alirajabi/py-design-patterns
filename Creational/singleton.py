#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    test_1=Singleton()
    test_2=Singleton()
    if(id(test_1)==id(test_2)):
        print "Same"
    else:
        print "Different"

### OUTPUT ###
# Same
