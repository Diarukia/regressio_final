from regression_framework.metaheuristics.sho import Sho
from sklearn.linear_model import Lasso
from regression_framework.regressions_models.regression_model_base import Regression_model_base
import random
import time

class Lasso_model(Regression_model_base):
    def __init__(self,optimization_problem):
        super().__init__(optimization_problem)
        self.metaheuristic_target = Sho(self.optimization_problem.calcule_fitness,self.aceptation_criteria,0.1415,25,self.optimization_problem.random_solution,self.roulette_function)
        # 0.1158 irace
        # basico es 0.1415
    def regression_function(self):
        return Lasso(alpha=0.1,max_iter = 32000)
