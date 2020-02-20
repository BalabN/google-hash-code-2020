import numpy as np


def ScoreLibery(bookScores,libery):
    # print(libery)
    for i,eachLibery in enumerate(libery):
        sumeScore=0
        bookScore=[]
        tmp1=[]
        tmp2=[]
        books = eachLibery["books"]
        for eachBook in books:
            sumeScore=sumeScore+bookScores[eachBook]
            bookScore.append(bookScores[eachBook])


        sortedIndex = np.argsort(bookScore)
        sortedIndex = sortedIndex[::-1]
        for x in sortedIndex:
            tmp1.append(bookScore[x])
            tmp2.append(books[x])


        libery[i]["booksScore"] = tmp1
        libery[i]["books"] = tmp2

        numberOfBooks=len(eachLibery["books"])
        booksScore = numberOfBooks * sumeScore

        liberyScore=booksScore+(booksScore/(eachLibery["t_j"]+(eachLibery["m_j"]/numberOfBooks)))

        libery[i]["score"]=round(liberyScore,2)

    # print(libery)
    return libery


