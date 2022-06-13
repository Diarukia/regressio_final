from regression_framework.functions.base_function import Base_function
import numpy as np

class Extended_rosenbrock_function(Base_function):
    def __init__(self,name = 'extended_rosenbrock_function',lower_bound = -30,upper_bound = 30,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        odd = x[::2]
        even = x[1::2]
        return 100 * np.square(  np.subtract(even , np.square(odd))  ).sum() + np.square(   np.subtract(1 , odd)   ).sum()