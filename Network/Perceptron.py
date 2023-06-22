import math
import random


class Perceptron:
    """Class that represents perceptron."""

    def __init__(self, name, training_data, alfa=0.01):
        self.name = name
        self.training_data = training_data
        self.weight = []
        self.teta = 1.0
        self.alfa = alfa

    def learn(self):
        """Learn function which completes task of learning process. It counts y, which is result of
        activate function and calculates new weights vector and new teta. Then it calculates teaching
        error based on formula "(1/vector.size)*sum.of((d-y)^2)"
        """

        self.weight_draw(len(list(self.training_data[0].data)))
        E_max = 0.01
        E = 1.0
        i = 0

        while E >= E_max and i < 1000000:
            sum = 0.0
            for vector in self.training_data:
                y = self.activation_func(vector)
                if vector.name == self.name:
                    d = 1
                else:
                    d = 0

                self.new_weight(d, y, vector)
                self.new_teta(d, y)

                sum += math.pow(d - y, 2)

            E = (1.0 / len(self.training_data)) * sum

            i += 1

    def weight_draw(self, length):
        """Draws starting weights for perceptron.

        Parameters
        ----------
        length : int
            the length of weight vector.
        """
        for i in range(length):
            random.seed()
            self.weight.append(random.random())

    def activation_func(self, vector):
        """Threshold activation function returns 1 if net is greater or equals 0.

        Parameters
        ----------
        vector : MyVector
            input vector that will be classified by this perceptron.

        Returns
        -------
        1 : int
            if is activated.
        0 : int
            if is not activated.
        """
        if self.net(vector) >= 0:
            return 1
        else:
            return 0

    def net(self, vector):
        """Dot product minus teta

        Parameters
        ----------
        vector : MyVector
            input vector that will be classified by this perceptron.

        Returns
        -------
        net : float
            Dot product minus teta.
        """
        net = 0.0

        for i in range(len(vector.data)):
            net += vector.data[i] * self.weight[i]

        net -= self.teta

        return net

    def new_weight(self, d, y, vector):
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

    def new_teta(self, d, y):
        """Calculates a new teta based on the formula "alfa * (d - y)"

        Parameters
        ----------
        d : int
            expected result
        y : int
            actual result
        """
        self.teta -= self.alfa * (d - y)

    def func(self, vector):
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
        y = self.activation_func(vector)
        if y == 1:
            return self.name
        else:
            return "Null"
