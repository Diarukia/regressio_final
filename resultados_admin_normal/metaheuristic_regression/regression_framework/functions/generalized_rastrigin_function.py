from regression_framework.functions.base_function import Base_function
from numpy import cos,pi
import numpy as np
import random

class Generalized_rastrigin_function(Base_function):
    def __init__(self,name = 'Generalized_rastrigin_function',lower_bound = -5.12,upper_bound = 5.12,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        n = len(x)
        return 10*n + sum(x**2 - 10 * cos(2 * pi * x))

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution
