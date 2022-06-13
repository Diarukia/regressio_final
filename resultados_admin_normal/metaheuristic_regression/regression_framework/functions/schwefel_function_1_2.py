from regression_framework.functions.base_function import Base_function
import numpy as np
import random

class Schwefel_function_1_2(Base_function):
    def __init__(self,name = 'Schwefel_function_1_2',lower_bound = -100,upper_bound = 100,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.array(value)
        return np.sum([np.sum(x[:i]) ** 2
                   for i in range(len(x))])

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution