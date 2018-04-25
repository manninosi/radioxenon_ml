"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
import sys

import test_functions as tf
from ..main_Copy import *
#from radioxenon.read_in.ml_matrix_composition import form_matrix



n=5
simulation_vec, experimental_vec, nrows, ncols = mlmc.form_matrix(n); 
tf.test_import_sizes(nrows, ncols,n)
        