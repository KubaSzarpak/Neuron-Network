"""
Author: Jakub Szarpak
"""
from Code.My_Vector import My_Vector
from Code.Perceptron import Perceptron


def read_file(path):
    try:
        with open(path) as file:
            vector_list = []
            line = file.readline()
            while line != "":
                lista = line.split(",", 1)
                data = count_letters(lista[1])

                vector_list.append(My_Vector(data, lista[0]))

                line = file.readline()

        return vector_list
    except FileNotFoundError:
        print("No such file")


def count_letters(data):
    a_ascii = ord("a")
    data.lower()
    character_occurrence = list()
    for i in range(26):
        character_occurrence.append(0)

    for letter in str(data):
        if a_ascii <= ord(letter) < (a_ascii + 26):
            character_occurrence[ord(letter) - a_ascii] += 1

    return character_occurrence


trainingPath = "C:\\Users\\kubas\\PycharmProjects\\pythonProject\\Data\\lang.train.csv"
testPath = "C:\\Users\\kubas\\PycharmProjects\\pythonProject\\Data\\lang.test.csv"

trainingList = read_file(trainingPath)
testList = read_file(testPath)
perceptron_E = Perceptron("English", trainingList)
perceptron_G = Perceptron("German", trainingList)
perceptron_P = Perceptron("Polish", trainingList)
perceptron_S = Perceptron("Spanish", trainingList)

a = 0
i = 1
for vec in testList:
    correctType = perceptron_E.func(vec)

    if correctType == vec.name:
        a += 1
        continue

    correctType = perceptron_G.func(vec)

    if correctType == vec.name:
        a += 1
        continue

    correctType = perceptron_P.func(vec)

    if correctType == vec.name:
        a += 1
        continue

    correctType = perceptron_S.func(vec)

    if correctType == vec.name:
        a += 1
        continue

    # e = perceptron_E.func(vec)
    # g = perceptron_G.func(vec)
    # p = perceptron_P.func(vec)
    # s = perceptron_S.func(vec)

    # print(e + " | " + g + " | " + p + " | " + s)

print("Dane testowe: " + str(len(trainingList)) + " | Dane sprawdzone: " + str(a))
