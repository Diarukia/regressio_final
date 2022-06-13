from regression_framework.admins.base_admin import Base_admin
from sklearn.linear_model import LogisticRegression
from regression_framework.utils import save_general_comparation

import pandas as pd
import numpy as np
import random
import time


class Logistic_admin(Base_admin):
    def __init__(self,alpha,beta,models):
        super().__init__(alpha,beta,models)
        self.list_value = list()
        self.list_fitness = list()
        self.time_all = None
        self.results = {'model': list(), 'fitness' : list()}

    def run_admin(self):
        current_values = None
        regression = 0
        self.time_all = time.time()
        for i in range(10):
            if(i < 5):
                current_values,fitness = self.models[i].run_model(self.beta,self.save_general_data,current_values)
                self.results['model'].append(i)
                self.results['fitness'].append(fitness)
            elif(i >= 5):
                regression = self.execute_regression(i)
                model = regression
                current_values,fitness = self.models[model].run_model(self.beta,self.save_general_data,current_values)
                self.results['model'].append(model)
                self.results['fitness'].append(fitness)
            print('vamos en la iteracion ',i)
        self.time_all = (time.time() - self.time_all )
        print('best fitness : ',min(self.list_fitness))
        print('worst fitness : ',max(self.list_fitness))
        save_general_comparation(self.list_fitness,self.time_all,self.models[0].optimization_problem.name)

    def execute_regression(self,iteration):
        function = 0
        log = LogisticRegression(solver = 'lbfgs',max_iter = 32000)
        try:
            log.fit(self.results['model'],self.results['fitness'])
            function = log.predict(self.results['fitness'])[0]
        except ValueError:
            function = random.randint(0, 4)
        return function

    def save_general_data(self,values,fitness):
        self.list_value = self.list_value+values
        self.list_fitness = self.list_fitness+fitness

        