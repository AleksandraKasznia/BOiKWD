import numpy as np
from itertools import combinations

A = np.array([[1, 2/3, 2, 5/2, 5/3, 5], [3/2, 1, 3, 10/3, 3, 9], [1/2, 1/3, 1, 4/3, 7/8, 5/2],
              [2/5, 3/10, 3/4, 1, 5/6, 12/5], [3/5, 1/3, 8/7, 6/5, 1, 3], [1/5, 1/9, 2/5, 5/12, 1/3, 1]])

vector56 = np.array([[3], [1]])

B = np.array([[1, 2/5, 3, 7/3, 1/2, 1], [5/2, 1, 4/7, 5/8, 1/3, 3], [1/3, 7/4, 1, 1/2, 2, 1/2],
              [3/7, 8/5, 2, 1, 4, 2], [2, 3, 1/2, 1/4, 1, 1/2], [1, 1/3, 2, 1/2, 2, 1]])

vector456 = np.array([[2], [1/2], [1]])

C = np.array([[1, 17/4, 17/20, 8/5, 23/6, 8/3], [4/17, 1, 1/5, 2/5, 9/10, 2/3], [20/17, 5, 1, 21/10, 51/10, 10/3],
              [5/8, 5/2, 10/21, 1, 5/2, 11/6], [6/23, 10/9, 10/51, 2/5, 1, 19/30], [3/8, 3/2, 3/10, 6/11, 30/19, 1]])

vector24 = np.array([[2], [5]])


def if_can_be_solved_with_hre(matrix, n, k):
    list_of_options = []
    koczkodaj = []

    for j in range(len(matrix)):
        list_of_options.append(j)
    comb = combinations(list_of_options, 3)
    for i in list(comb):
        value_for_three = matrix[i[0]][i[1]] / matrix[i[0]][i[2]] / matrix[i[2]][i[1]]
        val = min([abs(1 - value_for_three), abs(1 - 1 / value_for_three)])
        koczkodaj.append(val)
    value = max(koczkodaj)
    condition = 1 - (1 + (4 * (n - 1) * (n - k -2)) ** (1/2)) / (2 * (n - 1))

    return value < condition


def rank_with_aritm(matrix, vector, known_objects):
    n = len(matrix)
    k = len(known_objects)
    u = n - k
    matrix_a = np.zeros((u, u))
    matrix_b = np.zeros((u, k))

    index_b_i = 0
    index_a_i = 0
    index_i = 0

    for i in range(n):
        if not(len(known_objects) > index_i and known_objects[index_i] == i):
            index_j = 0
            index_a_j = 0

            for j in range(n):
                if len(known_objects) > index_j and known_objects[index_j] == j:
                    matrix_b[index_b_i][index_j] = matrix[i][j]
                    index_j += 1
                else:
                    matrix_a[index_a_i][index_a_j] = matrix[i][j]
                    index_a_j += 1

            index_a_i += 1
            index_b_i += 1
        else:
            index_i += 1

    multiplier_a = -1 / (n - 1)

    for i in range(u):
        for j in range(u):
            if i != j:
                matrix_a[i][j] *= multiplier_a

    b = np.dot((-multiplier_a * matrix_b), vector)
    w = np.linalg.solve(matrix_a, b)

    if if_can_be_solved_with_hre(matrix, n, len(known_objects)):
        print("Otrzymany ranking jest poprawny")
    else:
        print("Otrzymany ranking jest niepewny")
    result = np.zeros(n)
    index = 0
    index_w = 0

    for i in range(n):
        if len(known_objects) > index and known_objects[index] == i:
            result[i] = vector[index]
            index += 1
        else:
            result[i] = w[index_w]
            index_w += 1

    print(result)


def rank_with_geo(matrix, vector, known_objects):
    n = len(matrix)
    k = len(known_objects)
    u = n - k
    prod_m = np.zeros(u)
    index = 0

    index_of_an_object = 0
    for i in range(n):
        if len(known_objects) > index_of_an_object and  known_objects[index_of_an_object] == i:
            index_of_an_object += 1
        else:
            prod_m[index] = np.prod(matrix[i])
            index += 1

    prod_w = np.prod(vector)
    tmp = prod_m * prod_w
    b = np.log10(tmp)

    matrix_a = np.full((u,u), -1)
    np.fill_diagonal(matrix_a, n - 1)
    w = np.linalg.solve(matrix_a, b)

    result = np.zeros(n)
    index = 0
    index_w = 0

    for i in range(n):
        if len(known_objects) > index and known_objects[index] == i:
            result[i] = vector[index]
            index += 1
        else:
            result[i] = 10**w[index_w]
            index_w += 1

    print(result)


print("Ranking HRE z wartością średnią arytmetyczną A")
rank_with_aritm(A, vector56, [4, 5])
print("Ranking HRE z wartością średnią geometryczną A")
rank_with_geo(A, vector56, [4, 5])
print("Ranking HRE z wartością średnią arytmetyczną B")
rank_with_aritm(B, vector456, [3, 4, 5])
print("Ranking HRE z wartością średnią geometryczną B")
rank_with_geo(B, vector456, [3, 4, 5])
print("Ranking HRE z wartością średnią arytmetyczną C")
rank_with_aritm(C, vector24, [1, 3])
print("Ranking HRE z wartością średnią geometryczną C")
rank_with_geo(C, vector24, [1, 3])


