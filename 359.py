# https://www.reddit.com/r/dailyprogrammer/comments/8gzaz5/20180504_challenge_359_hard_primes_in_grids/
from math import ceil, sqrt

# data = [[1, 1, 3],
#         [7, 5, 4],
#         [9, 3, 7]]

# data = [[1, 1, 9, 3, 3],
#         [9, 9, 5, 6, 3],
#         [8, 9, 4, 1, 7],
#         [3, 3, 7, 3, 1],
#         [3, 2, 9, 3, 9]]

data = [[3, 1, 7, 3, 3, 3],
        [9, 9, 5, 6, 3, 9],
        [1, 1, 8, 1, 4, 2],
        [1, 3, 6, 3, 7, 3],
        [3, 4, 9, 1, 9, 9],
        [3, 7, 9, 3, 7, 9]]
primes = set()


# Iterate over each cell in the grid and solve the problem for each one
def solve():
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            process(x, y)


# Processes a cell in the grid at the given X,Y location. Checks neighboring cells
# in all directions for potential primes.
def process(x, y):

    # Check horizontally across
    current_num = None
    for y1 in range(y, len(data)):
        if current_num is None:
            current_num = data[x][y1]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x][y1]))
        check_for_prime(current_num)

    # Check horizontally backwards
    current_num = None
    for y1 in range(y, -1, -1):
        if current_num is None:
            current_num = data[x][y1]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x][y1]))
        check_for_prime(current_num)

    # Check vertically down
    current_num = None
    for x1 in range(x, len(data)):
        if current_num is None:
            current_num = data[x1][y]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x1][y]))
        check_for_prime(current_num)

    # Check vertically up
    current_num = None
    for x1 in range(x, -1, -1):
        if current_num is None:
            current_num = data[x1][y]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x1][y]))
        check_for_prime(current_num)

    # Check diagonally south east
    current_num = None
    for z in range(0, len(data)):
        if x + z > len(data) - 1 or y + z > len(data) - 1:
            break
        if current_num is None:
            current_num = data[x + z][y + z]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x + z][y + z]))
        check_for_prime(current_num)

    # Check diagonally south west
    current_num = None
    for z in range(0, len(data)):
        if x + z > len(data) - 1 or y - z < 0:
            break
        if current_num is None:
            current_num = data[x + z][y - z]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x + z][y - z]))
        check_for_prime(current_num)

    # Check diagonally north west
    current_num = None
    for z in range(0, len(data)):
        if x - z < 0 or y - z < 0:
            break
        if current_num is None:
            current_num = data[x - z][y - z]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x - z][y - z]))
        check_for_prime(current_num)

    # Check diagonally north east
    current_num = None
    for z in range(0, len(data)):
        if x - z < 0 or y + z > len(data) - 1:
            break
        if current_num is None:
            current_num = data[x - z][y + z]
            check_for_prime(current_num)
            continue
        current_num = int(str(current_num) + str(data[x - z][y + z]))
        check_for_prime(current_num)


# Check if the provided number is a prime. If it is, it's added to the set of known primes.
def check_for_prime(n):
    if is_prime(n):
        primes.add(n)


# Does the check on whether the number is a prime.
def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    for y in range(3, ceil(sqrt(x)) + 1, 2):
        if x % y == 0:
            return False

    return True


solve()
print(len(primes))
print(sorted(primes))
