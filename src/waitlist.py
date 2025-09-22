class _Node:
    __slots__ = ("name", "next")
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        return self._size

    def to_list(self):
        """Return names from head to tail as a Python list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.name)
            curr = curr.next
        return result

    def join(self, name):
        """Append name at the tail (O(1))."""
        new_node = _Node(name)
        if not self.head:  # empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def find(self, name):
        """Return True if name exists, else False."""
        curr = self.head
        while curr:
            if curr.name == name:
                return True
            curr = curr.next
        return False

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        prev, curr = None, self.head
        while curr:
            if curr.name == name:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                if curr == self.tail:  # if tail is removed
                    self.tail = prev
                self._size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def bump(self, name):
        """Move first occurrence to the head; return True if moved."""
        if not self.head or self.head.name == name:
            return bool(self.head and self.head.name == name)

        prev, curr = None, self.head
        while curr:
            if curr.name == name:
                if curr == self.tail:
                    self.tail = prev
                if prev:
                    prev.next = curr.next
                curr.next = self.head
                self.head = curr
                return True
            prev, curr = curr, curr.next
        return False
