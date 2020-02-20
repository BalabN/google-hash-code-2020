import numpy as np


def ScoreLibery(bookScores,libery):
    for i,eachLibery in enumerate(libery):
        sumeScore=0
        BookScore=[]

        for eachBook in eachLibery["books"]:
            sumeScore=sumeScore+bookScores[eachBook]
            BookScore.append(bookScores[eachBook])

       # print(BookScore)
       # arr1inds = np.argsort(BookScore)
       # sorted_arr1=np.take_along_axis(BookScore, arr1inds, axis=0)
       # print(sorted_arr1)
       # sorted_arr1 = BookScore[arr1inds[::-1]]
       # sorted_arr2 = eachLibery["books"][arr1inds[::-1]]

       # print(sorted_arr1,sorted_arr2)

        libery[i]["booksScore"] = BookScore

        numberOfBooks=len(eachLibery["books"])
        booksScore = numberOfBooks * sumeScore

        liberyScore=booksScore+(booksScore/(eachLibery["t_j"]+(eachLibery["m_j"]/numberOfBooks)))

        libery[i]["score"]=round(liberyScore,2)

    return libery


