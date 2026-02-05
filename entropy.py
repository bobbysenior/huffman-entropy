#!/bin/python3 

import argparse
from math import log2

parser = argparse.ArgumentParser()
parser.add_argument("FILENAME", help="The path to the file on which to compute entropy")

args = parser.parse_args()

filename = args.FILENAME

def compute_entropy(data) -> float:
    """
    Function that takes as an argument a list of frequencies by bytes (from 0 to 255)
    """
    # Count the number of iteration for every byte
    freq = [0 for _ in range(255)]
    for byte in data:
        freq[byte] += 1

    # Compute the frequency of each byte
    size = len(data)
    for i in range(len(freq)):
        if freq[i] == 0:
            continue
        freq[i] = freq[i] / size

    H = 0
    for p in freq:
        if p == 0:
            continue
        H -= p * log2(p)

    
    return H

def main():
    with open(filename, "rb") as f:
        data = f.read()
    print(compute_entropy(data))


if __name__ == "__main__":
    main()
