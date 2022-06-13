from abc import ABC, abstractmethod
from regression_framework.utils import save_fitness_data ,save_general_comparation
import pandas as pd
import numpy as np
import random
import warnings
import logging
import time
class Regression_model_base:
    def __init__(self,optimization_problem):
        self.optimization_problem = optimization_problem
        self.metaheuristic_target = None
        self.infactsol = 0
        self.factsol = 0
        self.imprperc = 0
        self.parameter_model = {'PercFactSol': list(), 'PercInfactSol' : list(), 'ImprPerc' : list()}
        self.roulette = [0.2,0.2,0.2,0.2,0.2]
        self.total_iteration = 1000
        self.values = list()
        self.fitness = list()

    def run_model(self,beta,save_general_data = None,current_values = None):
        #current_values = current_values
        time_all = time.time()
        contador = 0
        while(self.total_iteration > 0):
            if(self.total_iteration/ beta >= 1 ):
                current_values = self.metaheuristic_target.run_metaheuristic(self.metaheuristic_target.poblation_number,self.metaheuristic_target.poblation_values,self.optimization_problem.name,self.save_data)
                self.total_iteration -= beta
            else:
                current_values = self.metaheuristic_target.run_metaheuristic(self.metaheuristic_target.poblation_number,self.metaheuristic_target.poblation_values,self.optimization_problem.name,self.total_iteration,self.save_data)
                self.total_iteration -= self.total_iteration
            self.regression_model()
            self.normalize(self.roulette)
            contador += 1
        time_all = (time.time() - time_all )
        #save_general_comparation(self.fitness,time_all,self.optimization_problem.name) # descomentar para solo correr la regresion sola
        save_fitness_data(self.fitness,self.values,self.optimization_problem.name)
        self.total_iteration = 100
        #print('el mejor es valor es', current_values[0])
        save_general_data(self.values,self.fitness)
        print('best fitness : ',np.min(self.fitness))
        print('peor fitness : ',np.max(self.fitness))
        print()
        self.fitness = list()
        self.values = list()
        self.parameter_model = {'PercFactSol': list(), 'PercInfactSol' : list(), 'ImprPerc' : list()}
        return current_values,current_values[0]

    def aceptation_criteria(self, value_1, value_2, kind = 0):
        if(kind == 0):
            if self.optimization_problem.calcule_fitness(value_1)<self.optimization_problem.calcule_fitness(value_2):
                self.factsol += 1
                return True
            else:
                self.infactsol += 1
                return False
        else:
            if self.optimization_problem.calcule_fitness(value_1)<self.optimization_problem.calcule_fitness(value_2):
                self.imprperc = abs(self.optimization_problem.calcule_fitness(value_1)-self.optimization_problem.calcule_fitness(value_2))/   (self.optimization_problem.calcule_fitness(value_1)+0.1)
            self.save_regression_info()
        return True

    def roulette_function(self,poblation_number,poblation_values,current_iterations,random_solution):
        if(current_iterations % 10 == 0):
            n = random.random()
            amount = 0
            for i in range(5):
                n = n-self.roulette[i]
                amount = amount + 20
                if n <= 0:
                    break
            poblation_number = amount
            poblation_values = self.modify_poblation(poblation_number,poblation_values,random_solution)
        return poblation_number,poblation_values

    def modify_poblation(self,poblation_number,poblation_values,random_solution):
        while(poblation_number < len(poblation_values)):
            poblation_values.pop()
        while(poblation_number > len(poblation_values)):
            poblation_values.append(random_solution())
        return poblation_values

    def save_regression_info(self):
        self.parameter_model['PercFactSol'].append(self.factsol/(self.factsol+self.infactsol))
        self.parameter_model['PercInfactSol'].append(self.infactsol/(self.factsol+self.infactsol))
        self.parameter_model['ImprPerc'].append(abs(self.imprperc))
        
    def regression_model(self):
        regr = self.regression_function()
        X,Y = self.processing_data(regr)
        self.roulette[0]= regr.predict([[X.iloc[0]['PercFactSol'],X.iloc[0]['PercInfactSol']]])
        self.roulette[1]= regr.predict([[X.iloc[1]['PercFactSol'],X.iloc[1]['PercInfactSol']]])
        self.roulette[2]= regr.predict([[X.iloc[2]['PercFactSol'],X.iloc[2]['PercInfactSol']]])
        self.roulette[3]= regr.predict([[X.iloc[3]['PercFactSol'],X.iloc[3]['PercInfactSol']]])
        self.roulette[4]= regr.predict([[X.iloc[4]['PercFactSol'],X.iloc[4]['PercInfactSol']]])

    @abstractmethod
    def regression_function(self):
        pass
        
    def processing_data(self,regr):
        aux_df = pd.DataFrame()
        df = pd.DataFrame(self.parameter_model,columns=['PercFactSol', 'PercInfactSol','ImprPerc'])
        df = df.replace([np.inf, -np.inf], np.nan).dropna(how='any')
        df = df.fillna(0)
        regr.fit(df[['PercFactSol', 'PercInfactSol']],df['ImprPerc'])
        for i in range(5):
            max_row = df.iloc[df['ImprPerc'].idxmax()].to_frame().T
            df = df.drop(df.index[[df['ImprPerc'].idxmax()]])
            aux_df = pd.concat([max_row, aux_df], ignore_index=True)
            df2 = pd.DataFrame([[0]*df.shape[1]],columns=df.columns)
            df = df.append(df2, ignore_index=True)
        X = aux_df[['PercFactSol', 'PercInfactSol']]
        Y = aux_df['ImprPerc']
        return X,Y

    def normalize(self,roulette):
        roulette_sum = np.sum(np.absolute(roulette))
        for i in range(len(roulette)):
            with warnings.catch_warnings():
                warnings.filterwarnings('error')
                try:
                    roulette[i] = abs(roulette[i])/roulette_sum
                except Warning as e:
                    roulette[i] = 0

    def save_data(self,poblation):
        for i in poblation:
            self.values.append(i)
            self.fitness.append( self.optimization_problem.calcule_fitness(i))
