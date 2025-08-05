"""
Problem 1-2. [16 points] Given a data structure D that supports Sequence operations:
• D.build(X) in O(n) time, and
• D.insert at(i, x) and D.delete at(i), each in O(log n) time,
where n is the number of items stored in D at the time of the operation, describe algorithms to
implement the following higher-level operations in terms of the provided lower-level operations.
Each operation below should run in O(k log n) time. Recall, delete at returns the deleted item.
(a) reverse(D, i, k): Reverse in D the order of the k items starting at index i (up to
index i + k − 1).
(b) move(D, i, k, j): Move the k items in D starting at index i, in order, to be in front
of the item at index j. Assume that expression i ≤ j < i + k is false.
"""


def reverse(D, i, k):
    if k < 2:
        return
    a = D.delete_at(i)
    b = D.delete_at(i + k - 1)
    D.insert_at(i, b)
    D.insert_at(i + k - 1, a)

    reverse(D, i + 1, k - 2)


def move(D, i, k, j):
    if k < 1:
        return
    x = D.delete_at(i)
    if j > i:
        j -= 1
    D.insert_at(j, x)
    j += 1
    if i > j:
        i += 1
    move(D, i, k - 1, j)


"""
Sisa Limpson is a very organized second grade student who keeps all of her course notes on individual pages stored in a three-ring binder. If she has n pages of notes in her binder, the first page
is at index 0 and the last page is at index n − 1. While studying, Sisa often reorders pages of her
notes. To help her reorganize, she has two bookmarks, A and B, which help her keep track of
locations in the binder.
Describe a database to keep track of pages in Sisa’s binder, supporting the following operations,
where n is the number of pages in the binder at the time of the operation. Assume that both
bookmarks will be placed in the binder before any shift or move operation can occur, and that
bookmark A will always be at a lower index than B. For each operation, state whether your
running time is worst-case or amortized.
build(X) Initialize database with pages from iterator X in O(|X|) time.
place mark(i, m) Place bookmark m ∈ {A, B} between the page at index i and
the page at index i + 1 in O(n) time.
read page(i) Return the page at index i in O(1) time.
shift mark(m, d) Take the bookmark m ∈ {A, B}, currently in front of the page at
index i, and move it in front of the page at index i + d
for d ∈ {−1, 1} in O(1) time.
move page(m) Take the page currently in front of bookmark m ∈ {A, B},
and move it in front of the other bookmark in O(1) time. 
"""
"""
The major idea is to build an array

1. build(X). Initializ an array to store pages.
2. place mark(i, m), we can define two varibals to store mark A and B
    at this step, we need to extend the array to the size of 3n.
    dividing the array to three parts. p1, p2(A-B), p3, in front of two marks, we keep n space
3. shift mark(m, d)
4. move page(m), for the method, because there is some space before marks, so when we move the page, it is constant time after amortization.

"""


"""
Problem 1-4. [44 points] Doubly Linked List
In Lecture 2, we described a singly linked list. In this problem, you will implement a doubly
linked list, supporting some additional constant-time operations. Each node x of a doubly linked
list maintains an x.prev pointer to the node preceeding it in the sequence, in addition to an
x.next pointer to the node following it in the sequence. A doubly linked list L maintains a pointer
to L.tail, the last node in the sequence, in addition to L.head, the first node in the sequence.
For this problem, doubly linked lists should not maintain their length.
(a) [8 points] Given a doubly linked list as described above, describe algorithms to implement the following sequence operations, each in O(1) time.
insert first(x) insert last(x) delete first() delete last()
(b) [5 points] Given two nodes x1 and x2 from a doubly linked list L, where x1 occurs
before x2, describe a constant-time algorithm to remove all nodes from x1 to x2 inclusive from L, and return them as a new doubly linked list.
(c) [6 points] Given node x from a doubly linked list L1 and second doubly linked list L2,
describe a constant-time algorithm to splice list L2 into list L1 after node x. After the
splice operation, L1 should contain all items previously in either list, and L2 should
be empty.
(d) [25 points] Implement the operations above in the Doubly Linked List Seq
class in the provided code template; do not modify the Doubly Linked List Node
class. You can download the code template including some test cases from the website.
"""


class Node:
    def __init__(self, item):
        self.prev = None
        self.next = None
        self.item = item


class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, x):

        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_last(self, x):

        if self.tail is None:
            self.insert_first(x)
            return
        node = Node(x)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            return None

        deleted_node = self.head
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return deleted_node.item

    def delete_last(self):
        if self.tail is None:
            return None

        if self.size == 1:
            return self.delete_first()

        deleted_node = self.tail
        self.tail.prev.next = None
        self.tail = deleted_node.prev
        self.size -= 1
        return deleted_node.item

    def remove(self, x1, x2):
        if x1 is self.head and x2 is self.tail:
            self.head = None
            self.tail = None
        elif x1 is self.head:
            self.head = x2.next
            x2.next.prev = None
        elif x1 is not self.head and x2 is not self.tail:
            x1.prev.next = x2.next
            x2.next.prev = x1.prev.next
        else:
            x1.prev.next = None
            self.tail = x1.prev.next

        new_list = Doubly_Linked_List()
        new_list.head = x1
        x1.prev = None
        new_list.tail = x2
        x2.next = None
        return new_list
    def splice(self,other,x):
        
