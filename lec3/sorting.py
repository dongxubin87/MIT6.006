def selection_sort_last(L):
    n = len(L)
    for i in range(n - 1, 0, -1):
        max = i
        for j in range(i):
            if L[j] > L[max]:
                max = j
        L[i], L[max] = L[max], L[i]


def selection_sort_first(L):
    n = len(L)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if L[j] < L[min]:
                min = j
        L[i], L[min] = L[min], L[i]


def selection_recursion(L):
    n = len(L)
    if n < 1:
        return
    selection_recursion_helper(L, n - 1)


def selection_recursion_helper(L, k):
    if k < 1:
        return
    m = k
    for i in range(k):
        if L[m] < L[i]:
            m = i
    L[k], L[m] = L[m], L[k]
    selection_recursion_helper(L, k - 1)


def insertion_sort(L):
    n = len(L)
    for i in range(1, n):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1


def merge_sort_recursion(L):
    n = len(L)
    if n < 2:
        return
    mid = n // 2
    A = L[:mid]
    B = L[mid:]
    merge_sort_recursion(A)
    merge_sort_recursion(B)
    a = len(A)
    b = len(B)

    while a > 0 and b > 0:
        if A[a - 1] > B[b - 1]:
            L[a + b - 1] = A[a - 1]
            a -= 1
        else:
            L[a + b - 1] = B[b - 1]
            b -= 1

    while a > 0:
        L[a + b - 1] = A[a - 1]
        a -= 1
    while b > 0:
        L[a + b - 1] = B[b - 1]
        b -= 1


def merge_sort(A, a=0, b=None):
    if b is None:
        b = len(A)
    if b - a <= 1:
        return
    m = (a + b) // 2
    merge_sort(A, a, m)
    merge_sort(A, m, b)
    L, R = A[a:m], A[m:b]
    i = j = 0
    while a < b:
        if j >= len(R) or (i < len(L) and L[i] <= R[j]):  # keep stable
            A[a] = L[i]
            i += 1
        else:
            A[a] = R[j]
            j += 1
        a += 1


lst = [2, 3, 4, 4, 1, 5, 7]
# selection_sort_last(lst)
# selection_recursion(lst)
# selection_sort_first(lst)
# insertion_sort(lst)
merge_sort(lst)
print(lst)
