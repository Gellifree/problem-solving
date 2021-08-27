#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

class Stack:

    def __init__(self):
        self.stack_pointer = -1
        self.max_size = 20
        self.data = {}

    def empty(self) -> bool:
        return self.stack_pointer < 0

    def full(self) -> bool:
        return self.stack_pointer == self.max_size

    def push(self, value) -> bool:
        if not self.full():
            self.stack_pointer += 1
            self.data[self.stack_pointer] = value
            return True
        else:
            return False

    def pull(self):
        if not self.empty():
            value = self.data[self.stack_pointer]
            del self.data[self.stack_pointer]
            self.stack_pointer -= 1
            return value
        else:
            return False



def main():
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.push(1)
    print(stack.data)
    print(stack.pull())
    print(stack.pull())
    print(stack.data)

if __name__ == '__main__':
    main()
