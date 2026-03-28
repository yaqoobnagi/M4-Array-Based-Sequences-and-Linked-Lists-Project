# infix_converter.py
from stack import Stack

class InfixToPostfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+':1, '-':1, '*':2, '/':2}

    def convert(self, expression):
        output = []
        tokens = expression.split()
        for token in tokens:
            if token.isalnum():  # operand
                output.append(token)
            elif token == '(':
                self.stack.push(token)
            elif token == ')':
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    output.append(self.stack.pop())
                self.stack.pop()  # remove '('
            else:  # operator
                while (not self.stack.is_empty() and
                       self.stack.peek() != '(' and
                       self.precedence[token] <= self.precedence[self.stack.peek()]):
                    output.append(self.stack.pop())
                self.stack.push(token)
        while not self.stack.is_empty():
            output.append(self.stack.pop())
        return ' '.join(output)
