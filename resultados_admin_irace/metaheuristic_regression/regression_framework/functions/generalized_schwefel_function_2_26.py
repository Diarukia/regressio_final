from regression_framework.functions.base_function import Base_function
from numpy import sqrt, sin
import numpy as np
import random

class Generalized_schwefel_function_2_26(Base_function):
    def __init__(self,name = 'Generalized_schwefel_function_2_26',lower_bound = -500,upper_bound = 500,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        return - sum(x * sin(sqrt(abs(x))))

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) + self.lower_bound
        return randomSolution