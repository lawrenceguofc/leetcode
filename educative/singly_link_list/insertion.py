
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    # insert into the first place
    def prepend(self,data):
        newNode = Node(data)
        last_node = self.head
        newNode.next = last_node
        self.head = newNode
    # insert after certain node
    def insert_after_node(self,prev_node,data):
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode

                


def main():
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.prepend('E')
    llist.print_list() 
    # insert after certain node
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.insert_after_node(llist.head.next, "D")
    llist.print_list()  

if __name__ == "__main__":
    main()