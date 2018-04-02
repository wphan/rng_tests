import random
import numpy as np

from scipy.special import gammaincc


def get_pik_value(k, x):
    if k == 0:
        out = 1 - 1.0 / (2 * np.abs(x))
    elif k >= 5:
        out = (1.0 / (2 * np.abs(x))) * (1 - 1.0 / (2 * np.abs(x))) ** 4
    else:
        out = (1.0 / (4 * x * x)) * (1 - 1.0 / (2 * np.abs(x))) ** (k - 1)
    return out


def random_excursions(bit_string):
    """
    http://qrng.b-phot.org/static/media/NistTestsLongDescription.pdf

    :param bit_string: string of bits
    :return p-values: result of test, if all 8 are >= 0.01
    """
    '''
    int_data = []
    for i in bit_string:
        a = -1.0 if (i == '0') else 1.0
        int_data.append(a)
    '''
    int_data = [(-1.0 if (i == '0') else 1.0) for i in bit_string]

    # calculate cumulative sum and append 0 to beginning and end
    cumulative_sum = np.cumsum(int_data)
    cumulative_sum = np.append(cumulative_sum, [0])
    cumulative_sum = np.append([0], cumulative_sum)

    states = np.array([-4, -3, -2, -1, 1, 2, 3, 4])

    # identify locations where cumulative sum visits 0
    position = np.where(cumulative_sum == 0)[0]

    cycles = []
    for pos in list(range(len(position) - 1)):
        cycles.append(cumulative_sum[position[pos]:position[pos + 1] + 1])

    num_cycles = len(cycles)

    state_count = []
    for cycle in cycles:
        state_count.append(([len(np.where(cycle == state)[0]) for state in states]))
    state_count = np.transpose(np.clip(state_count, 0, 5))

    su = []
    for cycle in range(6):
        su.append([(sct == cycle).sum() for sct in state_count])
    su = np.transpose(su)

    piks = ([([get_pik_value(uu, state) for uu in range(6)]) for state in states])
    inner_term = num_cycles * np.array(piks)
    chi = np.sum(1.0 * (np.array(su) - inner_term) ** 2 / inner_term, axis=1)
    p_values = ([gammaincc(2.5, cs / 2.0) for cs in chi])
    return p_values

def is_u_randoms(p_values):
    """
    larger the return, more unrandom this is
    """
    is_randoms = 0
    for value in p_values:
        if value < 0.01:
            is_randoms += 1

    return is_randoms

if __name__ == "__main__":
    # test not very random numbers
    test_bad_randoms = ""
    for i in list(range(512)):
        test_bad_randoms += "10"
    print("input: not random input, output: {}".format(is_u_randoms(random_excursions(test_bad_randoms))))

    test_zeroes = ''.join(["0" for i in list(range(1024))])
    print("input: 0, output: {}".format(is_u_randoms(random_excursions(test_zeroes))))

    # test with random number
    test_random = format(random.getrandbits(1024), '0b')
    print("input: random 1024-bit number, output: {}".format(is_u_randoms(random_excursions(test_random))))
