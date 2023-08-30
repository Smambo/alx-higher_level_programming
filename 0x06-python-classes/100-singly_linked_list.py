#!/usr/bin/python3
"""A class that defines a node of a singly linked list"""


class Node:
    """Creates a node class object"""
    def __init__(self, data, next_node=None):
        """Initialises node object."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data property."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data property."""
        if type(value) is not int:
            raise (TypeError("data must be an integer"))
        self.__data = value

    @property
    def next_node(self):
        """Retrieves node property."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets node property."""
        if (not isinstance(value, Node) and value is not None):
            raise (TypeError("next_node must be a Node object"))
        self.__next_node = value

class SinglyLinkedList:
    """Creates a singly linked list class object"""
    __head = None

    def __init__(self):
        """Initialises list."""
        pass

    def __str__(self):
        """print entire list in stdout."""
        my_list = []

        while self.__head:
            my_list.append(self.__head.data)
            self.__head = self.__head.next_node
        return ("\n".join([str(i) for i in sorted(my_list)]))

    def sorted_insert(self, value):
        """
        Inserts new node into correct sorted
        position in the list
        """
        new_node = Node(value, self.__head)
        self.__head = new_node
