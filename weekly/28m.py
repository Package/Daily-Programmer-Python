# https://old.reddit.com/r/dailyprogrammer/comments/81aexf/weekly_28_mini_challenges/

"""
[nth number of Recamán's Sequence]
"""
def a(n):
    recaman_seq = [0]

    for x in range(1, n + 1):
        lower = recaman_seq[x - 1] - x
        higher = recaman_seq[x - 1] + x

        if lower >= 0 and lower not in recaman_seq:
            recaman_seq.append(lower)
        else:
            recaman_seq.append(higher)

    return recaman_seq[n]


print('a({}) = {}'.format(5, a(5)))
print('a({}) = {}'.format(15, a(15)))
print('a({}) = {}'.format(25, a(25)))
print('a({}) = {}'.format(100, a(100)))
print('a({}) = {}'.format(1005, a(1005)))
