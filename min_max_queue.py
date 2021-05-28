import unittest

# from queue_lesson import Queue
from stack_lesson import Stack


class MyQueue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def isEmpty(self):
        if not self.instack.is_empty() and not self.outstack.is_empty():
            return None

    def push(self, element):
        self.instack.push(element)

    def pop(self):
        self.isEmpty()

        if self.outstack.is_empty():
            while not self.instack.is_empty():
                self.outstack.push(self.instack.pop())
            return self.outstack.pop()
        else:
            return self.outstack.pop()

    def min(self):
        if self.instack.is_empty():
            return self.outstack.minimum()
        return self.instack.minimum()

    def max(self):
        if self.instack.is_empty():
            return self.outstack.maximum()
        return self.instack.maximum()

    def sum(self):
        if self.instack.is_empty():
            return self.outstack.summ_all()
        return self.instack.summ_all()


q = MyQueue();
q.push(1);
q.push(2);
q.push(3);
q.pop();
print(q.min() == 2);
print(q.max() == 3);
print(q.sum == 5);
