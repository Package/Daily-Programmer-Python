# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/


def scrabble(letters, target):
    blanks = letters.count("?")
    letters = list(letters)
    matched = 0

    for t in target:
        # Can use the blanks and what we have already matched to complete the word
        if matched + blanks >= len(target):
            break

        if t in letters:
            letters.remove(t)
            matched += 1
        elif blanks > 0:
            matched += 1
            blanks -= 1
        else:
            return False

    return True


def read_file():
    with open("input/enable1.txt") as f:
        return [w.replace("\n", "") for w in f.readlines()]


def longest(letters):
    return sorted([w for w in words if scrabble(letters, w)], key=lambda w: len(w), reverse=True)[0]

words = read_file()

# Tests
print(longest("dcthoyueorza"))
print(longest("uruqrnytrois"))
print(longest("rryqeiaegicgeo??"))
print(longest("udosjanyuiuebr??"))
print(longest("vaakojeaietg????????"))