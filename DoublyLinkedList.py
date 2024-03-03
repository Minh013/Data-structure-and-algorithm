# Homework: Delete the element at the end

# Python code for doubly linked list
class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
# this link always point to first Link
head = None
# this link always point to last Link
last = None
current = None
# is list empty
def is_empty():
    return head is None


#display the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = head
        while ptr is not None:
            print(f"({ptr.key},{ptr.data})")
            ptr = ptr.next
    #insert link at the first location
    def insert_first(self, key, data):
        global head, last
        #create a link
        link = Node(data, key)
        if is_empty():
            #make it the last link
            last = link
        else:
            #update first prev link
            head.prev = link
        #point it to old first link
        link.next = head
        #point first to new first link
        head = link

    def delete_first(self):
        global head, last
        link = head
        if head.next == None:
            last = None
        else:
            head.next.prev = None
        head = head.next
        return link

    def delete_at_end(self):
        head = self.head
        while head.next.next is not None:
            head = head.next
        head.next = None
        return head


object1 = DoublyLinkedList()
object1.insert_first(5, 10)
object1.insert_first(4, 3)
object1.insert_first(2, 7)
print("Doubly Linked List: ")
object1.print_list()
print("Delete at the first: ")
object1.delete_first()
object1.print_list()
print("Delete at the end: ")
object1.delete_at_end()
