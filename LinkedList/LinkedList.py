# Some operations
# Insertion, Deletion, Display, Search, Delete
# Adding element at the begging

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Print the Linked List
    def print_list(self):
        val = self.head
        print("Linked List: ")
        while val is not None:
            print(val.data)
            val = val.next


    def add_at_the_beginning(self, newData):
        new_node = Node(newData)

        # Update the new nodes next val to the existing node
        new_node.next = self.head
        self.head = new_node

    def add_el_at_position(self, node_position, new_data):
        if node_position is None:
            print("The position doesnt exist")
            return
        new_node = Node(new_data)
        new_node.next = node_position.next
        node_position.next = new_node

    def delete_at_begin(self):
        self.head = self.head.next

    def delete_at_end(self):
        head = self.head
        while head.next.next is not None:
            head = head.next
        head.next = None
        return head

    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        # Find the key to be deleted
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # If the key is not present
        if temp is None:
            return

        # Remove the node
        if prev is not None:
            prev.next = temp.next
        else:
            # If the key is in the head node
            self.head = temp.next

    def search_node(self, key):
        count = 0
        head = self.head
        while head is not None:
            if head.data == key:
                print("The element is found")
                count += 1
            head = head.next
        if count == 0:
            print("The element is not found")


list1 = SinglyLinkedList()
list1.head = Node("4")
el1 = Node("5")
el2 = Node("6")
el3 = Node("7")
el4 = Node("3")

list1.head.next = el1
el1.next = el2
el2.next = el3
el3.next = el4

# list1.add_at_the_beginning("3")
list1.add_el_at_position(el3.next, "9")
list1.print_list()
print("Here we are deleting element at the beginning")
list1.delete_at_begin()
list1.print_list()
print("Here we are deleting element at the end")
list1.delete_at_end()
list1.print_list()
list1.delete_node(2)
list1.print_list()
list1.search_node("3")
