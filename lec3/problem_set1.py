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
    D.insert_at(i + k - 1, a)
    D.insert_at(i, b)
    reverse(D, i + 1, k - 2)
