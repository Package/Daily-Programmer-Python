# https://old.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/


def tally_scores(chars):
    char_mapping = {}

    for c in chars:
        if c.lower() not in char_mapping:
            char_mapping[c.lower()] = 0
        char_mapping[c.lower()] += -1 if c.isupper() else 1

    return char_mapping


print(tally_scores('EbAAdbBEaBaaBBdAccbeebaec'))