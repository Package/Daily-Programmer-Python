# https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/


def adds_to_zero(nums):
    if 0 in nums:
        return True

    solutions = [(xv, yv)
                 for xk, xv in enumerate(nums)
                 for yk, yv in enumerate(nums)
                 if xk != yk and xv + yv == 0]

    return len(solutions) > 0


print(adds_to_zero([-97364, -71561, -69336, 19675, 71561, 97863]))
