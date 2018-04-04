import timeit
import pickle
import glob

from tests.cumsum import cumsum
from tests.frequency_monobit import monobit
from tests.random_excursions import random_excursions
from tests.runs import runs
from tests.spectral import spectral


def run_a_test(test_execution, samples):
    print("=============================")
    print("Running {} test".format(test_execution.__name__))
    for sample in samples:
        start_time = timeit.default_timer()
        print(sample)
        with open(sample, "rb") as f:
            data = pickle.load(f)
            p_value = test_execution(data)
            name = sample.split("/")[-1]
            name = name.split(".")[0]
            name.replace("_sample", "")
            print("{0}: P_value: {1}: elapsed_time: {2}s".format(name, p_value, timeit.default_timer() - start_time))


def run_all_tests(samples):
    '''
    ['./sample_data/Linux_WSL_sample.pickle', './sample_data/Linux_ubuntu.pickle', './sample_data/Windows_sample.pickle']
    '''
    run_a_test(cumsum, samples)
    run_a_test(monobit, samples)
    run_a_test(random_excursions, samples)
    run_a_test(runs, samples)
    run_a_test(spectral, samples)


if __name__ == "__main__":
    samples = glob.glob("./sample_data/*.pickle")
    total_start = timeit.default_timer()
    run_all_tests(samples)
    print("\nTotal time elapsed: {}s".format(timeit.default_timer() - total_start))
