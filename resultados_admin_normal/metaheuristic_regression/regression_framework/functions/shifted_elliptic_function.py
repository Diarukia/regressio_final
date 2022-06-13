from regression_framework.functions.base_function import Base_function
import numpy as np
from cec2013lsgo.cec2013 import Benchmark


class Shifted_elliptic_function(Base_function):
    def __init__(self,name = 'Shifted_elliptic_function',lower_bound = -100,upper_bound = 100,dimension = 1000):
        super().__init__(name,lower_bound,upper_bound,dimension)
        self.bench = Benchmark()
        self.info = self.bench.get_info(1)
        self.dimension = self.info['dimension']
        self.calculus = self.bench.get_function(1)
        self.counter = 0

    def get_fitness(self,value):
        value = np.asarray_chkfinite(value)
        self.counter += 1
        self.reset()
        return self.calculus(value)

    def random_solution(self):
        aleatorio = self.info['lower']+np.random.rand(self.dimension)*(self.info['upper']-self.info['lower'])
        return aleatorio[0]

    def calcule_fitness(self,value):
        #return self.get_fitness([value for x in range(self.dimension)])
        return self.get_fitness(np.full((1000), value, dtype=np.float64)  )

    def reset(self):
        if(self.counter > 1000000):
            self.__init__()