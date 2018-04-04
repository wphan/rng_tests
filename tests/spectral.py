import random
import numpy
import math

import scipy
from scipy.special import erfc


def spectral(bit_string):
    """
    http://qrng.b-phot.org/static/media/NistTestsLongDescription.pdf

    recommend using bit_string length > 1000
    p-value >= 0.01 considered random

    :param bit_string: string of bits
    :return p-value: result of test
    """
    if len(bit_string) < 1000:
        print("WARNING: RECOMMENDED BIT LENGTH > 1000")

    n = len(bit_string)
    x = [(2 * int(i) - 1) for i in bit_string]

    s = scipy.fft(x)

    # operate on half of the DFT
    mod = numpy.abs(s[0:int(n / 2)])
    threshold = math.sqrt(numpy.log(1 / 0.05) * n)

    # theoretical number of peaks
    n0 = 0.95 * (n / 2)

    # actual number of peaks
    n1 = len(numpy.where(mod < threshold)[0])

    # result
    p_value = (n1 - n0) / math.sqrt(n * 0.95 * 0.05 / 2)
    p_value = erfc(abs(p_value) / math.sqrt(2))

    return p_value


if __name__ == "__main__":
    bits = 2048

    # test not very random numbers
    test_ones = format(2**bits - 1, "0b")
    print("input: 2^{0}- 1, output: {1}".format(bits, spectral(test_ones)))

    test_zeroes = ''.join(["0" for i in list(range(bits))])
    print("input: 0, output: {}".format(spectral(test_zeroes)))

    # test with random number
    test_random = format(random.getrandbits(bits), '0b')
    print("input: random {0}-bit number, output: {1}".format(bits, spectral(test_random)))
