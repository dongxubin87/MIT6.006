"""Problem 1-4. Brick Blowing
Porkland is a community of pigs who live in n houses lined up along one side of a long, straight
street running east to west. Every house in Porkland was built from straw and bricks, but some
houses were built with more bricks than others. One day, a wolf arrives in Porkland and all the
pigs run inside their homes to hide. Unfortunately for the pigs, this wolf is extremely skilled at
blowing down pig houses, aided by a strong wind already blowing from west to east. If the wolf
blows in an easterly direction on a house containing b bricks, that house will fall down, along with
every house east of it containing strictly fewer than b bricks. For every house in Porkland, the wolf
wants to know its damage, i.e., the number of houses that would fall were he to blow on it in an
easterly direction."""

"""
(a) Suppose n = 10 and the number of bricks in each house in Porkland from west to east
is [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]. Compute for this instance the
damage for every house in Porkland.
"""
a = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
ans = [4, 5, 6, 3, 3, 1, 4, 1, 1, 1]

"""
(b) A house in Porkland is special if it either (1) has no easterly neighbor or (2) its adjacent neighbor to the east contains at least as many bricks as it does. Given an array
containing the number of bricks in each house of Porkland, describe an O(n)-time
algorithm to return the damage for every house in Porkland when all but one house
in Porkland is special.
"""


def special_damage():
    q = [1, 2, 5, 6, 7, 1, 2, 3]
    n = len(q)
    res = [1] * n
    k = -1
    for i in range(n - 1):
        if q[i] > q[i + 1]:
            k = i + 1
            break
    if k == -1:
        return res
    # tail = q[k + 1 :]
    # p = 0
    # m = len(tail)
    # for i in range(0, k + 1):
    #     while p < m and q[i] > tail[p]:
    #         p += 1
    #     res[i] = p + 1
    # return res
    j = k
    p = 0
    for i in range(k):
        while j < n and q[i] > q[j]:
            p += 1
            j += 1
        res[i] = p + 1

    return res


print(special_damage())

"""
Given an array containing the number of bricks in each house of Porkland, describe
an O(n log n)-time algorithm to return the damage for every house in Porkland.
Write a Python function get damages that implements your algorithm
"""
a = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]


def merge_damage(a):
    n = len(a)
    res = [1 for _ in a]
    H = [(a[i], i) for i in range(len(a))]

    def merge_count(H, l, r):
        if r - l <= 1:
            return
        mid = (l + r) // 2
        merge_count(H, l, mid)
        merge_count(H, mid, r)
        i = l
        j = mid
        temp = []
        count = 0
        while i < mid and j < r:
            if H[i][0] > H[j][0]:
                temp.append(H[j])
                count += 1
                j += 1
            else:
                temp.append(H[i])
                res[H[i][1]] += count
                i += 1
        while i < mid:
            temp.append(H[i])
            res[H[i][1]] += count
            i += 1
        while j < r:
            temp.append(H[j])
            j += 1

        H[l:r] = temp

    merge_count(H, 0, n)
    return res


L = merge_damage(a)
print(L)
