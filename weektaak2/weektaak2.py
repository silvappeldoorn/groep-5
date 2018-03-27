import os
import re
import matplotlib.pyplot as plt
import statistics

def main():
    bp = int(input('Per hoeveel nucleotide wil je de sequenties sorteren?:'))

    for file in [f for f in os.listdir() if re.match(".*\.fasta", f)]:
        seq,file,headers = inlezen(file)
        gc_lijst,gcprocent = GC_berekenen(seq,file,bp)
        Grafiek(gc_lijst,bp,seq,headers,gcprocent)
    
def inlezen(file):
    file = open(file,'r')
    
    lengte = 0
    seq = ''
    headers = ''
    for line in file:
        if line.startswith('>'):
            headers += line
        else:
            line = line.rstrip()
            seq += line
            lengte += len(line)

    headers = (headers[13:44].replace(',',''))

    print(headers)

    return seq,file,headers

def GC_berekenen(seq,file,bp):
  
    gcprocent = round(((seq.count('C')+seq.count('G'))/(len(seq)-seq.count('N')))*100, 3)
    print('GC%:',gcprocent,'%')

    ratio = gcprocent/100    

    lijst = [seq[i:i+bp] for i in range(0, len(seq), bp)]

    gc_lijst = []
    
    #print(lijst)
    for waarde in lijst:
        #print(len(waarde))
        
        if waarde.count('N') != 0:    
            n = waarde.count('N')
            g = waarde.count('G')
            c = waarde.count('C')
        
            GC = round((((g + c) + n*(ratio)) /len(waarde)) *100,3)

            gc_lijst.append(GC)
            
        else:
            g = waarde.count('G')
            c = waarde.count('C')
            GC = round(((g + c) /len(waarde)) *100,3)
            gc_lijst.append(GC)
            
    #print(gc_lijst)  
    print('Mediaan:',statistics.median(gc_lijst))
    print('Variantie:',statistics.variance(gc_lijst))
    print(40*'-')
    return gc_lijst,gcprocent

def Grafiek(gc_lijst,bp,seq,headers,gcprocent):
    x_data = []
    lengte = 0
    tick_lijst = []
    i = bp

    for line in gc_lijst:
        if tick_lijst == []:
            tick_lijst.append(bp)
        else:
            i += bp
            tick_lijst.append(i)

    for stuff in gc_lijst:
        lengte += 1
        x_data.append(lengte)
    
    plt.bar(x_data, gc_lijst,tick_label = tick_lijst, align = 'center',color = 'turquoise')
    plt.axhline(y=gcprocent,color = 'r',linestyle = '-',linewidth = 2.0)
    plt.title('GC% per {} bp in {}'.format(bp,headers))
    plt.ylabel('GC%')
    plt.xlabel('Aantal nucleotide')
    plt.show()
    
main()
