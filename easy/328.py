# https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/


def gen_squares(n, str):
    int_str = [int(x) for x in str.split(' ')]
    s = list()

    for x in range(0, n):
        s.append(int_str[x*n:(x*n)+n])
    return s


def check_latin(grid):
    cols = set()

    for index, g in enumerate(grid):
        # Item in a row more than once
        if len(set(g)) != len(g):
            return False
        cols.add(g[index])

    for x in range(0, len(grid)):
        cols = set()
        for g in grid:
            cols.add(g[x])

        # Item in columns more than once
        if len(cols) != len(grid):
            return False

    return True


input_str = '1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1'
squares = gen_squares(4, input_str)
print(check_latin(squares))
