# postfix_evaluator.py
from stack import Stack

class PostfixEvaluator:
    def __init__(self):
        self.stack = Stack()

    def evaluate(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))
            elif token.replace('.', '', 1).isdigit():  # handle floats
                self.stack.push(float(token))
            else:  # operator
                if self.stack.size() < 2:
                    raise ValueError("Invalid postfix expression")
                b = self.stack.pop()
                a = self.stack.pop()
                result = self.apply_operator(a, b, token)
                self.stack.push(result)
        if self.stack.size() != 1:
            raise ValueError("Invalid postfix expression")
        return self.stack.pop()

    def apply_operator(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        else:
            raise ValueError(f"Unknown operator: {operator}")
