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
        return self.first > self.last

    def full(self) -> bool:
        return self.last == self.max_size

    def push(self, value) -> bool:
        if not self.full():
            self.last += 1
            self.data[self.last] = value
            return True
        else:
            return False

    def pull(self):
        if not self.empty():
            value = self.data[self.first]
            del self.data[self.first]
            self.first += 1
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

if __name__ == '__main__':
    main()
