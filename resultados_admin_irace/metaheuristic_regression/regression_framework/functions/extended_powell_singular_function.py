from regression_framework.functions.base_function import Base_function
import numpy as np

class Extended_powell_singular_function(Base_function):
    def __init__(self,name = 'Extended_powell_singular_function',lower_bound = -100,upper_bound = 100,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        x1 = x[0::4]
        x2 = x[1::4]
        x3 = x[2::4]
        x4 = x[3::4]
        return np.square(x1 + 10 * x2).sum() + 5 * np.square(  np.subtract(x3 , x4)  ).sum()  + np.power( np.subtract(x2 , 2 * np.square(x3)), 4).sum() + 10 * np.power(np.subtract(x1 , x4), 4).sum()
