from tashkeel import Tashkeels

def is_raf(word):
    pass

def is_nasb(word):
    pass

def is_jarr(word):
    if list(word)[-1] == Tashkeels.KASRA.value:
        return True
    return False




