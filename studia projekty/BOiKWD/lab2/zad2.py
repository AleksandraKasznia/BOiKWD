import numpy as np

numberOfHotels = 4
numberOfCrit = 4
priceMatrix = np.array([[1, 15/21, 23/21, 25/21], [21/15, 1, 23/15, 25/15], [21/23, 15/23, 1, 15/23],
                  [21/25, 15/25, 23/25, 1]])

foodMatrix = np.array([[1, 1, 3/2, 25/20], [1, 1, 3/2, 25/20], [2/3, 2/3, 1, 25/30],
                        [20/25, 20/25, 30/25, 1]])

distanceMatrix = np.array([[1, 3/2, 12/20, 8/20], [2/3, 1, 12/30, 8/30], [20/12, 30/12, 1, 8/12],
                            [20/8, 30/8, 12/8, 1]])

parkingMatrix = np.array([[1, 1/9, 1, 1/9], [9, 1, 9, 1], [1, 1/9, 1, 1/9], [9, 1, 9, 1]])

prefMatrix = np.array([[1, 5, 3, 4], [1/5, 1, 4, 1], [1/3, 1/4, 1, 2], [1/4, 1, 1/2, 1]])

listOfMatrices = [priceMatrix, foodMatrix, distanceMatrix, parkingMatrix]

listOfVectors = []

for i in listOfMatrices:
    e_values, e_vectors = np.linalg.eig(i)
    vector = e_vectors[:, e_values.argmax()]
    vector /= np.sum(vector)
    listOfVectors.append(vector)

e_values, e_vectors = np.linalg.eig(prefMatrix)
vector = e_vectors[:, e_values.argmax()]
vector /= np.sum(vector)

for i in range(len(vector)):
    listOfVectors[0][i] *= vector[i]
    listOfVectors[1][i] *= vector[i]
    listOfVectors[2][i] *= vector[i]
    listOfVectors[3][i] *= vector[i]

prefSum = np.zeros(shape=(numberOfHotels,2))


for i in range(numberOfCrit):
    for j in range(numberOfHotels):
        prefSum[i][0] += listOfVectors[i][j]

for i in range(numberOfHotels):
    prefSum[i][1] = i

print(prefSum)
prefSum = prefSum[:, 0].argsort()

print("Ranking\n")

for i in range(numberOfHotels):
    print(prefSum[numberOfHotels-i-1])

print("Legenda\n 0 - hotel TUR\n 1 - hotel KUR\n 2 - hotel MUR\n 3 - hotel BÓR")

