"""Module to check the ending of arabic words"""
from tashkeel import Tashkeels


# def is_raf(word):
#     # if list(word)[-1] == Tashkeels.KASRA.value:
#     #     return True
#     # return False
#     pass

# def is_nasb(word):
#     pass


def is_jarr(word):
    """check if arabic word ends with kasra"""
    return list(word)[-1] == Tashkeels.KASRA.value
