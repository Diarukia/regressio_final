from regression_framework.functions.base_function import Base_function
from numpy import sin,pi
import numpy as np
import random
import math

class Generalized_penalized_function(Base_function):
    def __init__(self,name = 'Generalized_penalized_function',lower_bound = -50,upper_bound = 50,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value, fr=4000):
        x = np.asarray_chkfinite(value)
        sum1=0
        sum2=0
        for i in range(len(x)):
            y=self.yi(x[i])
            if(i<len(x)-1):
                sum1=((y-1)**2)*(1+10*(sin(math.pi*self.yi(x[i+1]))**2))
            else:
                sum1+= (y-1)**2
            sum2+= self.u(x[i],10,100,4)
        return (math.pi/len(x))*(10*sin(math.pi*self.yi(x[1]))+sum1)+sum2

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution

    def yi(self,x):
        return 1 + (x+1)/4

    def u(self,x,a,k,m):
        if(x<a):
            return k*(x-a)**m
        elif(x<-a):
            return k*(-x-a)**m
        else:
            return 0