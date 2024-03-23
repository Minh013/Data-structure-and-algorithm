#Python code for doubly linked list
class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
#this link always point to first Link
head = None
#this link always point to last Link
last = None
current = None
#is list empty
def is_empty():
    return head is None


#display the doubly linked list
def print_list():
    ptr = head
    while ptr is not None:
        print(f"({ptr.key},{ptr.data})")
        ptr = ptr.next
#insert link at the first location
def insert_first(key, data):
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

def remove_index(key):
    global head, last
    current = head
    while current is not None:
        if current.key == key:
            if current == head:
                head = current.next
                if head is not None:
                    head.prev = None
                else:
                    last = None
            elif current == last:
                last = current.prev
                last.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
            return
        current = current.next
    print("Node with the key", key, "not found")


insert_first(1,10)
insert_first(2,20)
insert_first(3,30)
insert_first(4,1)
insert_first(5,40)
insert_first(6,56)
print("Doubly Linked List: ")
print_list()
remove_index(2)
print("After deletion: ")
print_list()
