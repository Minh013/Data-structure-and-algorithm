# Homework: Delete first = None
current = None

def is_empty():
    return head is None

# Insert Element
def insert_first(key, data):
    # Create link
    global head
    new_node = Node(key, data)
    if is_empty():
        head = new_node
        head.next = head
    else:
        # Point it to the old first node
        new_node.next = head
        # Point first to the new first node
        head = new_node

def print_list():
    global head
    link = head
    print("[", end=" ")
    if head is not None:
        while link.next != link:
            print("({},{})".format(link.key, link.data), end=" ")
            link = link.next
        print("]")


insert_first(5, 10)
insert_first(7, 4)
insert_first(3, 2)
print("Circle linked list: ")
print_list()
