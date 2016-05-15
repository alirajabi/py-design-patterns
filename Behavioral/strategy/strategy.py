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

class SprintBehavior(RunningBehavior):
    def invoke(self):
        return 'sprint behavior: fast but energy consuming'

class WalkingBehavior(RunningBehavior):
    def invoke(self):
        return 'walk behavior: slow but energy preserving'

class UnableToFlyBehavior(FlyingBehavior):
    def invoke(self):
        return 'Not able to fly'

class LowAltitudeFlyingBehavior(FlyingBehavior):
    def invoke(self):
        return 'Flying low: dangerous but less visible'
        

def main():
    bird2 = Animal(UnableToFlyBehavior(), SprintBehavior())
    bird1 = Animal(LowAltitudeFlyingBehavior(), WalkingBehavior())

    print('bird2 tries to fly: ', bird2.fly())
    print('bird2 tries to run: ', bird2.run())
    print('')
    print('bird1 tries to fly: ', bird1.fly())
    print('bird1 tries to run: ', bird1.run())
   
    print('')

    print('bird1 gets hit')
    bird1.fly_behavior = UnableToFlyBehavior()
    print('bird1 tries to fly: ', bird1.fly())
    print('bird1 tries to run: ', bird1.run())

# output:
# bird2 tries to fly:  Not able to fly
# bird2 tries to run:  sprint behavior: fast but energy consuming
# 
# bird1 tries to fly:  Flying low: dangerous but less visible
# bird1 tries to run:  walk behavior: slow but energy preserving
# 
# bird1 gets hit
# bird1 tries to fly:  Not able to fly
# bird1 tries to run:  walk behavior: slow but energy preserving


if __name__ == '__main__':
    main()


