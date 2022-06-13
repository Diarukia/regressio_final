from regression_framework.functions.base_function import Base_function

import numpy as np

class Variably_dimensioned_function(Base_function):
    def __init__(self, name = 'Variably_dimensioned_function', lower_bound = -100, upper_bound = 100, dimension = 160):
        super().__init__(name, lower_bound, upper_bound, dimension)
    
    def get_fitness(self, x):
        fsum = 0
        fn1 = 0
        for i in range(0,self.dimension):
            fj = x[i] - 1
            fsum = fsum + fj * fj
            fn1 = fn1 + (i+1) * fj
        fn1_fn1 = fn1 * fn1
        fsum = fsum + fn1_fn1 + fn1_fn1 * fn1_fn1
        return fsum


