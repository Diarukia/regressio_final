from regression_framework.functions.base_function import Base_function
import numpy as np
import random

class Shekel_foxholes_function(Base_function):
    def __init__(self,name = 'Shekel_foxholes_function',lower_bound = -65.536,upper_bound = 65.536,dimension = 2):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        a=[[-32,-32],[-16,-32],[0,-32],[16,-32],[32,-32],[-32,-16],[-16,-16],[0,-16],[16,-16],[32,-16],[-32,0],[-16,0],[0,0],[16,0],[32,0],[-32,16],[-16,16],[0,16],[16,16],[32,16],[-32,32],[-16,32],[0,32],[16,32],[32,32]]
        sum=0
        x = np.asarray_chkfinite(value)
        for i in range(25):
            sumint=0
            for j in range(2):
                sumint+=(x[j]-a[i][j])**6
            sumint+= i
            sum+=(1/sumint)
        sum+=(1/500)
        sum=(1/sum)
        return sum+1

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution