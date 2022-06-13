from regression_framework.functions.base_function import Base_function
import numpy as np
import random
import math

class Hartman_family_function_1(Base_function):
    def __init__(self,name = 'Hartman_family_function_1',lower_bound = 0,upper_bound = 1,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = value
        a=[[3,10,30],
           [0.1,10,35],
           [3,10,30],
           [0.1,10,30]]
        c=[1,1.2,3,3.2]
        p=[[0.3689,0.1170,0.2673],
           [0.4699,0.4387,0.7470],
           [0.1091,0.8732,0.5547],
           [0.03815,0.5743,0.8828]]
        sum=0
        for i in range(4):
            sumint=0
            for j in range(3):
                sumint+=a[i][j]*((x[j]-p[i][j])**2)
            sumint= -sumint
            sum+= c[i]*math.exp(sumint)
        return -sum

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution