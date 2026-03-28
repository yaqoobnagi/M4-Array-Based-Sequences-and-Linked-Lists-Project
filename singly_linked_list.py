# singly_linked_list.py

from stack import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def build_list_forward(self, values):
        self.head = None
        for value in values:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

    def build_list_backward(self, values):
        self.head = None
        for value in values:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_interior(self, value):
        if self.head is None or self.head.data == value:
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def remove_all(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        result = "Head -> "
        current = self.head
        while current:
            result += f"{current.data} -> "
            current = current.next
        result += "None"
        print(result)

    def display_reverse_nr(self):
        stack = Stack()
        current = self.head
        while current:
            stack.push(current.data)
            current = current.next
        result = "None <- "
        while not stack.is_empty():
            result += f"{stack.pop()} <- "
        result += "Head"
        print(result)
