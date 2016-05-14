#!/usr/bin/env python
import time
import threading

class Logger():

    def __init__(self):
        self.log_level = 0
        self.observers = dict()

    def log(self, logMessage):
        for name, lis in self.observers.items():
            print("list name:", name)
            for observer, level in lis:
                if self.log_level >= level:
                    if name == "async":
                        threading.Thread(target = observer.log, args=(logMessage,)).start()
                    else:
                        observer.log(logMessage)
            
        print()

    def register_logger(self, log_backend, level):
        self.__add_log_backend_to_observers_list(log_backend, level, 'sync')

    def register_async_logger(self, log_backend, level):
        self.__add_log_backend_to_observers_list(log_backend, level, 'async')
    
    def __add_log_backend_to_observers_list(self, log_backend, level, observers_list_name):
        if observers_list_name not in self.observers:
            self.observers[observers_list_name] = []
        self.observers[observers_list_name].append((log_backend, level))

    def set_log_level(self, log_level):
        self.log_level = log_level

class LogBackend():
    def log(self, msg):
        print(msg)

class NormalLogger(LogBackend):
    def log(self, msg):
        print("normal logger logging:", msg)

class DecoratedLogger(LogBackend):
    def __init__(self, opening, closing):
        self.opening = opening
        self.closing = closing

    def log(self, msg):
        print(self.opening, msg, self.closing)

def main():
    logger = Logger()
    logger.set_log_level(1)
    logger.register_logger(NormalLogger(), 1)
    logger.register_async_logger(DecoratedLogger('[-', '-]'), 2)
    
    logger.log(":D")
    logger.log("segmentation fault! :D")

    logger.set_log_level(2)

    logger.log("undefined behavior")
    logger.log("Another log")

    time.sleep(1)


if __name__ == '__main__':
    main()
