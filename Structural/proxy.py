#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class SalesManager(object):
    def talk(self):
        print("Sales Manager ready to talk")
    def meeting(self):
        print("Sales Manager ready to meet")



class Proxy(object):
    def __init__(self):
        self.busy = 'No'
        self.sales = None
        self.is_boss = False

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")


class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(2)
        print("This Sales Manager will not talk to you whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

    # source: https://github.com/faif/python-patterns/blob/master/proxy.py
