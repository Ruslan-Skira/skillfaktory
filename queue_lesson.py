class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def isEmpty(self):
        if self.instack and self.outstack:
            return None

    def push(self, element):
        self.instack.append(element)

    def pop(self):
        self.isEmpty()

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack.pop()
        else:
            return self.outstack.pop()


q = Queue()
q.push(1)
q.push(2)
q.push(3)

import unittest


class queueTest(unittest.TestCase):

    def test_ascending_input(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        assert (q.pop() == 1)
        assert (q.pop() == 2)
        assert (q.pop() == 3)
