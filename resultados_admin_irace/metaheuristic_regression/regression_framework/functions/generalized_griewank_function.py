from regression_framework.functions.base_function import Base_function
from numpy import cos,sqrt,prod
import numpy as np
import random

class Generalized_griewank_function(Base_function):
    def __init__(self,name = 'Generalized_griewank_function',lower_bound = -600,upper_bound = 600,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value, fr=4000):
        x = np.asarray_chkfinite(value)
        n = len(x)
        j = np.arange(1., n+1 )
        s = sum(x**2)
        p = prod(cos(x / sqrt(j)))
        return s/fr - p + 1

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution