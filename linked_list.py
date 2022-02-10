class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    # Singly Linked List

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        # returns the no of nodes in the list in linear time
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        # adds a new node containing data at the head of the list in constant time
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        # search for the first node containing data that matches the key
        # returns the node or None if not found. Takes linear time
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        # inserts a new node containing data at index position in constant time
        # but finding the position to insert is linear
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new
                new.next_node = next_node

    def __repr__(self):
        # returns string representation of the list in linear time
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return ' -> '.join(nodes)

    def remove_at_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.__count -= 1

        return current
