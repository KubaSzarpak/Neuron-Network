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

    def __weight_draw__(self, length):
        for i in range(length):
            random.seed()
            self.weight.append(random.random())

    def __activation_func__(self, vector):
        if self.__net__(vector) >= 0:
            return 1
        else:
            return 0

    def __net__(self, vector):
        net = 0.0

        for i in range(len(vector.data)):
            net += vector.data[i] * self.weight[i]

        net -= self.teta

        return net

    def __new_weight__(self, d, y, vector):
        for i in range(len(vector.data)):
            self.weight[i] = self.weight[i] + self.alfa * (d - y) * vector.data[i]

    def __new_teta__(self, d, y):
        self.teta -= self.alfa * (d - y)

    def __func__(self, vector):
        y = self.__activation_func__(vector)
        if y == 1:
            return self.name
        else:
            return "Null"
