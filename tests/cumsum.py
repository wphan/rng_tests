import numpy as np

import math
from scipy.stats import norm
from scipy.stats import t


def sncpdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def cumsum(bit_string, forward=True):
    """
    http://qrng.b-phot.org/static/media/NistTestsLongDescription.pdf

    near random bit_string, p_value should be near 0
    non-randomw ill have a large p_value

    :param bit_string: string of bits
    :param forward: True to traverse forwards, else backwards
    :return p-value: result of test
    """
    n = len(bit_string)

    # reverse traversal if desired
    bit_string = bit_string if forward else bit_string[::-1]

    sums = np.zeros(n)
    for idx, bit in enumerate(bit_string):
        epsilon = 1 if bit == '1' else -1

        if idx > 0:
            sums[idx] = sums[idx - 1] + epsilon
        else:
            sums[idx] = epsilon

    abs_max = np.max(np.abs(sums))

    # compute p-value
    # calculate terms in the first summation
    start = int(np.floor(0.25 * np.floor(-n / abs_max) + 1))
    end = int(np.floor(0.25 * np.floor(n / abs_max) - 1))
    first_terms = []
    for i in range(start, end + 1):
        left = t.cdf((4 * i + 1) * abs_max / np.sqrt(abs_max), 1)
        right = t.cdf((4 * i - 1) * abs_max / np.sqrt(abs_max), 1)
        first_terms.append(left - right)

    # calculate the terms in the second summation
    start = int(np.floor(0.25 * np.floor(-n / abs_max - 3)))
    end = int(np.floor(0.25 * np.floor(n / abs_max) - 1))
    second_terms = []
    for i in range(start, end + 1):
        left = t.cdf((4 * i + 3) * abs_max / np.sqrt(abs_max), 1)
        right = t.cdf((4 * i + 1) * abs_max / np.sqrt(abs_max), 1)
        second_terms.append(left - right)

    return 1.0 - np.sum(np.array(first_terms)) + np.sum(np.array(second_terms))


if __name__ == "__main__":
    # test not very random numbers
    test_bad_randoms = ""
    for i in list(range(512)):
        test_bad_randoms += "10"
    print("input: not random input, output: {}".format(cumsum(test_bad_randoms)))

    test_zeroes = ''.join(["0" for i in list(range(1024))])
    print("input: 0, output: {}".format(cumsum(test_zeroes)))

    # test with random number
    test_random = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    print("input: random number, output: {}".format(cumsum(test_random)))
