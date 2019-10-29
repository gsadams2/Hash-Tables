class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
​
class LinkedList:
    def __init__(self, set_head=None):
        self.head = set_head
​
    def add_to_head(self, value):
        # Create a head node
        new_node = Node(value, self.head)
        # Set current head to new node
        self.head = new_node
​
    def remove(self, value):
        '''
        Find and remove the node with the given value
        '''
        # If we have no head
        if not self.head:
            # print an error and return
            print("Error: Value not found")
        # If the head has our value
        elif self.head.value == value:
            # Remove the head by pointing self.head to head.next
            self.head = self.head.next
        # Else
        else:
            # Keep track of the parent node
            parent = self.head
            current = self.head.next
            # Walk through the linked list until we find a matching value
            while current:
                # If we find a matching value
                if current.value == value:
                    # Delete the node by pointing parent.next to node.next
                    parent.next = current.next
                    return
                parent = parent.next
                current = current.next
            # If we get to the end and have not found the value, print error
            print("Error: Value not found")
​
    # def contains(self, value):
    #     '''
    #     Return true if our LL contains the value
    #     '''
	# 	# Fill this in

    #     if not self.head:
    #         print("Error")
    #     else:
    #         current = self.head.next
    #         while current:
    #             if current.value == value:
    #                 return True
    #         print("Error")

    def contains(self, value):
        '''
        Return true if our LL contains the value
        '''
        current_node = self.head
​
        while current_node:
            if current_node.value == value:
                return True
​
            current_node = current_node.next
​
        return False


ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.contains(2) # True
ll.remove(2)
ll.contains(2) # False