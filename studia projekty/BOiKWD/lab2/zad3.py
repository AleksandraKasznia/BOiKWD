import numpy as np

car1price = 68200
car1fuel = 8.9
car1safety = 4
car1trunk = 4601
car1pas = 5

car3price = 87394
car3fuel = 5.8
car3safety = 4.5
car3trunk = 4301
car3pas = 4

car2price = 39900
car2fuel = 11.2
car2safety = 3.5
car2trunk = 4151
car2pas = 5

# I assumed that the price is most important, then safety and then the capacity
preferences = np.array([[1, 3, 5], [1/3, 1, 4], [1/5, 1/4, 1]])

passengers = np.array([[1, car1pas/car2pas, car1pas/car3pas], [car2pas/car1pas, 1, car2pas/car3pas],
                       [car3pas/car1pas, car3pas/car2pas, 1]])
trunk = np.array([[1, car1trunk/car2trunk, car1trunk/car3trunk], [car2trunk/car1trunk, 1, car2trunk/car3trunk],
                  [car3trunk/car1trunk, car3trunk/car2trunk, 1]])
safety = np.array([[1, car1safety/car2safety, car1safety/car3safety], [car2safety/car1safety, 1, car2safety/car3safety],
                   [car3safety/car1safety, car3safety/car2safety, 1]])
fuel = np.array([[1, car1fuel/car2fuel, car1fuel/car3fuel], [car2fuel/car1fuel, 1, car2fuel/car3fuel],
                 [car3fuel/car1fuel, car3fuel/car2fuel, 1]])
price = np.array([[1, car1price/car2price, car1price/car3price], [car2price/car1price, 1, car2price/car3price],
                  [car3price/car1price, car3price/car2price, 1]])

# preference
e_values, e_vectors = np.linalg.eig(preferences)
vectorOfPref = e_vectors[:, e_values.argmax()]
vectorOfPref /= np.sum(vectorOfPref)

# price
listOfPriceMatrices = [price, fuel]
listOfPriceVectors = []

for i in listOfPriceMatrices:
    e_values, e_vectors = np.linalg.eig(i)
    vector = e_vectors[:, e_values.argmax()]
    vector /= np.sum(vector)
    listOfPriceVectors.append(vector)

for i in range(len(listOfPriceVectors)):
    for j in range(len(listOfPriceVectors[0])):
        listOfPriceVectors[i][j] *= vectorOfPref[0]

# capacity
listOfCapacityMatrices = [trunk, passengers]
listOfCapacityVectors = []

for i in listOfCapacityMatrices:
    e_values, e_vectors = np.linalg.eig(i)
    vector = e_vectors[:, e_values.argmax()]
    vector /= np.sum(vector)
    listOfCapacityVectors.append(vector)

for i in range(len(listOfCapacityVectors)):
    for j in range(len(listOfCapacityVectors[0])):
        listOfCapacityVectors[i][j] *= vectorOfPref[1]

# safety
e_values, e_vectors = np.linalg.eig(safety)
safetyVector = e_vectors[:, e_values.argmax()]
safetyVector /= np.sum(safetyVector)

for i in range(len(safetyVector)):
    safetyVector[i] *= vectorOfPref[2]

# overall preferences
prefSum = np.zeros(shape=(len(preferences), 2))

for i in range(len(prefSum)):
    prefSum[i][0] += safetyVector[i]
    prefSum[i][1] = i
    for j in range(len(listOfCapacityVectors)):
        prefSum[i][0] += (listOfCapacityVectors[j][i]/len(listOfCapacityVectors))
    for k in range(len(listOfPriceVectors)):
        prefSum[i][0] += (listOfPriceVectors[k][i]/len(listOfPriceVectors))

print(prefSum)
prefSum = prefSum[:, 0].argsort()

print("Ranking\n")

for i in range(len(prefSum)):
    print(prefSum[len(prefSum)-i-1]+1, "samochód")
