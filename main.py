import math

def rough_estimate(x):
    # deliberately simple, just to have something to poke at
    return math.sqrt(abs(x)) * 1.3

if __name__ == "__main__":
    samples = [0, 1, 4, 16, 25]
    for s in samples:
        print(s, "->", round(rough_estimate(s), 3))
