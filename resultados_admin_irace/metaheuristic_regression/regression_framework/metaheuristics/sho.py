from regression_framework.metaheuristics.metaheuristic_base import Metaheuristic_poblation_base
from functools import cmp_to_key
import numpy as np

class Sho(Metaheuristic_poblation_base):
    def __init__(self,calcule_fitness,aceptation_criteria,h,poblation_number,random_solution,roulette_function,poblation_values = list()):
        super().__init__(calcule_fitness,random_solution,poblation_number,poblation_values,aceptation_criteria,roulette_function)
        self.h = h
        self.current_iterations = 0
    
    def run_metaheuristic(self,poblation_number,poblation_values,name,save_data,number_iterations = 100):
        if(name == 'Branin_function'):
            poblation_values= self.random_fill(poblation_number,poblation_values)
            poblation_values.sort()
            e = [0,0]
            b = [0,0]
            e[0] = 2*self.random_solution()[0]*self.h-self.h
            e[1] = 2*self.random_solution()[1]*self.h-self.h
            b[0]=2*self.random_solution()[0]
            b[1]=2*self.random_solution()[1]
            optimal_solutions = list() # ch
            best_solution_current = poblation_values[0]
            best_fitness_current = poblation_values[0]
            nuevaRana = [0,0]
            while(self.current_iterations < number_iterations):
                poblation_number,poblation_values = self.roulette_function(poblation_number,poblation_values,self.current_iterations,self.random_solution)
                for i in range(poblation_number):
                    pk = poblation_values[0]
                    nuevaRana[0]=best_solution_current[0]-(e[0]*((b[0]*best_solution_current[0])-pk[0])) # 10 equation
                    nuevaRana[1]=best_solution_current[0]-(e[1]*((b[1]*best_solution_current[1])-pk[1]))
                    pk = nuevaRana

                    if(self.aceptation_criteria(pk,poblation_values[i]) == False):
                        pk = poblation_values[i]
                    optimal_solutions.append(pk)
                for i in range(len(optimal_solutions)):
                    atake = [0,0]
                    pk = poblation_values[0]
                    actualrana=optimal_solutions[i]
                    atake[0] =actualrana[0] / len(optimal_solutions)
                    atake[1] =actualrana[1] / len(optimal_solutions)
                    pk=atake
                    if(self.aceptation_criteria(pk,optimal_solutions[i]) == True):
                        poblation_values[i]=pk
                    else:
                        poblation_values[i]=optimal_solutions[i]
                self.h = self.h - (self.current_iterations / number_iterations)
                #e = 2*self.random_solution()*self.h-self.h
                #b=2*self.random_solution()

                e[0] = 2*self.random_solution()[0]*self.h-self.h
                e[1] = 2*self.random_solution()[1]*self.h-self.h
                b[0]=2*self.random_solution()[0]
                b[1]=2*self.random_solution()[1]

                poblation_values.sort()
                if(self.aceptation_criteria(poblation_values[0],best_fitness_current,1) == True):
                    best_solution_current = poblation_values[0]
                    best_fitness_current = poblation_values[0]
            
                self.current_iterations += 1
                optimal_solutions = list()
                #save_data(poblation_values)

        else:
            poblation_values = self.random_fill(poblation_number,poblation_values)
            sorted(poblation_values,key=cmp_to_key(self.compare))
            #poblation_values.sort(key=self.compare,reverse=False)
            #poblation_values = self.ordenar_hienas(poblation_values)
            #poblation_values = poblation_values.sort(key = self.compare)
            e = (2*self.random_solution()*self.h)-self.h
            b=2*self.random_solution()
            optimal_solutions = list() # ch
            best_solution_current = poblation_values[0]
            best_fitness_current = poblation_values[0]
            while(self.current_iterations < number_iterations):
                poblation_number,poblation_values = self.roulette_function(poblation_number,poblation_values,self.current_iterations,self.random_solution)
                for i in range(poblation_number):
                    pk = poblation_values[i]
                    #nuevaRana=best_solution_current-(e*((b*best_solution_current)-pk)) # 10 equation
                    nuevaRana=np.subtract(best_solution_current, e*np.subtract(b*best_solution_current,pk) )
                    pk = nuevaRana
                    if(self.aceptation_criteria(pk,poblation_values[i]) == False):
                        pk = poblation_values[i]
                    optimal_solutions.append(pk)
                for i in range(len(optimal_solutions)):
                    pk = poblation_values[i]
                    atake = 0
                    actualrana=optimal_solutions[i]
                    atake=actualrana / len(optimal_solutions)
                    pk=atake
                    if(self.aceptation_criteria(pk,optimal_solutions[i]) == True):
                        poblation_values[i]=  self.redondear(pk,name)
                    else:
                        poblation_values[i]= self.redondear(optimal_solutions[i],name)
                self.h = self.h - (self.current_iterations / number_iterations)
                e = 2*self.random_solution()*self.h-self.h
                b=2*self.random_solution()
                #poblation_values = self.ordenar_hienas(poblation_values)
                sorted(poblation_values,key=cmp_to_key(self.compare))
                #poblation_values.sort(key=self.compare,reverse=False)
                if(self.aceptation_criteria(poblation_values[0],best_fitness_current,1) == True):
                    best_solution_current = poblation_values[0]
                    best_fitness_current = poblation_values[0]
            
                self.current_iterations += 1
                optimal_solutions = list()
                #print(self.current_iterations)
                save_data(poblation_values)
                
        self.current_iterations = 0
        self.poblation_values = poblation_values
        #return self.ordenar_hienas(poblation_values)
        return poblation_values

    def ordenar_hienas(self,poblation_values):
        for i in range(len(poblation_values)-1):
            if( self.calcule_fitness(poblation_values[i+1])  < self.calcule_fitness(poblation_values[i])  ):
                aux = poblation_values[i]
                poblation_values[i] = poblation_values[i+1]
                poblation_values[i+1]= aux
        return poblation_values

    def redondear(self,number,name):
        if(name == 'Generalized_schwefel_function_2_26'):
            return (number % 1)*500
        return number

    def compare(self,item1, item2):
        if self.calcule_fitness(item1) < self.calcule_fitness(item2):
            return -1
        elif self.calcule_fitness(item1) > self.calcule_fitness(item2):
            return 1
        return 0
    
    """def compare(self,x):
        print(x)
        return self.calcule_fitness(x)"""


