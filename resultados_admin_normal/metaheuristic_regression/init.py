from regression_framework.utils import setup_logging
from regression_framework.main import __main__
#from cec2013lsgo.cec2013 import Benchmark
import numpy as np
import logging
import warnings
import sys
import time


if __name__ == "__main__":
    start_time = time.time()
    setup_logging()
    logging.info("Starting the regression framework")
    warnings.filterwarnings("ignore")
    #arguments = sys.argv
    __main__()
    print("--- %s seconds ---" % (time.time() - start_time))

