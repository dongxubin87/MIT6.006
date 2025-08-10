def direct_access_array(A):
    u = 1 + max(A)
    D = [None] * u
    for x in A:
        D[x] = x
    i = 0
    for key in D:
        if key is not None:
            A[i] = key
            i += 1


def counting_sortA(A):
    u = 1 + max(A)
    D = [[] for i in range(u)]
    for x in A:
        D[x].append(x)
    i = 0
    for l in D:
        for x in l:
            A[i] = x
            i += 1


def counting_sortB(A):
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
        D[x.key] += 1
    for k in range(1, u):
        D[k] += D[k - 1]
    for x in list(reversed(A)):
        A[D[x.key] - 1] = x
        D[x.key] -= 1


def radix_sort(A):
    n = len(A)
    u = max(A)
    c = 1 + u.bit_length() // n.bit_length()

    class Obj:
        pass

    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i]
        for j in range(c):
            high, low = divmod(high, 10)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sortB(D)
    for i in range(n):
        A[i] = D[i].item


A = [329, 457, 657, 999, 839, 436, 720, 355]
radix_sort(A)
print(A)
