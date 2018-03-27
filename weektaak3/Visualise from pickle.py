#Auteur Tom
import pickle
from tkinter.filedialog import askdirectory
import matplotlib.pyplot as plt
import numpy as np
import os

def openfiles():
    searchterm = ".dat" #input("Wat moet er in de bestandsnaam staan?: ")
    for path, dirs, files in os.walk(askdirectory()):
        for subfile in files:
            if searchterm in subfile:
                newpath = path + "\\" + subfile
                visualize(newpath)


def visualize(file):
    #Magie
    with open(file, "rb") as filething:
        data = pickle.load(filething)
    file = file[:-4]
    width = 0.8 # the width of the bars
    color_iter = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'm', 'c', 'r']
    fig, ax = plt.subplots(figsize=(15, 7))
    start = 0
    labels = []
    for color, values in data.items():
        rects = ax.bar(np.arange(start, start + len(values[1])),
                       values[1],
                       color=next(color_iter),
                       tick_label=values[0],
                       width = width)
        labels.extend(values[0])
        start += len(values[1])
    plt.title(''.join((file.split('\\'))[-1:]))
    ax.xaxis.set_ticks(np.arange(0, start))
    ax.xaxis.set_ticklabels(labels, rotation=70)

    plt.setp(ax.get_xticklabels(),fontsize=10)
    #plt.show()
    plt.savefig("{}.png".format(''.join((file.split('\\'))[-1:]), bbox_inches='tight'))

openfiles()