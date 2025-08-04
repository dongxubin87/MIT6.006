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
