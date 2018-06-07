# https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/


def odd_numbers(max_range):
    return [x for x in range(1, max_range + 1, 2)]


def lucky_numbers(n):
    lucky = list(n)
    # Start with number 3 which is at index 1 of the input numbers
    index = 1

    while index < len(lucky):
        templucky = list()
        for k, v in enumerate(lucky):
            if k == 0 or (k + 1) % lucky[index] != 0:
                templucky.append(v)
        index += 1
        lucky = templucky

    return lucky


def check_lucky(x):
    nums = odd_numbers(x * 2)
    lucky_nums = lucky_numbers(nums)

    smaller = [n for n in lucky_nums if n < x][-1]
    larger = [n for n in lucky_nums if n > x][0]
    is_lucky = x in lucky_nums

    if is_lucky:
        print("{} is a lucky number".format(x))
    else:
        print("{} < {} < {}".format(smaller, x, larger))


check_lucky(103)
check_lucky(225)
check_lucky(997)
