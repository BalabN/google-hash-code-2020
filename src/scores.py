from statistics import mean, stdev


def filter_libs(book_scores, libraries):
    mean_score, dev_score = mean(book_scores), stdev(book_scores)
    mean_t, dev_t = mean(map(lambda x: x["t_j"], libraries)), stdev(map(lambda x: x["t_j"], libraries))
    libraries = list(filter(lambda x: mean(x["book_scores"]) >= mean_score - dev_score, libraries))
    libraries = list(filter(lambda x: x["t_j"] >= mean_t - dev_t, libraries))
    return list(libraries)
