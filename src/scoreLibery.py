import numpy as np


def ScoreLibery(bookScores,libery):

    all_books =[]
    libery_score=[]

    for i, eachLibery in enumerate(libery):
        all_books.extend(eachLibery["books"])


    unique_elements, counts_elements = np.unique(all_books, return_counts=True)
    unique_dict=dict(zip(unique_elements, counts_elements))


    for i,eachLibery in enumerate(libery):
        sumeScore=0
        bookScore=[]
        tmp1=[]
        tmp2=[]
        books_diversity=[]
        books = eachLibery["books"]

        for eachBook in books:
            sumeScore=sumeScore+bookScores[eachBook]
            bookScore.append(bookScores[eachBook])

            books_diversity.append(unique_dict[eachBook]-1)



        sortedIndex = np.argsort(bookScore)
        sortedIndex = sortedIndex[::-1]
        for x in sortedIndex:
            tmp1.append(bookScore[x])
            tmp2.append(books[x])


        libery[i]["booksScore"] = tmp1
        libery[i]["books"] = tmp2


        libery[i]["books_diversity"] = books_diversity

        numberOfBooks=len(eachLibery["books"])
        booksScore = numberOfBooks * sumeScore

        liberyScore=booksScore+(booksScore/(eachLibery["t_j"]+(eachLibery["m_j"]/numberOfBooks)))

        libery[i]["score"]=round(liberyScore,2)
        libery[i]["score"] = round((np.sum(libery[i]["books_diversity"])/len(libery[i]["books_diversity"])), 2)
        libery_score.append(libery[i]["score"])

    avarage_score=np.average(libery_score)

    for i, eachLibery in enumerate(libery):
        j2 = [x for x in libery[i]["books_diversity"] if x >= avarage_score]
        libery[i]["score"] = round((np.sum(j2)/len(j2)), 2)

    return libery

#od sredene vrednosti vseh srednih vrednosti...