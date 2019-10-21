import numpy as np

C1 = np.matrix([[1, 1/7, 1/5], [7, 1, 3], [5, 1/3, 1]])
C2 = np.matrix([[1, 5, 9], [1/5, 1, 4], [1/9, 1/4, 1]])
C3 = np.matrix([[1, 4, 1/5], [1/4, 1, 1/9], [5, 9, 1]])
C4 = np.matrix([[1, 9, 4], [1/9, 1, 1/4], [1/4, 4, 1]])
C5 = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
C6 = np.matrix([[1, 6, 4], [1/6, 1, 1/3], [1/4, 3, 1]])
C7 = np.matrix([[1, 9, 6], [1/9, 1, 1/3], [1/6, 3, 1]])
C8 = np.matrix([[1, 1/2, 1/2], [2, 1, 1], [1, 1, 1]])
Cpar = np.matrix([[1, 4, 7, 5, 8, 6, 6, 2], [1/4, 1, 5, 3, 7, 6, 6, 1/3], [1/7, 1/5, 1, 1/3, 5, 3, 3, 1/5],
                [1/5, 1/3, 3, 1, 6, 3, 4, 1/2], [1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
                [1/6, 1/6, 1/3, 1/3, 3, 1, 1/2, 1/5], [1/6, 1/6, 1/3, 1/4, 4, 2, 1, 1/5],
                [1/2, 3, 5, 2, 7, 5, 5, 1]])

listOfMatrices = [C1, C2, C3, C4, C5, C6, C7, C8]
listOfVectors = []

for i in listOfMatrices:
    e_values, e_vectors = np.linalg.eig(i)
    vector = e_vectors[:, e_values.argmax()]
    vector /= np.sum(vector)
    listOfVectors.append(vector)

e_values, e_vectors = np.linalg.eig(Cpar)
vector = e_vectors[:, e_values.argmax()]
vector /= np.sum(vector)

for i in range(len(vector)):
    listOfVectors[i][0] *= vector[i]
    listOfVectors[i][1] *= vector[i]
    listOfVectors[i][2] *= vector[i]

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(len(listOfVectors)):
    sum1 += listOfVectors[i][0]
    sum2 += listOfVectors[i][1]
    sum3 += listOfVectors[i][2]

print(sum1, sum2, sum3)

print("Ranking domów")


if sum1 > sum2:
    if sum2 > sum3:
        if sum1 > sum3:
            print("dom1\ndom2\ndom3")
        else:
            print("dom1\ndom3\ndom2")
    else:
        print("dom1\ndom3\ndom2")
else:
    if sum3 > sum2:
        print("dom3\ndom2\ndom1")
    else:
        if sum3 > sum1:
            print("dom2\ndom3\ndom1")
        else:
            print("dom2\ndom1\ndom3")