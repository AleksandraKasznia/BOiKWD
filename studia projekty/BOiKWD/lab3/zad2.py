import numpy as np
from itertools import combinations
from math import log

A = np.array([[1, 7, 3], [1/7, 1, 2], [1/3, 1/2, 1]])
B = np.array([[1, 1/5, 7, 1], [5, 1, 1/2, 2], [1/7, 2, 1, 3], [1, 1/2, 1/3, 1]])
C = np.array([[1, 2, 5, 1, 7], [1/2, 1, 3, 1/2, 5], [1/5, 1/3, 1, 1/5, 2],
              [1, 2, 5, 1, 7], [1/7, 1/5, 1/2, 1/7, 1]])
test = np.array([[1, 3, 1/2, 5], [1/3, 1, 1/6, 2], [2, 6, 1, 9], [1/5, 1/2, 1/9, 1]])

listOfMatrices = [A, B, C, test]
listOfSattyIndexes = []
listOfGeomIndexes = []
listOfKocIndexes = []
listOfVectors = []

for i in listOfMatrices:
    e_values, e_vectors = np.linalg.eig(i)
    index = (e_values.max() - len(i)) / (len(i) - 1)
    listOfSattyIndexes.append(index)

print(listOfSattyIndexes)

# geometryczny

for i in listOfMatrices:
    vector = []
    for j in range(len(i)):
        val = np.prod(i[j])
        val = val**(1.0/len(listOfMatrices[0]))
        vector.append(val)
    vector /= np.sum(vector)
    listOfVectors.append(vector)

for m in range(len(listOfMatrices)):
    matrix = listOfMatrices[m]
    vector = listOfVectors[m]
    index = 2/(len(matrix) - 1)/(len(matrix) - 2)
    summ = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            val = matrix[i][j] * vector[j] / vector[i]
            logarithm = log(val, 10)**2
            summ += logarithm
    index *= summ
    listOfGeomIndexes.append(index)

print(listOfGeomIndexes)

# koczkodaja

for i in listOfMatrices:
    listOfOptions = []
    koczkodaj = []
    for j in range(len(i)):
        listOfOptions.append(j)
    comb = combinations(listOfOptions, 3)
    for k in list(comb):
        valueForThree = i[k[0]][k[1]] / i[k[0]][k[2]] / i[k[2]][k[1]]
        val = min([abs(1 - valueForThree), abs(1 - 1 / valueForThree)])
        koczkodaj.append(val)
    listOfKocIndexes.append(max(koczkodaj))

print(listOfKocIndexes)


