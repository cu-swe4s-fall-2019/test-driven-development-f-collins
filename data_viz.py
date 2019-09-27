import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt 
import math_lib as ml

def boxplot(L, out_file_name):
    if out_file_name == None:
        return None

    fig = plt.figure(figsize=(5, 5), dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(L)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " + str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    if out_file_name == None:
        return None

    fig = plt.figure(figsize=(5, 5), dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L, bins=10)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " + str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')

def combo(L, out_file_name):
    if out_file_name == None:
        return None

    fig = plt.figure(figsize=(8, 5), dpi=300)

    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(L)

    ax = fig.add_subplot(1, 2, 2)
    ax.hist(L, bins=10)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " + str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')
