#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os


# Tároló elem a folyadékhoz
class Container():
    def __init__(self, size, value):
        self.size = size
        self.value = value
        self.valuemark = '▣'
        self.sizemark = '▢'
        self.counter = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if (value > 10):
            raise ValueError("Tíznél nagyobb tároló nem használható!")
        self._size = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if(value > self.size):
            raise ValueError("A tartalmazott mennyiség, nem lehet nagyobb, mint a méret!")
        self._value = value

    def print(self):
        self.counter = 0
        for i in range(self.value):
            print(self.valuemark, end="")
            self.counter += 1
        for i in range(self.counter, self.size):
            print(self.sizemark, end="")
        print()

    def fill(self, value):
        self.value += value

    def loadInto(self, Container):
        freeSpace = Container.size - Container.value

        if(freeSpace > self.value):
            Container.value += self.value
            self.value -= self.value
        else:
            Container.value += freeSpace
            self.value -= freeSpace

# gyűjtő osztály
class Shelf():
    def __init__(self, ContainerList):
        self.ContainerList = ContainerList

    def print(self):
        for i in range(len(self.ContainerList)):
            self.ContainerList[i].print()


def clear():
    os.system("clear")

containers = [Container(3,1), Container(5,0), Container(8,8)]

def main():
    print("Kezdőállapot")

    sh = Shelf(containers)
    sh.print()
    sh.ContainerList[0].loadInto(sh.ContainerList[0])
    print("--")
    sh.print()

if __name__ == '__main__':
    main()
