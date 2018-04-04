import platform
import random
import pickle


def generate_random_sample(os):
    rng = random.SystemRandom()
    with open("{}_sample.pickle".format(os), "wb") as f:
        data = rng.getrandbits(int(100e6))
        pickle.dump(format(data, "0b"), f)



if __name__ == "__main__":
    os = platform.system()
    generate_random_sample(os)
