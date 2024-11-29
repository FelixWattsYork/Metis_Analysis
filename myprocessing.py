#!/usr/bin/env python3

import scipy.io
import numpy as np
from matplotlib import pyplot as plt
import sys

sys.path.insert(1,"C:/Users/qxp518/OneDrive - University of York/Documents/data lab/MCF/in flight tokomak/P0-P10-20241129T114812Z-001/P0-P10")
full_dataset = scipy.io.loadmat("C:/Users/qxp518/OneDrive - University of York/Documents/data lab/MCF/in flight tokomak/P0-P10-20241129T114812Z-001/P0-P10/P39.5_B1_Idefault_Ndefault.mat")


def list_subsections():
    print("subsections (I'm using zerod by default):")
    print(full_dataset['post'].dtype)


def list_indexes(subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(full_dataset['post']['zerod'][0][0].dtype)


def get_variable(index, subsection='zerod'):
    a = full_dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(start, end, index, subsection='zerod'):
    a = get_variable(index, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))
def slice(array):
    ''' return the central half of array'''
    l = len(array)
    q = int(l/4)
    qu = int(3*q/4)
    spliced1 = array[q:]
    spliced2 = spliced1[:q]
    return spliced2
def plvar(array):
    ''' splices the array into the central hald and then takes the average'''
    array1 = slice(array)
    ave = np.nanmean(array1)   
    return ave    
    

list_subsections()
list_indexes()
print(get_average(50, 100, 'te0'))
plt.plot(get_variable('te0'))
plt.show()

plt.figure(2)

ni = np.array(get_variable('ni0'))
Te0 = np.array(get_variable('te0'))    # I do not know if this is the right variable
tite = np.array(get_variable('tite'))

Ti = Te0*tite

 
#Ti = tite*Te0
taue = np.array(get_variable('taue'))
PNBI = np.array(get_variable('pnbi'))
ave_P = plvar(PNBI)
ave_ni = plvar(ni)
ave_ti = plvar(Ti)
ave_taue = plvar(taue)

def pull_var(file_String):
    ''' pulls the variables from a file and returns triple product and Power
    of neutral beam injector'''
    full_dataset = scipy.io.loadmat(file_String)
    ni = np.array(get_variable('ni0'))
    Te0 = np.array(get_variable('te0'))    # I do not know if this is the right variable
    tite = np.array(get_variable('tite'))

    Ti = Te0*tite #Ti = tite*Te0
    taue = np.array(get_variable('taue'))
    PNBI = np.array(get_variable('pnbi'))   
    ave_P = plvar(PNBI)
    ave_ni = plvar(ni)
    ave_ti = plvar(Ti)
    ave_taue = plvar(taue) 
    triple = ave_taue*ave_ni*ave_ti
    return ave_P, triple
