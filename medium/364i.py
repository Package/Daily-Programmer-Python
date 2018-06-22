# https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/

ducci_cache = []


def rotate(ducci):
    return [abs(ducci[x] - (ducci[0] if x == len(ducci) - 1 else ducci[x+1])) for x in range(len(ducci))]


def solve(ducci):
    # The ducci has been seen before
    if ducci in ducci_cache:
        ducci_cache.append(ducci)
        return True

    ducci_cache.append(ducci)

    # The ducci has descended to all zeros
    zero_count = len([x for x in ducci if x == 0])
    if zero_count == len(ducci):
        return True

    return solve(rotate(ducci))


solve([10, 12, 41, 62, 31, 50])
for d in ducci_cache:
    print(d)
print('Solved in: {} steps'.format(len(ducci_cache)))