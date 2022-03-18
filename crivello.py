#Non ho idea del perché funzioni, esattamente come funzioni, ma funziona.
from math import *
from datetime import datetime
from heapq import heappush, heapreplace
import time

def save(data):
    f1 = open('pt.txt', 'w')
    f1.write(data)
    f1.close()
    
def genera_primi(toDo=0):
    
    fP = []
    n = 3
    i = 1
    w = 0
    todel = [ (4, 2) ]
    while w < toDo:
        if todel[0][0] is not n: 
            fP.append(n)
            w = n
            heappush(todel, (n*n, n))        
        else:     
            while todel[0][0] is n:             
                p = todel[0][1] 
                heapreplace(todel, (n+p, p))
        n += 1
        
    return fP

while True:

    j = int(input('Inserire numero massimo: \n'))
    print('Calculating...')
    notPrime = 0
    i=0
    n_app = []
    #c = datetime.now()
    #t= (c.day * 24 * 60 * 60 + c.second) * 1000 + c.microsecond / 1000.0
    t = int(time.time())
    n_primi = genera_primi(ceil(sqrt(j))) #Calcolare quanto grande può essere M.C.D. di J, numero molto grande, dispari, pertanto non avrà il 2 nella fattorizzazione

    while i < ceil(j/2):

        notPrime =0 
        f = i*2+1

        for e in n_primi:
            if f % e is 0 and f!=e:
                notPrime = 1
                break
        if notPrime is 0:
            n_app.append(f)
        
        i+=1     
    #c = datetime.now()    
    #t1 = (c.day * 24 * 60 * 60 + c.second) * 1000 + c.microsecond / 1000.0 - t
    #t1 = t1/1000
    t1 = int(time.time())-t
    print('Ultimo numero primo:',n_app[-1])
    print(f'Tempo: {t1} secondi')
    
    if int(t1) is 0: t1 = 1
    t1 = int(t1)
    f1 = int(j/t1)
    print(f'Frequenza: {f1}/secondo')
    save(str(n_app))
    print('Lista numeri primi salvata in: pt.txt')
    
