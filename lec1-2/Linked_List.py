class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node != None:
            yield node.item
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        node = Linked_List_Node(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        return x

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(self, len(self) - 1)


def find_cycle(L):
    head = L.head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            curr = slow.next
            while curr != slow:
                count += 1
                curr = curr.next
            return count
    else:
        return 0


lst = Linked_List_Seq()
lst.build([1, 2, 3, 4, 5, 6])


last_node = lst.head.later_node(len(lst) - 1)
loop_start_node = lst.head.later_node(0)
last_node.next = loop_start_node
length = find_cycle(lst)
print("length", length)


def Set_from_Seq(seq):
    class set_from_seq:
        def __init__(self):
            self.S = seq()

        def __len__(self):
            return len(self.S)

        def __iter__(self):
            yield from self.S

        def insert(self, x):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == x.key:
                    self.S.set_at(i, x)
                    return
            self.S.insert_last(x)

        def delete(self, x):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == x:
                    return self.S.delete_at(i)

        def find(self, x):
            for e in self:
                if e.key == x:
                    return e
            return None

        def find_min(self):
            min = None
            for x in self:
                if min is None or x.key < min.key:
                    min = x
            return min

        def find_max(self):
            max = None
            for x in self:
                if max is None or x.key > max.key:
                    max = x
            return max

        def find_next(self, x):
            res = None
            for e in self:
                if e.key > x:
                    if res is None or e.key < res.key:
                        res = e
            return res

        def find_prev(self, x):
            res = None
            for e in self:
                if e < x:
                    if res is None or res.key > e.key:
                        res = e
            return res

        def iter_ord(self):
            x = self.find_min()
            while x:
                yield x
                x = self.find_next(x.key)

    return set_from_seq


"""
Jen drives her ice cream truck to her local elementary school at recess. All the kids rush to line up
in front of her truck. Jen is overwhelmed with the number of students (there are 2n of them), so
she calls up her associate, Berry, to bring his ice cream truck to help her out. Berry soon arrives
and parks at the other end of the line of students. He offers to sell to the last student in line, but the
other students revolt in protest: “The last student was last! This is unfair!”
The students decide that the fairest way to remedy the situation would be to have the back half of
the line (the n kids furthest from Jen) reverse their order and queue up at Berry’s truck, so that the
last kid in the original line becomes the last kid in Berry’s line, with the (n+1)st kid in the original
line becoming Berry’s first customer.
(a) Given a linked list containing the names of the 2n kids, in order of the original line
formed in front of Jen’s truck (where the first node contains the name of the first kid
in line), describe an O(n)-time algorithm to modify the linked list to reverse the order
of the last half of the list. Your algorithm should not make any new linked list nodes
or instantiate any new non-constant-sized data structures during its operation. """


def reverse_linklist(L):
    n = len(L) // 2
    a = L.head
    for _ in range(n - 1):
        a = a.next
    # a is n item
    curr = a.next
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    a.next = prev


L = Linked_List_Seq()
L.build([1, 2, 3, 4, 5, 6])
for x in L:
    print(x)

reverse_linklist(L)
for x in L:
    print(x)
