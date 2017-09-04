# https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/

from itertools import permutations


def concat_numbers(nums):
    perms = list(int(''.join(p)) for p in permutations(nums))
    print("{} {}".format(min(perms), max(perms)))

n = '17 32 91 7 46'
concat_numbers([x for x in n.split(' ')])


