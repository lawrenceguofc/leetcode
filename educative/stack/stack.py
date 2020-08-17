class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def get_stack(self):
        return self.items



def main():
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    print(myStack.get_stack())
    myStack.push("C")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.get_stack())

if __name__ == "__main__":
    main()