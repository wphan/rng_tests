import numpy as np
from bad_rng import bad_rng

import pylab as pl


def generate(sequence, show=False):
    """
    Thsi doesnt work - how do u do this
    @param bit_string: string of bits
    @param show: True to show, False to save as png
    @return nothing: saves a png of the random generated
    """
    time_step = 1 / 30

    fft = np.fft.fft(sequence)
    freqs = np.fft.fftfreq(len(sequence), time_step)

    # plot
    pl.subplot(111)
    pl.plot(freqs, fft)
    if show:
        pl.show()
    else:
        pl.savefig("spectral.png")


if __name__ == "__main__":
    bits = 2048
    upperbound = 1e6

    # generate(format(random.getrandbits(bits), '0b'), True)
    generate([int(i * upperbound) for i in bad_rng], True)
