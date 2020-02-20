import numpy as np
import pandas as pd
import json
from hashio import read, write


def first(book_scores, libraries):
    libs = sorted(libraries, key=lambda x: x["t_j"])
    return [{
        "Y": i,
        "K": len(x["books"]),
        "books": sorted(x["books"], key= lambda x: book_scores[x])
    } for i, x in enumerate(libs)]


if __name__ == '__main__':
    print("Hello world!")
    fnames = [
        '/a_example.txt',
        'b_read_on.txt',
        'c_incunabula.txt',
        'd_tough_choices.txt',
        'e_so_many_books.txt',
        'f_libraries_of_the_world.txt'
    ]
    for fname in fnames:
        B, L, D, book_scores, libraries = read(f"data/input/{fname}")
        # print("B =", B)
        # print("L = ", L)
        # print("D = ", D)
        # print("book_scores = ", book_scores)
        # print("libraries = ", json.dumps(libraries, indent=4))
        # output = [
        #     {
        #         "Y": 0,  # library ID
        #         "K": 1,  # number of books scanned from library Y
        #         "books": [
        #             0, 1, 2, 3,  #  id of books ordered by scanning time
        #         ]
        #     }
        # ]
        output = first(book_scores, libraries)
        write(f"data/output/{fname}", output)
