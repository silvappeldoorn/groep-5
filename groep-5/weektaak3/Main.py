#Auteur Tom
import os
from tkinter.filedialog import askdirectory
import pickle
import matplotlib.pyplot as plt
import re

def openfiles():
    '''
    Openen van een folder voor het zoeken naar bestanden.
    Als het zoekwoord (Variabele searchterm) in de bestandnaam zit stuurt die hem door naar de readfiles functie.
    '''
    searchterm = "CDS.fasta" #input("Wat moet er in de bestandsnaam staan?: ")
    for path, dirs, files in os.walk(askdirectory()):
        for subfile in files:
            if searchterm in subfile:
                newpath = path + "\\" + subfile
                readfiles(newpath)

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
    codoncounter(headers, seqs, "".join((filepath.split('\\'))[-1:]))

def codoncounter(headers, seqs, filename):
    '''
    Accepteerd een header en sequentielijst samen met de filename.
    Met behulp van een codon dictionary worden de sequenties doorzocht voor codons.
    De gevonden codons worden aan een andere dictionary toegevoegd.
    De aangemaakte dictionary gaat naar de dictprocessor functie om verder te worden verwerkt en gesorteerd.
    '''
    start = 0
    stop = 3
    headercount = 0
    with open("TemplateDict.dat", "rb") as usagefile:
        usagedict = pickle.load(usagefile)
    with open("CodonDict.dat","rb") as CodonFile:
        codonDict = pickle.load(CodonFile)
    for seq in seqs:
        seq = seq.lower()
        if re.search("gene=env", headers[headercount]) == None: #aanpassen als je ENV zoekt of wat anders.
            for x in range(int((len(seq)-len(seq)%3)/3)):
                for key in codonDict:
                    if key == seq[start:stop]:
                        try:
                            usagedict[codonDict[key]].append("{} {}".format(codonDict[key], key))
                        except KeyError:
                            usagedict[codonDict[key]] = ["{} {}".format(codonDict[key], key)]
                        start+=3
                        stop +=3
                        break

        headercount += 1
        start = 0
        stop = 3
    dictprocessor(usagedict, "="*40, filename)

def dictprocessor(usagedict, header, filename):
    '''
    De dictprocessor functie verwerkt de voorheen gemaakte dictionary tot een alfabetisch gesorteerde dictionary.
    De key:value paren zijn: Aminozuurletter:([codons],[aantalcodon]) voor (in theorie) makkelijke verwerking met matplotlib.
    Deze dictionary gaat naar de pickledump functie.
    '''
    tempcount = []
    tempcodon = []
    sorteddict = {}
    for key in usagedict:
        unsortedset = set(usagedict[key])
        sortedset = sorted(unsortedset)
        for thing in sortedset:
            tempcodon.append(thing)
            tempcount.append(usagedict[key].count(thing))
        sorteddict[key] = tempcodon,tempcount
        tempcount = []
        tempcodon = []
    pickledump(sorteddict, header, filename)


def pickledump(codondict, header, filename):
    '''
    Dumpt alle dictionaries naar een pickle bestand voor latere verwerking.
    '''
    with open("CodonUsageDict {}.dat".format("".join((filename.split('.'))[0])), "wb") as file:
        pickle.dump(codondict, file)

openfiles()

