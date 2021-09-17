class node :
    def __init__(self, data) :
        self.data = data 
        self.next = None 

class LinkedList : 
    def __init__(self) : 
        self.head = None 

    def reverse(self) : 
        prev = None 
        current = self.head 
        while(current != None):
            next = current.next 
            current.next = prev 
            prev = current 
            current = next 
        self.head = prev

    def push(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head 
        while(temp):
            print (temp.data)
            temp = temp.next 


llist = LinkedList()
llist.push(10)
llist.push(34)
llist.push(43)
llist.push(51)

print ("Given Linked List")
llist.printList()
llist.reverse()
print("\n Reversed Linked List ")
llist.printList()