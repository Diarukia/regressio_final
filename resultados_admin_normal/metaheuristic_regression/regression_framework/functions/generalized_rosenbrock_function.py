from regression_framework.functions.base_function import Base_function
import random
import numpy as np

class Generalized_rosenbrock_function(Base_function):
    def __init__(self,name = 'Generalized_rosenbrock_function',lower_bound = -30,upper_bound = 30,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        """ http://en.wikipedia.org/wiki/Rosenbrock_function """
        # a sum of squares, so LevMar (scipy.optimize.leastsq) is pretty good
        x = np.asarray_chkfinite(value)
        x0 = x[:-1]
        x1 = x[1:]
        return sum((1 - x0) **2)+100 * sum((x1 - x0**2)**2)

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution