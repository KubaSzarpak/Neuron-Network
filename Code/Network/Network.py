from Code.Network.Perceptron import Perceptron


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
    correct_answers = 0
    for vec in test_data:
        for perceptron in perceptron_list:
            if vec.name == perceptron.__func__(vec):
                correct_answers += 1
                break

    return correct_answers


def execute(perceptron_list, vec):
    for perceptron in perceptron_list:
        result = perceptron.__func__(vec)
        if result != "Null":
            return result
    return "Not found"
