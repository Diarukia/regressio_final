from regression_framework.functions.base_function import Base_function
import numpy as np
import random
import math
class Hartman_family_function_2(Base_function):
    def __init__(self,name = 'Hartman_family_function_2',lower_bound = 0,upper_bound = 1,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = value
        a = [[10,3,17,3.5,1.7,8],
             [0.05,10,17,0.1,8,14],
             [3,3.5,1.7,10,17,8],
             [17,8,0.05,10,0.1,14]]
        c = [1, 1.2, 3, 3.2]
        p = [[0.131,0.169,0.556,0.012,0.828,0.588],
             [0.232,0.412,0.830,0.373,0.100,0.999],
             [0.234,0.141,0.352,0.288,0.304,0.665],
             [0.404,0.882,0.873,0.574,0.109,0.038]]
        sum = 0
        for i in range(4):
            sumint = 0
            for j in range(6):
                sumint += a[i][j] * ((x[j] - p[i][j]) ** 2)
            sumint = -sumint
            sum += c[i] * math.exp(sumint)
        return -sum

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution