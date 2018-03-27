import matplotlib.pyplot as plt
import re
import os

def main():
    seq = inlezen()
    waardelijst,lijst = tellen(seq)
    grafiek(waardelijst,lijst)

def inlezen():
    file = open('identity.txt','r')
    seq = []

    for line in file:
        line = line.split('\t')
        for thing in line:
            thing = thing.strip().split(' ')
            for item in thing:
                if item != '':
                    if ":" not in item and '_' not in item and '-' not in item:
                        seq.append(item)
    return seq

def tellen(seq):
    waardelijst = []
    tellijst = []
    lijst = []
    
    i = 0
    k = 1
    while i != 100:
        for waarde in seq:
            if float(waarde) > i and float(waarde) <= k:
                tellijst.append(waarde)

        lijst.append(len(tellijst))
        tellijst = []
        waardelijst.append(i)
        i += 1
        k += 1
##    print(waardelijst)
##    print(lijst)
    return waardelijst,lijst

def grafiek(waardelijst,lijst):
    plt.bar(waardelijst,lijst)
    #plt.plot(waardelijst,lijst)
    plt.xlabel('Percentages in stappen van 1')
    plt.ylabel('Aantal matches')
    plt.title('%identity matches met stappen van 1 over 404 bestanden')
    plt.show()


main()
