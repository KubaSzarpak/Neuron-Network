from Code.Network.My_Vector import My_Vector


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
        return -1


def count_letters(data):
    a_ascii = ord("a")
    character_occurrence = list()
    for i in range(26):
        character_occurrence.append(0)

    for letter in str(data):
        letter.lower()
        if a_ascii <= ord(letter) < (a_ascii + 26):
            character_occurrence[ord(letter) - a_ascii] += 1

    return character_occurrence
