#!/usr/bin/env python3

import matplotlib
matplotlib.use('TkAgg')  # Switch to an interactive backend
import scipy.io
import numpy as np
from matplotlib import pyplot as plt



def list_subsections(full_dataset):
    print("subsections (I'm using zerod by default):")
    print(full_dataset['post'].dtype)


def list_indexes(full_dataset,subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(full_dataset['post']['zerod'][0][0].dtype)


def get_variable(full_dataset,index, subsection='zerod'):
    a = full_dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(full_dataset,start, end, index, subsection='zerod'):
    a = get_variable(full_dataset,index, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))


if __name__ == "__main__":
    full_dataset = scipy.io.loadmat("Complete/P1.5_B1_Idefault_Ndefault.mat")
    list_subsections(full_dataset)
    list_indexes(full_dataset)
    print(get_average(full_dataset,50, 100, 'tite'))
    tio = np.array(get_variable(full_dataset,'tite'))*np.array(get_variable(full_dataset,'te0'))
    nio = np.array(get_variable(full_dataset,'ni0'))
    taue = np.array(get_variable(full_dataset,"taue"))
    tripple_product= tio*nio*taue
    print(np.mean(tripple_product[50:100]))
    plt.plot(tripple_product)
    plt.show()


