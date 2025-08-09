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
    u = 1 + max(A)
    D = [0] * u
    for x in A:
        D[x] += 1
    for k in range(1, u):
        D[k] += D[k - 1]
    for x in list(reversed(A)):
        A[D[x] - 1] = x
        D[x] -= 1


A = [4, 4, 6, 3, 6, 5, 1, 2, 3]
counting_sortB(A)
print(A)
