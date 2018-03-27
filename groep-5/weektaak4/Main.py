#Auteur Tom
import os
from tkinter.filedialog import askopenfilenames
import pickle
import matplotlib.pyplot as plt
import re
import collections
def openfiles():
    for filename in askopenfilenames(initialdir="C:\\Users\\Tom\\Desktop\\Weektaak4\\weektaak4", title="Select files"):
        readfiles(filename)

def readfiles(filepath):
    '''
    Functie accepteerd een filepath en zorgt voor het openen van dit bestand.
    Daarna zal deze functie de headers en sequenties scheiden in 2 verschillende lijsten.
    Deze lijsten, samen met de filename worden naar de codoncounter gestuurd.
    '''
    headers = []
    seqs = []
    tempseq = ''
    #pause = input("".join((filepath.split('\\'))[-1:]))    # Deze lijn was/is voor debuggen
    with open(filepath) as file:
        for line in file:
            if line[0] == '>':
                headers.append(line.rstrip())
                if tempseq != '':
                    seqs.append(tempseq)
                    tempseq = ''
            else:
                tempseq += line.rstrip()
        seqs.append(tempseq)
    aminocounter(headers, seqs, "".join((filepath.split('/'))[-1:]))

def aminocounter(headers, seqs, filename):
    input("{} druk op enter om door te gaan".format(filename))
    seqlijst = ''
    tempcount = 0
    for x in range(len(headers)):
        if 'Env' not in headers[x]:
            seqlijst += seqs[x]
    aminocount = collections.Counter(seqlijst)
    print(aminocount)
    meestamino = str(input('Geef de 3 meestgebruikte aminozuren').upper())
    minstanimo = str(input('Geef de 3 minstgebruikte aminozuren').upper())

    percent_cys = round(seqlijst.count('C')/len(seqlijst)*100, 2)
    percent_tryp = round(seqlijst.count('W')/len(seqlijst) * 100, 2)

    for character in "AFGILMPV":
        tempcount += seqlijst.count(character)
    percent_phobic = tempcount/len(seqlijst)*100

    tempcount = 0
    for character in "DEHKNQRST":
        tempcount += seqlijst.count(character)
    percent_phylic = tempcount/len(seqlijst)*100

    tempcount = 0
    for character in meestamino:
        tempcount += seqlijst.count(character)
    percent_most_used = tempcount/len(seqlijst)*100

    tempcount = 0
    for character in minstanimo:
        tempcount += seqlijst.count(character)
    percent_least_used = tempcount/len(seqlijst)*100
    print()
    print('Percentage Cys =', percent_cys)
    print('Percentage Tryp = ', percent_tryp)
    print()
    print('Percentage Phobic = ', round(percent_phobic, 2))
    print('Percentage Phylic = ', round(percent_phylic,2))
    print()
    print('Percentage 3 meestgebruikt = ', round(percent_most_used,2))
    print('Percentage 3 minstgebruikt = ', round(percent_least_used,2))
    print()
    print('De 3 meestgebruikte aminozuren zijn', meestamino)
    print('De 3 minstgebruikte aminozuren zijn', minstanimo)
    print()
openfiles()

