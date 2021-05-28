class Deque:
    def __init__(self, *items):
        self.count = 0
        self.first = self.last = None
        for item in items:
            self.pushBack(item)

    def pushBack(self, item):
        temp = self.last
        if temp:
            self.last.next = self.last = Node(item)
            self.last.prior = temp
        else:
            self.first = self.last = Node(item)
        self.count += 1
        return self, item

    def pushFront(self, item):
        temp = self.first
        if temp:
            self.first.prior = self.first = Node(item)
            self.first.next = temp
        else:
            self.first = self.last = Node(item)
        self.count += 1
        return self, item

    def popBack(self):
        temp = self.last
        if not temp:
            return self, None
        self.last = self.last.prior
        if self.last:
            self.last.next = None
        self.count -= 1
        if not self:
            self.first = None
        return temp.element

    def popFront(self):
        temp = self.first
        if not temp:
            if not temp:
                return self, None
        self.first = self.first.next
        if self.first:
            self.first.prior = None
        self.count -= 1
        if not self:
            self.last = None
        return temp.element

    def back(self):
        return self.last.element

    def front(self):
        return self.first.element

    def size(self):
        return self.count

    def __str__(self):
        return 'DQ({})'.format(','.join(map(repr, self)))

    def __repr__(self):
        return repr(str(self))

    def __iter__(self):
        if not self.first:
            return iter('')
        current = self.first
        while current.next:
            yield current.element
            current = current.next
        yield current.element

    def __len__(self):
        return self.count

    def __bool__(self):
        return bool(len(self))

    def __add__(self, other):
        return DQ(self, other)


class Node:
    def __init__(self, element=None):
        self.next = self.prior = None
        self.element = element

    def __str__(self):
        return str(self.element)

    def __repr__(self):
        return 'Node({})'.format(repr(self.element))


import unittest


class test(unittest.TestCase):

    # test with a list sorted in ascending order
    def test(self):
        list = Deque()
        list.pushFront(2)
        list.pushFront(1)
        list.pushBack(3)

        assert (list.popFront() == 1)
        assert (list.popBack() == 3)
        assert (list.back() == list.front())

        assert (list.back() == 2)


if __name__ == '__main__':
    unittest.main()
