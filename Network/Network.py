from Perceptron import Perceptron


def generate_perceptions_list(training_data, alpha=0.01):
    """Generates a list of perceptrons, every of a uniq class from given training data

    Parameters
    ----------
    training_data : list
        The list of data, that network could learn from

    Returns
    -------
    perceptron_list : list
        The list of perceptrons of uniq types
    """
    perceptron_list = []
    for data in training_data:
        exists = False
        for t in perceptron_list:
            if data.name == t.name:
                exists = True
                break

        if not exists:
            perceptron_list.append(Perceptron(data.name, training_data, alpha))
    return perceptron_list


def do(perceptron_list, test_data):
    """Gives each data from test_data to each perceptron and increments correct_answers
    if some perceptron classifies correctly.

    Parameters
    ----------
    perceptron_list : list
        a list of perceptrons.

    test_data : list
        a list of My_Vector that you want to test the network on.

    Returns
    -------
    correct_answers : int
        count how much data was classified correctly.
     """
    correct_answers = 0
    for vec in test_data:
        for perceptron in perceptron_list:
            if vec.name == perceptron.func(vec):
                correct_answers += 1
                break

    return correct_answers


def execute(perceptron_list, vec):
    """Gives each perceptron the vector vec. If some perceptron activates then it returns this value. If not, then it returns "Not found"

    Parameters
    ----------
    perceptron_list : list
        a list of perceptrons.
    vec
        a vector with data that you want to classify.

    Returns
    -------
    result : str
        The result of classification or "Not found" if network could not classify this data.

    """
    for perceptron in perceptron_list:
        result = perceptron.func(vec)
        if result != "Null":
            return result
    return "Not found"
