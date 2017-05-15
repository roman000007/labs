from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        self._head = None

    def __len__(self):
        res = 0
        current = self._head
        while current != None:
            res += 1
            current = current.next
        return res

    def split_half(self):
        current = self._head
        l = len(self)
        ml1 = Multiset()
        ml2 = Multiset()
        for i in range(l // 2):
            ml1.add(current)
            current = current.next
        while current is not None:
            ml2.add(current)
            current = current.next
        return ml1, ml2

    def __str__(self):
        current = self._head
        s = ""
        while current != None:
            s += str(current) + " -> "
            current = current.next
        return s[:-4]




