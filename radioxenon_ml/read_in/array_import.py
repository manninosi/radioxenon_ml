"""
Created on Fri Apr 20 13:00:43 2018

@author: Steven
Topic: array importer
"""
import numpy as np


def load_2d_coinc_spectrum(inputfile):
    """
    Reads the "inputfile" text file
    Note: must be CSV and UTF-8 currently
    """    
    coincidence_array = np.genfromtxt(inputfile, delimiter = ',', dtype='int')
    return coincidence_array


def vector_spectrum(inputarray):
    """
    Takes the matrix that was loaded friom matlab and turns it into an nx1 matrix
    Outputs the vector, as well as the rows and columns of said vector
    """
    [rows,columns] = inputarray.shape
    vec_spec = np.reshape(inputarray,[rows*columns,1])
    return vec_spec, rows, columns
    