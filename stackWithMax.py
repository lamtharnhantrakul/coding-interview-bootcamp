from collections import namedtuple

class Stack:
    ElemCache = namedtuple('ElemCache',('element','max'))

    def __init__(self):
        self._elements = []

    def empty(self):
        return len(self._elements) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack!')
        return self._elements[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('max(): empty stack!')
        return self._elements.pop().element

    def push(self, x):
        self._elements.append(self.ElemCache(x, x if self.empty() else max(x,self.max())))

stack = Stack()
stack.push(1)
print(stack.max())
stack.push(3)
print(stack.max())
stack.push(2)
print(stack.max())
stack.push(5)
print(stack.max())
stack.push(1)
print(stack.max())
