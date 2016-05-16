#!/usr/bin/env python


class SystemdUnit():

    def start(self):
        self.on_pre_start()
        self.on_start()

    def stop(self):
        self.on_stop()
        self.on_post_stop()

    def on_pre_start(self):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_post_stop(self):
        pass


class MyUnit(SystemdUnit):

    def __init__(self, *args):
        self.start_args = args

    def on_pre_start(self):
        print('setting up environment ...')

    def on_start(self):
        print('running the executable with args:', *self.start_args)

    def on_stop(self):
        print('stopping ...')

    def on_post_stop(self):
        print('cleaning up')


def main():
    unit = MyUnit('args', 'to', 'executable')
    unit.start()
    unit.stop()


if __name__ == '__main__':
    main()
