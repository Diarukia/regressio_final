from regression_framework.functions.base_function import Base_function
from numpy import pi,cos,exp,sqrt
import numpy as np
import random

class Ackley_function(Base_function):
    def __init__(self,name = 'Ackley_function',lower_bound = -32,upper_bound = 32,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value,a=20, b=0.2, c=2*pi):
        x = np.asarray_chkfinite(value)  # ValueError if any NaN or Inf
        n = len(x)
        s1 = sum(x**2)
        s2 = sum(cos(c * x))
        return -a*exp(-b*sqrt(s1 / n)) - exp(s2 / n) + a + exp(1)

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution
