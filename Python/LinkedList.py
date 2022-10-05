class Node:
    def __init__(self, data):
        self.element = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.size = 0
    
    def is_empty(self):
        return self.head_node == None

    def insert_at_head(self, data):
        N = Node(data)
        N.next_node = self.head_node
        self.head_node = N
        self.size += 1

    def insert_at_tail(self, data):
        if self.is_empty():
            self.insert_at_head(data)
        else:
            N = Node(data)
            N.next_node = None
            temp = self.head_node
            while temp.next_node is not None:
                temp = temp.next_node 
            temp.next_node = N
            N.next_node = None 
            self.size += 1
        return 

    def remove_duplicates(self):
        unique = []
        curr = self.head_node
        prev = None
        if self.head_node is not None:
            while curr.next_node:
                if curr.element in unique:
                    prev.next_node = curr.next_node
                    self.size -= 1
                else:
                    unique.append(curr.element)
                    prev = curr    
                curr = curr.next_node
            if curr.element in unique:
                self.size -= 1
                prev.next_node = None
        

    def print_list(self):
        if self.head_node is None:
            print("None")
        else:
            temp = self.head_node
            while temp.next_node is not None:
                print(temp.element, end = " -> ")
                temp = temp.next_node
            print(temp.element, "-> None")
        print("Size:", self.size)

    def delete_head(self):
        node = self.head_node
        if node is not None:
            self.head_node = node.next_node
            node.next_node = None
            self.size -= 1
        return
    
    def delete_element(self, val):
        prev = None
        curr = self.head_node
        if self.head_node.element == val:
            self.head_node = curr.next_node
            del curr
            self.size -= 1
            curr = self.head_node
        if curr is not None:
            while curr.next_node:
                if curr.element == val:
                    prev.next_node = curr.next_node
                    self.size -= 1  
                else:
                    prev = curr
                curr = curr.next_node
            if curr.element == val:
                prev.next_node = None
                del curr
                self.size -= 1
        return

    def delete_tail(self):
        curr = self.head_node
        prev = None
        while curr.next_node:
            prev = curr
            curr = curr.next_node
        prev.next_node = None
        del curr
        self.size -= 1
   
    def reverse(self):
        prev = None
        curr = self.head_node
        while curr:
            next = curr.next_node
            curr.next_node = prev
            prev, curr = curr, next
        self.head_node = prev    

class __main__:
    import random    
    linkedlist = LinkedList()
    choice = 1
    while choice:
        linkedlist.insert_at_head(random.randint(1, 10))
        choice = int(input("Element inserted. Insert more? No(0)   Yes(1):"))
    linkedlist.print_list()
    linkedlist.remove_duplicates()
    linkedlist.print_list()