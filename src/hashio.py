from statistics import mean


def read(fname):
    with open(fname) as f:
        content = f.readline().split("\n")
        B, L, D = (int(x) for x in content[0].split(" "))
        book_scores = [int(b) for b in f.readline().split(" ")]
        # print(B, L, D)
        # print(book_scores)
        libraries = []
        for j in range(L):
            n_j, t_j, m_j = [int(x) for x in f.readline().split(" ")]
            book_ids = [int(x) for x in f.readline().split(" ")]
            lib_book_scores = [book_scores[x] for x in book_ids]
            libraries.append({
                "n_j": n_j,  # nubmber of books
                "t_j": t_j,  # days to signup
                "m_j": m_j,  # can be shipped from lib
                "books": book_ids,
                "book_scores": lib_book_scores,
                "simple_score_1": t_j * m_j * mean(lib_book_scores)
            })
    return B, L, D, book_scores, libraries


def write(fname, data):
    with open(fname, "w") as f:
        f.write(f"{len(data)}\n")
        for library in data:
            f.write(f"{library['Y']} {library['K']}\n")
            for x in library["books"]:
                f.write(f"{x} ")
            f.write(f"\n")
