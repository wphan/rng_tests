from copy import copy

import random

import pylab as pl
import matplotlib


def make_random_bitmap(rng, bits, show=False):
    """
    @param rng: callable that generates 'bits' bits of random numbers
    @param bits: generate a png of resolution bits x bits
    @param show: True to show, False to save as png
    @return nothing: saves a png of the random generated
    """
    data = []
    for i in list(range(bits)):
        # generate a random number 'bits' long
        bit_string = format(rng(bits), '0b')
        bit_string = [int(i) for i in bit_string]

        # pad with leading 0's
        while len(bit_string) < bits:
            bit_string.insert(0, 0)
        data.append(bit_string)

    # make black/white
    cmap = copy(matplotlib.cm.get_cmap('gray'))
    cmap.set_under('white')
    cmap.set_over('black')

    # plot
    pl.subplot(111)
    pl.imshow(data, cmap=cmap, origin='lower', interpolation='nearest')
    if show:
        pl.show()
    else:
        name = '_'.join([rng.__name__, str(bits)])
        pl.savefig(name + ".png")


if __name__ == "__main__":
    make_random_bitmap(random.getrandbits, 256)
