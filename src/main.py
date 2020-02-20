import numpy as np
import pandas as pd
import json
from hashio import read, write
from scoreLibery import ScoreLibery
from scores import filter_libs


def first(book_scores, libraries):
    utez1, utez2 = 0.9, 0.1
    max_score1 = max(libraries, key=lambda x: x["simple_score_1"])["simple_score_1"]
    # max_score2 = max(libraries, key=lambda x: x["score"])["score"]
    libs = sorted(enumerate(libraries), key=lambda x: utez1 * x[1]["simple_score_1"]/max_score1)  # + utez2 * 1/x[1]["score"]/max_score2)
    output = []
    for i, x in libs:
        out = {
            "Y": x["Y"],
            "K": len(x["books"]),
            "books": sorted(x["books"], key= lambda x: book_scores[x], reverse=True)
        }
        output.append(out)
    return output


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
        print(fname)
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
        libraries = ScoreLibery(book_scores, libraries)
        libraries = filter_libs(book_scores, libraries)
        output = first(book_scores, libraries)
        write(f"data/output/{fname}", output)
