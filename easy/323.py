# https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/

from itertools import combinations


def triplets(nums):
    trips = {(x, y, z) for x in nums for y in nums for z in nums if sum([x, y, z]) == 0}
    trips_sorted = (sorted(t) for t in trips)
    return list(sorted(trips_sorted))


def triplets2(nums):
    return set(tuple(sorted(x)) for x in combinations(nums, 3) if sum(x) == 0)


print(triplets2([9, -6, -5, 9, 8, 3, -4, 8, 1, 7, -4, 9, -9, 1, 9, -9, 9, 4, -6, -8]))
