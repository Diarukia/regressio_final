from regression_framework.functions.base_function import Base_function

import numpy as np

class Penalty_I_function(Base_function):
    def __init__(self, name = 'Penalty_I_function', lower_bound = -100, upper_bound = 100, dimension = 160):
        super().__init__(name, lower_bound, upper_bound, dimension)
        self.count = 0
    
    def get_fitness(self, x):
        #self.count += 1
        #print(self.count)

        a = 10 ** -5
        sqrta = np.sqrt(a)
        fsum = 0
        fn1 = 0
        for i in range(self.dimension):
            fsum = fsum + (sqrta * (x[i] - 1)) * (sqrta * (x[i] - 1))
            fn1 = fn1 + x[i] * x[i]
        fn1 = fn1 - 0.25
        fsum = fsum + fn1 * fn1
        return fsum
