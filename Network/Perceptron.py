import math
import random


class Perceptron:

    def __init__(self, name, training_data, alfa=0.01):
        self.name = name
        self.training_data = training_data
        self.weight = []
        self.teta = 1.0
        self.alfa = alfa

    def __learn__(self):
        self.__weight_draw__(len(list(self.training_data[0].data)))
        E_max = 0.01
        E = 1.0
        i = 0

        while E >= E_max and i < 1000000:
            sum = 0.0
            for vector in self.training_data:
                y = self.__activation_func__(vector)
                if vector.name == self.name:
                    d = 1
                else:
                    d = 0

                self.__new_weight__(d, y, vector)
                self.__new_teta__(d, y)

                sum += math.pow(d - y, 2)

            E = (1.0 / len(self.training_data)) * sum

            i += 1
        # print(f"{self.name} learned after {i} iterations")

    def __weight_draw__(self, length):
        """Draws starting weights for perceptron

        Parameters
        ----------
        length : int
            the length of weight vector
        """
        for i in range(length):
            random.seed()
            self.weight.append(random.random())

    def __activation_func__(self, vector):
        """Threshold activation function returns 1 if net is greater or equals 0.

        Parameters
        ----------
        vector : MyVector
            input vector that will be classified by this perceptron

        Returns
        -------
        1 if is activated or 0 if is not activated
        """
        if self.__net__(vector) >= 0:
            return 1
        else:
            return 0

    def __net__(self, vector):
        """Dot product minus teta

        Parameters
        ----------
        vector : MyVector
            input vector that will be classified by this perceptron

        Returns
        -------
        net : int
            Dot product minus teta
        """
        net = 0.0

        for i in range(len(vector.data)):
            net += vector.data[i] * self.weight[i]

        net -= self.teta

        return net

    def __new_weight__(self, d, y, vector):
        """Calculates a new vector of weights based on the formula "weight + alfa * (d - y) * vector"

        Parameters
        ----------
        d : int
            expected result
        y : int
            actual result
        vector : MyVector
            input vector that will be classified by this perceptron
        """
        for i in range(len(vector.data)):
            self.weight[i] = self.weight[i] + self.alfa * (d - y) * vector.data[i]

    def __new_teta__(self, d, y):
        """Calculates a new teta based on the formula "alfa * (d - y)"

        Parameters
        ----------
        d : int
            expected result
        y : int
            actual result
        """
        self.teta -= self.alfa * (d - y)

    def __func__(self, vector):
        """Main function. It activates all methods of this perceptron to classify given vector

        Parameters
        ----------
        vector : MyVector
            input vector that will be classified by this perceptron

        Returns
        -------
        self.name : string
            if perceptron activates
        "Null"
            if perceptron is not activated"""
        y = self.__activation_func__(vector)
        if y == 1:
            return self.name
        else:
            return "Null"
