
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
    # delete a node by value
    def delete_node(self,key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None
    # iterative implementation
    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    """# recursive
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + len_recursive(node.next)
    """
    # swap nodes
    def swap_nodes(self,key_1,key_2):
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None 
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next,curr_1.next
    # reverse a linkedlist
    def reverse_llist(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur = nxt
        self.head = prev



         


                


def main():
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.prepend('E')
    llist.print_list() 
    # insert after certain node
    """     
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.insert_after_node(llist.head.next, "D")
     """
    #llist.print_list()  
    # delete 
    llist.delete_node("B")
    llist.delete_node("E")
    llist.print_list()

    # swap nodes
    llist.swap_nodes('A','C')
    llist.print_list()

if __name__ == "__main__":
    main()