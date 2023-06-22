from My_Vector import My_Vector


def read_file(path: str):
    """Reads file and generates a list of My_Vector based on the number of occurrences
    of each letter of the Latin alphabet.

    Parameters
    ----------
    path : str
        path to a file which stores data.

    Returns
    -------
    vector_list
        a list of My_Vector that can be used with neuron network.
    """
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


def count_letters(data: str):
    """Counts occurrences of each letter of the Latin alphabet in data.

    Parameters
    ----------
    data : str
        a text

    Returns
    -------
    character_occurrence : list
        a list of how much each 26 letters occurrences in data.

    """
    a_ascii = ord("a")
    character_occurrence = []
    for i in range(26):
        character_occurrence.append(0)

    for letter in str(data):
        letter.lower()
        if a_ascii <= ord(letter) < (a_ascii + 26):
            character_occurrence[ord(letter) - a_ascii] += 1

    return character_occurrence
