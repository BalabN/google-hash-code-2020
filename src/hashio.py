def read(fname):
    with open(fname) as f:
        content = f.readline().split("\n")
        B, L, D = (int(x) for x in content[0].split(" "))
        book_scores = [int(b) for b in f.readline().split(" ")]
        print(B, L, D)
        print(book_scores)
        libraries = []
        for j in range(L):
            n_j, t_j, m_j = [int(x) for x in f.readline().split(" ")]
            book_ids = [int(x) for x in f.readline().split(" ")]
            libraries.append({
                "n_j": n_j,
                "t_j": t_j,
                "m_j": m_j,
                "books": book_ids
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
