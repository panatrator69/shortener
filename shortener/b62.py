"""Stolen from https://fredrikaverpil.github.io/blog/2021/01/08/encoding-uuids-with-base62/"""

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num, alphabet=BASE62):
    """Encode a positive number in Base X.

    Arguments:
        `num` (int): The number to encode
        `alphabet` (str): The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return "".join(arr)


def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number.

    Arguments:
        `string` (str): The encoded string
        `alphabet` (str): The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base**power)
        idx += 1

    return num
