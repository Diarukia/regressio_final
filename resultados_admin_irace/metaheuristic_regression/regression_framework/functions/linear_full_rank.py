from regression_framework.functions.base_function import Base_function
import numpy as np

class Linear_full_rank(Base_function):
    def __init__(self,name = 'Linear_full_rank',lower_bound = -100,upper_bound = 100,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        #i = np.array(np.arange(1,self.dimension+1))
        #return self.dimension + np.sum(list(map(lambda x,y: np.cos(x)+y*(1-np.cos(x)-np.sin(x)),x,i)))
        m = 100
        m2 =  2 / m
        m4 = 2 * m2
        n = len(x)
        sum_x = np.sum(x)
        msx = m2 * sum_x + 1
        fi = x - msx
        fnm = -msx
        return np.sum(fi * fi) + (m - n) * fnm * fnm




