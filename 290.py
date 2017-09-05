# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/


def is_kaprekar_number(n):
    n2 = str(n ** 2)

    for x in range(0, len(n2)):
        left = n2[:x]
        right = n2[x:]

        if left == '' or int(left) == 0 or right == '' or int(right) == 0:
            continue

        if int(left) + int(right) == n:
            return True

    return False


def gen_kaprekar_numbers(min_range, max_range):
    return [n for n in range(min_range, max_range + 1) if is_kaprekar_number(n)]


print(gen_kaprekar_numbers(1, 50))
print(gen_kaprekar_numbers(2, 100))
print(gen_kaprekar_numbers(101, 9000))