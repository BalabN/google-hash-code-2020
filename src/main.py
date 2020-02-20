import numpy as np
import pandas as pd
import json
from hashio import read, write

if __name__ == '__main__':
    print("Hello world!")
    fname = '/a_example.txt'
    B, L, D, book_scores, libraries = read(f"data/input/{fname}")
    print("B =", B)
    print("L = ", L)
    print("D = ", D)
    print("book_scores = ", book_scores)
    print("libraries = ", json.dumps(libraries, indent=4))
    output = [
        {
            "Y": 0,  # library ID
            "K": 1,  # number of books scanned from library Y
            "books": [
                0, 1, 2, 3,  #  id of books ordered by scanning time
            ]
        }
    ]
    A = len(output)
    write(f"data/output/{fname}", output)
