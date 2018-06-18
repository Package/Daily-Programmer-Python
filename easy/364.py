# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
import random

dd_input = '5d12'


def get_number_of_dice():
    return int(dd_input[:dd_input.index('d')])


def get_dice_size():
    return int(dd_input[dd_input.index('d') + 1:])


print(sum([random.randint(1, get_dice_size()) for x in range(get_number_of_dice())]))
