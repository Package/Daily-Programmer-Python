from itertools import permutations


def next_largest(num):
    perms = set(''.join(x) for x in list(permutations(str(num), len(str(num)))))
    return min([x for x in perms if int(x) > num])


print(next_largest(19000))

