#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

class Heap:
    def __init__(self):
        self.data = {}
        self.max_size = 20
        self.first = 1
        self.last = 0

    def empty(self) -> bool:
        return self.last == 0

    def full(self) -> bool:
        return (self.first == 1 and self.last == self.max_size) or (self.last > 0 and self.last == self.first - 1)

    def push(self, value) -> bool:
        if not self.full():
            if(self.last < self.max_size):
                self.last += 1
            else:
                self.last = 1
            self.data[self.last] = value
            return True
        else:
            return False

    def pull(self):
        if not self.empty():
            value = self.data[self.first]
            if(self.first == self.last):
                self.first = 1
                self.last = 0
            else:
                if self.first < self.max_size:
                    self.first += 1
                else:
                    self.first = 1
            return value
        else:
            return False


def main():
    heap = Heap()
    heap.push(5)
    heap.push(10)
    heap.push(11)


    print(heap.pull())
    print(heap.pull())
    print(heap.pull())
    print(heap.pull())

    heap.push(74)
    heap.push(10)
    print(heap.pull())

if __name__ == '__main__':
    main()
