import random
import math

from scipy.special import erfc


def monobit(bit_string):
    """
    http://qrng.b-phot.org/static/media/NistTestsLongDescription.pdf

    p-value >= 0.01 considered random

    :param bit_string: string of bits
    :return p-value: result of monobit test
    """
    count = 0
    for bit in bit_string:
        count += (2*int(bit) - 1)

    observed_sum = abs(count) / math.sqrt(len(bit_string))
    p_value = erfc(observed_sum / math.sqrt(2))

    return p_value

if __name__ == "__main__":
    # test not very random numbers
    test_ones = format(2**256 - 1, "0b")
    print("input: 2^256 - 1, output: {}".format(monobit(test_ones)))

    test_zeroes = ''.join(["0" for i in list(range(256))])
    print("input: 0, output: {}".format(monobit(test_zeroes)))

    # test with random number
    test_random = format(random.getrandbits(256), '0b')
    print("input: random 256-bit number, output: {}".format(monobit(test_random)))
