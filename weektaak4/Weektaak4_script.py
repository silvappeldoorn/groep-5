#Auteur: Stijn de Wijse

import os
import re


def main():
    aminozuren = {"A":0, "R":0, "N":0, "D":0, "C":0,
                  "F":0, "Q":0, "E":0, "G":0, "H":0,
                  "I":0, "L":0, "K":0, "M":0, "P":0,
                  "S":0, "T":0, "W":0, "Y":0, "V":0}
    for file in [f for f in os.listdir() if re.match(".*\.fasta", f)]:
        headerlijst, seqlijst = readfiles(file)
        aminocount(headerlijst, seqlijst)
        hydrointeractie(headerlijst, seqlijst, aminozuren)    

def readfiles(file):
    file = open(file,'r')
    print(file)
    
    seq = ''
    headers = ''
    seqlijst = ''
    headerlijst = []
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            headers = line
            headerlijst.append(headers)
        if not line.startswith('>'):
            seq += line
        if line.startswith('>') and seq is not '':
            seqlijst += seq
            seq = ''
    seqlijst += seq
##    print(40* "*")
#    print(headerlijst)

    return headerlijst, seqlijst

def aminocount(headerlijst, seqlijst):
    Cysteine = "C"
    Tryptofaan = "W"
    cyscount = 0
    trpcount = 0
    i = 0
    for item in seqlijst:
        cys = seqlijst[i].count("C")
        trp = seqlijst[i].count("W")
        cyscount += cys
        trpcount += trp
        i += 1
##    print(cyscount)
##    print(trpcount)
##    print(40*"-")
    cyspercent = (cyscount/len(seqlijst))*100
    trppercent = (trpcount/len(seqlijst))*100
    print("Het percentage cysteine is: ", cyspercent)
    print("Het percentage tryptofaan is: ", trppercent)

def hydrointeractie(headerlijst,seqlijst,aminozuren):
    #print(seqlijst[0])
    foob = ["A","F","I","L","M","P","W","V"]
    fiel = ["R","N","D",'C','Q','E','G','H','K','S','T','Y']
    foobcount = 0
    fielcount = 0

    for amino in aminozuren:
        aminozuren[amino] = int(len(re.findall(amino,seqlijst)))
    for waarde in foob:
        foobcount+= aminozuren[waarde]
    for waarde2 in fiel:
        fielcount+= aminozuren[waarde2]

    
##    print('hydrofoob:', foobcount)
##    print('hydrofiel:', fielcount)
    

    foobpercent = (foobcount/len(seqlijst))*100
    fielpercent = (fielcount/len(seqlijst))*100

    print("Het percentage hydrofobe aminozuren is: ", foobpercent)
    print("Het percentage hydrofiele aminozuren is: ", fielpercent)
##    print(40* "-")
    valuesort = sorted(aminozuren.values())
    aminosort = sorted(aminozuren, key=aminozuren.get)
    print(aminosort[:3])
    print(valuesort[:3])
    print(aminosort[-3:])
    print(valuesort[-3:])

    for codon in valuesort[:3]:
        #print(codon)
        minpercent = (codon/len(seqlijst))*100
        
    for codon in valuesort[-3:]:
        maxpercent = (codon/len(seqlijst))*100
        

        print(maxpercent)
        print(minpercent)
        print(40*"#")


            
main()
