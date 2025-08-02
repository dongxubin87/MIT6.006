"""
Problem 1-3. Collage Collating
Fodoby is a company that makes customized software tools for creative people. Their newest
software, Ottoshop, helps users make collages by allowing them to overlay images on top of each
other in a single document. Describe a database to keep track of the images in a given document
which supports the following operations:
1. make document(): construct an empty document containing no images
2. import image(x): add an image with unique integer ID x to the top of the document
3. display(): return an array of the document’s image IDs in order from bottom to top
4. move below(x, y): move the image with ID x directly below the image with ID y
Operation (1) should run in worst-case O(1) time, operations (2) and (3) should each run in worstcase O(n) time, while operation (4) should run in worst-case O(log n) time, where n is the number
of images contained in a document at the time of the operation.
"""

import bisect


class Image:
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.prev = None
        self.next = None

    def __lt__(self, other):
        return self.id < other.id


class Document:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ids_sorted = []

    def import_image(self, x, v):
        node = Image(x, v)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        bisect.insort(self.ids_sorted, node)

    def dispaly(self):
        res = []
        cur = self.tail
        while cur:
            res.append(cur)
        return res

    def move(self, x, y):
        id_x = bisect.bisect_left(self.ids_sorted, Image(x, None))
        id_y = bisect.bisect_left(self.ids_sorted, Image(y, None))

        node_x = self.ids_sorted[id_x]
        node_y = self.ids_sorted[id_y]

        if node_x.prev:
            node_x.prev.next = node_x.next
        else:
            self.head = node_x.next

        if node_x.next:
            node_x.next.prev = node_x.prev
        else:
            self.tail = node_x.prev

        node_x.prev = node_y
        node_x.next = node_y.next

        if node_y.next:
            node_y.next.prev = node_x
        else:
            self.tail = node_x

        node_y.next = node_x
