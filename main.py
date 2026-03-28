# main.py
from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

# ---- Postfix Evaluation ----
postfix = ["5 3 +",
           "8 2 - 3 +",
           "5 3 8 * +",
           "6 2 / 3 +",
           "5 8 + 3 -",
           "5 3 + 8 *",
           "8 2 3 * + 6 -",
           "5 3 8 * + 2 /",
           "8 2 + 3 6 * -",
           "5 3 + 8 2 / -"]

evaluator = PostfixEvaluator()
print("----- Postfix Evaluator -----")
for expr in postfix:
    result = evaluator.evaluate(expr)
    print(f"[{expr}] = {result}")

# ---- Infix to Postfix ----
infix = ["A + B",
         "A + B * C",
         "( A + B ) * C",
         "A * B + C / D",
         "( A + B ) * ( C - D )",
         "A + B * C - D / E",
         "A * ( B + C ) / D",
         "( A + B * C ) / ( D - E )",
         "A + ( B - C ) * D",
         "( A + B * ( C - D ) ) / E"]

converter = InfixToPostfixConverter()
print("\n----- Infix to Postfix Converter -----")
for expr in infix:
    result = converter.convert(expr)
    print(f"[{expr}] -> [{result}]")

# ---- Singly Linked List Tests ----
values = [10, 20, 30, 40, 50]

sll = SinglyLinkedList()
print("\n---- Build a forward list ----")
sll.build_list_forward(values)
sll.display()
sll.delete_first()
print("Delete the first node:", end=" ")
sll.display()
sll.delete_last()
print("Delete the last node:", end=" ")
sll.display()
sll.delete_interior(30)
print("Delete the interior node:", end=" ")
sll.display()

print("\n---- Build a backward list ----")
sll.build_list_backward(values)
sll.display()
sll.delete_first()
print("Delete the first node:", end=" ")
sll.display()
sll.delete_last()
print("Delete the last node:", end=" ")
sll.display()
sll.delete_interior(30)
print("Delete the interior node:", end=" ")
sll.display()

print("\n---- Non-recursive reverse print test ----")
sll.build_list_forward(values)
sll.display()
sll.display_reverse_nr()

print("\n---- Remove all test ----")
values2 = [1,2,4,6,1,3,6]
sll.build_list_forward(values2)
sll.display()
sll.remove_all(1)
print("Removing 1 and all duplicates:", end=" ")
sll.display()
s
