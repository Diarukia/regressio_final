from abc import ABC, abstractmethod
import numpy as np
import random

class Base_function(ABC):
    def __init__(self,name,lower_bound,upper_bound,dimension):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimension = dimension

    @abstractmethod
    def get_fitness(self,value):
        pass

    def random_solution(self):
        #return self.lower_bound+np.random.rand(self.dimension)*(self.upper_bound-self.lower_bound)
        return self.lower_bound+random.random()*(self.upper_bound-self.lower_bound)


    def calcule_fitness(self, x):
        #return self.get_fitness(x)
        return self.get_fitness(np.full((self.dimension), x, dtype=np.float64)  )

    def get_info(self):
        print("Function name : ", self.name)
        print("Lower bound : ",self.lower_bound)
        print("Upper bound : ", self.upper_bound)
        print("Dimension : ", self.dimension)