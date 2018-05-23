# https://www.reddit.com/r/dailyprogrammer/comments/7ttiq5/20180129_challenge_349_easy_change_calculator/


def get_input(input):
    split_input = [x for x in str(input).split(' ')]
    input_map = dict()
    input_map['total'] = int(split_input[0])
    input_map['coins'] = sorted([int(x) for x in split_input[1:]], reverse=True)

    return input_map


def get_change(total, coins):
    curr_total = 0
    curr_count = 0
    returned_coins = []

    for y in coins:
        for z in coins:
            curr_total += z
            curr_count += 1
            returned_coins.append(z)

            if curr_total == total:
                print('# of coins needed: {}. Coins returned: {}'.format(curr_count, returned_coins))
                # print(returned_coins)
                return

            if curr_total > total:
                curr_total -= z
                curr_count -= 1
                returned_coins.remove(z)

    print('Impossible to give change.')

    return False


program_input = get_input('19 100 50 50 50 50')
get_change(program_input['total'], program_input['coins'])