import unittest

from stack_lesson import Stack


def calculate(s):
    stack = Stack()
    for el in s.split(' '):
        if el == '+':
            stack.push(stack.pop() + stack.pop())
        elif el == '*':
            stack.push(stack.pop() * stack.pop())
        elif el == '-':
            _to = stack.pop()
            _from = stack.pop()
            stack.push(_from - _to)
        elif el == '/':
            _to = stack.pop()
            _from = stack.pop()
            stack.push(_from / _to)
        else:
            stack.push(int(el))
    return stack.pop()


class exampleTest(unittest.TestCase):
    def test(self):
        assert (calculate("2 2 2 + *") == 8)


if __name__ == '__main__':
    unittest.main()
