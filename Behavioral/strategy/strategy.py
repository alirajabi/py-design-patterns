#!/usr/bin/env python

class Animal():
    def __init__(self, fly_behavior, running_behavior):
        self.fly_behavior = fly_behavior
        self.running_behavior = running_behavior

    def fly(self):
        return self.fly_behavior.invoke()

    def run(self):
        return self.running_behavior.invoke()

class RunningBehavior():
    def invoke(self):
        return 'default running behavior'
    
class FlyingBehavior():
    def invoke(self):
        return 'default flying behavior'

class SprintBehavior():
    def invoke(self):
        return 'sprint behavior: fast but energy consuming'

class WalkingBehavior():
    def invoke(self):
        return 'walk behavior: slow but energy preserving'

class UnableToFlyBehavior():
    def invoke(self):
        return 'Not able to fly'

class LowAltitudeFlyingBehavior():
    def invoke(self):
        return 'Flying low: dangerous but less visible'
        

def main():
    shotormorgh = Animal(UnableToFlyBehavior(), SprintBehavior())
    oghab = Animal(LowAltitudeFlyingBehavior(), WalkingBehavior())

    print('shotormorgh tries to fly: ', shotormorgh.fly())
    print('shotormorgh tries to run: ', shotormorgh.run())
    print('')
    print('oghab tries to fly: ', oghab.fly())
    print('oghab tries to run: ', oghab.run())
   
    print('')

    print('oghab gets hit')
    oghab.fly_behavior = UnableToFlyBehavior()
    print('oghab tries to fly: ', oghab.fly())
    print('oghab tries to run: ', oghab.run())

# output:
# shotormorgh tries to fly:  Not able to fly
# shotormorgh tries to run:  sprint behavior: fast but energy consuming
# 
# oghab tries to fly:  Flying low: dangerous but less visible
# oghab tries to run:  walk behavior: slow but energy preserving
# 
# oghab gets hit
# oghab tries to fly:  Not able to fly
# oghab tries to run:  walk behavior: slow but energy preserving


if __name__ == '__main__':
    main()


