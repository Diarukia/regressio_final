import logging
import sys
import numpy as np
import pandas as pd
import statistics
import os

def setup_logging():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO , filename='framework.log')


def save_general_comparation(values,time,function_name):
    media_to_csv = statistics.mean(values)
    time_to_csv = time
    funcion = function_name
    desviacion_estandar = np.std(values)
    df = pd.DataFrame({'funciones' : funcion, 'media' : media_to_csv, 'desviacion estandar' : desviacion_estandar ,'tiempo' : time_to_csv},index=[0])
    df.to_excel(function_name+"_general.xlsx")

def save_fitness_data(fitness,value,function_name):
    counter = 1
    #df.to_excel('iteration_'+str(iteration)+'_'+function_name+"_fitness.xlsx")
    while(True):
        if(os.path.isfile("../2/"+'iteration_'+str(counter)+'_'+function_name+"_fitness.xlsx")  == False):
            df = pd.DataFrame({'fitness' : fitness, 'value' : value,'iteration' : counter})
            df.to_excel('iteration_'+str(counter)+'_'+function_name+"_fitness.xlsx")
            break
        counter += 1
    df = pd.DataFrame({'fitness' : list(), 'value' : list(),'iteration' : list()})
    



