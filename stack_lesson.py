class Stack:
    def __init__(self):
        self.stack = list()
        self.min_element_stack = list()
        self.max_element_stack = list()

    def push(self, element):
        if self.size() == 0:
            self.min_element_stack.append(element)
            self.max_element_stack.append(element)
        else:
            self.min_element_stack.append(min(self.min_element_stack[self.size() - 1], element))
            self.max_element_stack.append(max(self.max_element_stack[self.size() - 1], element))

        self.stack.append(element)

    def pop(self):

        if self.is_empty():
            raise ValueError('Empty stack')
        self.min_element_stack.pop()
        self.max_element_stack.pop()
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

    def clear(self):
        self.stack.clear()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def minimum(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self.min_element_stack[self.size() - 1]

    def maximum(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self.max_element_stack[self.size() - 1]

    def summ_all(self):
        return sum(self.stack)



if __name__ == 'main':
    print('hmm')
