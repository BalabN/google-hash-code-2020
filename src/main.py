import numpy as np
import pandas as pd
import json
from hashio import read, write

if __name__ == '__main__':
    print("Hello world!")
    B, L, D, libraries = read('data/input/a_example.txt')
    print("B =", B)
    print("L = ", L)
    print("D = ", D)
    print("libraries = ", json.dumps(libraries, indent=4))

