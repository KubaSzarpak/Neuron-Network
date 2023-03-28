import math
import random


class Perceptron:
    def __init__(self, name, training_data):
        self.name = name
        self.training_data = training_data
        self.weight = []
        self.teta = 1.0
        self.alfa = 0.01

        self.learn()

    def learn(self):
        self.weight_draw(len(list(self.training_data[0].data)))
        E_max = 0.01
        E = 1.0
        i = 0

        while E >= E_max and i < 10000000:
            sum = 0.0
            for vector in self.training_data:
                y = self.activationFunc(vector)
                if vector.name == self.name:
                    d = 1
                else:
                    d = 0

                self.newWeight(d, y, vector)
                self.newTeta(d, y)

                sum += math.pow(d - y, 2)

            E = (1.0 / len(self.training_data)) * sum
            i += 1

    def weight_draw(self, length):
        for i in range(length):
            self.weight.append(random.random())

    def activationFunc(self, vector):
        if (self.Net(vector) >= 0):
            return 1
        else:
            return 0

    def Net(self, vector):
        net = 0.0

        for i in range(len(vector.data)):
            net += vector.data[i] * self.weight[i]

        net -= self.teta

        return net

    def newWeight(self, d, y, vector):
        for i in range(len(vector.data)):
            self.weight[i] = self.weight[i] + self.alfa * (d - y) * vector.data[i]

    def newTeta(self, d, y):
        self.teta -= self.alfa * (d - y)

    def func(self, vector):
        y = self.activationFunc(vector)

        if y == 1:
            return self.name
        else:
            return "Null"
