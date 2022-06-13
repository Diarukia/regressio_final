from regression_framework.functions.base_function import Base_function
import numpy as np
from cec2013lsgo.cec2013 import Benchmark

class One_separable_shifted_rotated_elliptic_function(Base_function):
    def __init__(self,name = 'One_separable_shifted_rotated_elliptic_function',lower_bound = -100,upper_bound = 100,dimension = 100):
        super().__init__(name,lower_bound,upper_bound,dimension)
        self.bench = Benchmark()
        self.info = self.bench.get_info(4)
        self.dimension = self.info['dimension']
        self.calculus = self.bench.get_function(4)
        self.counter = 0

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        self.counter += 1
        self.reset()
        return self.calculus(x)

    def random_solution(self):
        aleatorio = self.info['lower']+np.random.rand(self.dimension)*(self.info['upper']-self.info['lower'])
        return aleatorio[0]

    def calcule_fitness(self,value):
        #return self.get_fitness([value for x in range(self.dimension)])
        return self.get_fitness(np.full((1000), value, dtype=np.float64)  )

    def reset(self):
        if(self.counter > 1000000):
            self.__init__()