from abc import ABC, abstractmethod

class Base_admin(ABC):
    def __init__(self,alpha,beta,models):
        self.alpha = alpha
        self.beta = beta
        self.models = models
    
    @abstractmethod
    def run_admin(self):
        pass

    @abstractmethod
    def execute_regression(self):
        pass