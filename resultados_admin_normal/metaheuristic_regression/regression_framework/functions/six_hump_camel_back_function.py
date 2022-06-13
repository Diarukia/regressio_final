from regression_framework.functions.base_function import Base_function
import numpy as np
import random

class Six_hump_camel_back_function(Base_function):
    def __init__(self,name = 'Six_hump_camel_back_function',lower_bound = -5,upper_bound = 5,dimension = 2):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = value
        return 4*x[0]**2-2.1*x[0]**4+(1/3)*x[0]**6+x[0]*x[1]+4*x[1]**4-4*x[1]**2

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution