from statistics import mean


def filter_libs(book_scores, libraries):
    mean_score = mean(book_scores)
    filter(lambda x: mean(x["book_scores"] >= mean_score), libraries)
    return list(libraries)
