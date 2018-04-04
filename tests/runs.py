import random
import math

from scipy.special import erfc
from tests.frequency_monobit import monobit


def runs(bit_string):
    """
    http://qrng.b-phot.org/static/media/NistTestsLongDescription.pdf

    p-value >= 0.01 considered random

    :param bit_string: string of bits
    :return p-value: result of runs test
    """
    pi = 0
    n = len(bit_string)
    for bit in bit_string:
        pi += int(bit)

    pi = float(pi / n)

    p_value = 0.0
    if monobit(bit_string) >= 0.01:
        vn = 1
        for idx, i in enumerate(bit_string):
            try:
                if (bit_string[idx] != bit_string[idx + 1]):
                    vn += 1
            except IndexError:
                break

        p_value = abs(vn - 2 * n * pi * (1 - pi))
        p_value = p_value / (2 * math.sqrt(2 * n) * pi * (1 - pi))
        p_value = erfc(p_value)

    return p_value


if __name__ == "__main__":
    # test not very random numbers
    test_ones = format(2**256 - 1, "0b")
    print("input: 2^256 - 1, output: {}".format(runs(test_ones)))

    test_zeroes = ''.join(["0" for i in list(range(256))])
    print("input: 0, output: {}".format(runs(test_zeroes)))

    # test with random number
    test_random = format(random.getrandbits(256), '0b')
    print("input: random 256-bit number, output: {}".format(runs(test_random)))
