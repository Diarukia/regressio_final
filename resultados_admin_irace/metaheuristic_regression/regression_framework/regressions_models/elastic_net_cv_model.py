from regression_framework.metaheuristics.sho import Sho
from sklearn.linear_model import ElasticNetCV
from regression_framework.regressions_models.regression_model_base import Regression_model_base
import random
import time

class Elastic_net_cv_model(Regression_model_base):
    def __init__(self,optimization_problem):
        super().__init__(optimization_problem)
        self.metaheuristic_target = Sho(self.optimization_problem.calcule_fitness,self.aceptation_criteria,0.1158,25,self.optimization_problem.random_solution,self.roulette_function)

    def regression_function(self):
        return ElasticNetCV(max_iter = 32000)