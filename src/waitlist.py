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
        return self._size

    def __repr__(self):
        return f"Waitlist({self.to_list()})"

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.name)
            curr = curr.next
        return result

    def join(self, name):
        new_node = _Node(name)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def find(self, name):
        curr = self.head
        while curr:
            if curr.name == name:
                return True
            curr = curr.next
        return False

    def cancel(self, name):
        prev, curr = None, self.head
        while curr:
            if curr.name == name:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = prev
                curr.next = None  # optional cleanup
                self._size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def bump(self, name):
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
