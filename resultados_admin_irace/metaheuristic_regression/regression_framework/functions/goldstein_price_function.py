from regression_framework.functions.base_function import Base_function
import numpy as np
import random


class Goldstein_price_function(Base_function):
    def __init__(self,name = 'Goldstein_price_function',lower_bound = -2,upper_bound = 2,dimension = 2):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = value
        x[0] = x[0]
        x[1] = x[1]
        return (1+((x[0]+x[1]+1)**2)*(19-14*x[0]+3*(x[0]**2)-14*x[1]+6*x[0]*x[1]+3*(x[1]**2)))*(30+((2*x[0]-3*x[1])**2)*(18-32*x[0]+12*(x[0]**2)+48*x[1]-36*x[0]*x[1]+27*(x[1]**2)))

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) + self.lower_bound
        return randomSolution