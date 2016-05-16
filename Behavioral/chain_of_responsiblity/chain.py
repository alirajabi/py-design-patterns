#!/usr/bin/env python


class Handler(object):

    def __init__(self):
        self.next = None

    def set_next(self, next_handler):
        self.next = next_handler

    def handle(self, request):
        if self.can_handle(request):
            return self._handle(request)
        elif self.next is not None:
            return self.next.handle(request)
        else:
            return None

    def _handle(self, request):
        return None


class CoinRequest(object):

    def __init__(self, size):
        self._size = size

    def size(self):
        return self._size


class CoinSorter(Handler):

    def __init__(self, min_coin_size_to_catch):
        super().__init__()
        self.min_coin_size = min_coin_size_to_catch

    def can_handle(self, request):
        return self.min_coin_size <= request.size()

    def _handle(self, request):
        return '{} coin sorter handles {} coin\
'.format(self.min_coin_size, request.size())


def main():
    c10 = CoinSorter(10)
    c15 = CoinSorter(15)
    c20 = CoinSorter(20)

    c20.set_next(c15)
    c15.set_next(c10)

    coins = [CoinRequest(x) for x in range(0, 25, 3)]

    for coin in coins:
        print(coin.size(), ':', c20.handle(coin))
    print()

    c17 = CoinSorter(17)
    c17.set_next(c15)
    c20.set_next(c17)

    for coin in coins:
        print(coin.size(), ':', c20.handle(coin))


if __name__ == '__main__':
    main()

# 0 : None
# 3 : None
# 6 : None
# 9 : None
# 12 : 10 coin sorter handles 12 coin
# 15 : 15 coin sorter handles 15 coin
# 18 : 15 coin sorter handles 18 coin
# 21 : 20 coin sorter handles 21 coin
# 24 : 20 coin sorter handles 24 coin
#
# 0 : None
# 3 : None
# 6 : None
# 9 : None
# 12 : 10 coin sorter handles 12 coin
# 15 : 15 coin sorter handles 15 coin
# 18 : 17 coin sorter handles 18 coin
# 21 : 20 coin sorter handles 21 coin
# 24 : 20 coin sorter handles 24 coin
