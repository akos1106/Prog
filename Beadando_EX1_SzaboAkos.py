#6-os feladat

import sys
import numpy as np
import matplotlib.pyplot as plt

try:
    def intte(lista):
        ls=[]
        for i in lista:
            ls.append(int(i))
        return ls

    a = input("Adjon meg egy évszámot és egy számot (xxxx y): ")
    ls = a.split(" ")
    ev = ls[0]
    n = int(ls[1])

    fajlinteszt=open(sys.argv[1], "r")
    elso=fajlinteszt.readline()
    listaa=elso.split(",")
    oszlopokszama=len(listaa)
    sorokszama=0
    for sor in fajlinteszt:
        sor = sor.strip()
        listaaa = sor.split(",")
        datum = listaaa[0].split("/")
        if datum[2] == ev:
            sorokszama+=1
    sorokszama+=1           #header miatt
    fajlinteszt.close()
    #megvan hogy hányszor hanyas lesz az a mátrix amiben csak a megadott évi adatok vannak és az összes oszlop

    fajlin = open(sys.argv[1], "r")

    mat=np.empty((sorokszama,oszlopokszama),dtype=object)
    k=0
    elso=fajlin.readline()
    elso=elso.strip()
    elsolst=elso.split(",")
    for i in range(len(elsolst)):
        mat[k,i]=elsolst[i]
    k=1
    #header-t beletette a mat első sorába

    for sor in fajlin:
        sor = sor.strip()
        lista = sor.split(",")
        datum = lista[0].split("/")
        if datum[2] == ev:
            for i in range(len(lista)):
                mat[k,i]=lista[i]
            k+=1
    #a mat mátrix első sorában benne van a header, a többi sorában
    #   a megfelelő évhez tartozó adatok, és első oszlopban a dátumok

    atlagok=[]
    for j in range(oszlopokszama):
        sum=0
        for i in range(sorokszama):
            if j>0 and i>0:
                sum+=int(mat[i,j])
        atlag=sum/(sorokszama-1)
        if j>0:
            atlagok.append((mat[0,j],atlag))
    #atlagok tuple-ben benne vannak a megyék nevei és hozzájuk az átlagok a megfelelő évben

    atlagok.sort(key=lambda x: x[1], reverse=True)
    atlagok=atlagok[:n]
    #atlagok tuple-ben benne van az első n db legnagyobb átlagú megye

    dict={}
    for i in range(n):
        dict["lista"+str(i)]=[]
    #szótár amelyben a keyek: "lista0","lista1","lista2"..."listan"; a value-k üres listák ([])

    for i in range(n):
        for oszlop in range(oszlopokszama):
            for sor in range(sorokszama):
                if oszlop>0 and sor>0:
                    if mat[0,oszlop]==atlagok[i][0]:
                        dict['lista'+str(i)].append(mat[sor,oszlop])
    #n darab lista létrehozva, bennük a fertőzések száma hetente, az első listában (dict['lista0']) a
    # legmagasabb átlaggal rendelkező megye, és így csökkennek az átlagok ahogy a lista száma nő

    teng=[]
    for i in range(len(dict['lista0'])):
        teng.append(i)
    #x tengelyhez használandó lista (0,1,2...hetekszama)

    #nem túl szép megoldás, de ezt máshogy nem tudtam összehozni, hogy n darab plt.plot legyen, és el lehessen őket nevezni
    if n==1:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        plt.legend((line1), (atlagok[0][0]))
    if n==2:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        plt.legend((line1,line2), (atlagok[0][0],atlagok[1][0]))
    if n==3:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        plt.legend((line1, line2, line3), (atlagok[0][0], atlagok[1][0], atlagok[2][0]))
    if n==4:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        plt.legend((line1, line2, line3, line4), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0]))
    if n==5:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        plt.legend((line1, line2, line3, line4, line5), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0]))
    if n==6:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        line6, = plt.plot(teng, intte(dict["lista5"]), 'm')
        plt.legend((line1, line2, line3, line4, line5, line6), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0]))
    if n==7:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        line6, = plt.plot(teng, intte(dict["lista5"]), 'm')
        line7, = plt.plot(teng, intte(dict["lista6"]), 'k')
        plt.legend((line1, line2, line3, line4, line5, line6, line7), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0]))
    if n==8:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        line6, = plt.plot(teng, intte(dict["lista5"]), 'm')
        line7, = plt.plot(teng, intte(dict["lista6"]), 'k')
        line8, = plt.plot(teng, intte(dict["lista7"]), 'r--')
        plt.legend((line1, line2, line3, line4, line5, line6, line7, line8), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0]))
    if n==9:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        line6, = plt.plot(teng, intte(dict["lista5"]), 'm')
        line7, = plt.plot(teng, intte(dict["lista6"]), 'k')
        line8, = plt.plot(teng, intte(dict["lista7"]), 'r--')
        line9, = plt.plot(teng, intte(dict["lista8"]), 'g--')
        plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0]))
    if n==10:
        line1, = plt.plot(teng, intte(dict["lista0"]), 'r')
        line2, = plt.plot(teng, intte(dict["lista1"]), 'g')
        line3, = plt.plot(teng, intte(dict["lista2"]), 'b')
        line4, = plt.plot(teng, intte(dict["lista3"]), 'y')
        line5, = plt.plot(teng, intte(dict["lista4"]), 'c')
        line6, = plt.plot(teng, intte(dict["lista5"]), 'm')
        line7, = plt.plot(teng, intte(dict["lista6"]), 'k')
        line8, = plt.plot(teng, intte(dict["lista7"]), 'r--')
        line9, = plt.plot(teng, intte(dict["lista8"]), 'g--')
        line10, = plt.plot(teng, intte(dict["lista9"]), 'b--')
        plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9, line10), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0], atlagok[9][0]))

    #grafikon feliratok hozzáadása, jól írja a -ban/-ben -t az év után
    ev=int(ev)
    if ev==2005 or ev==2007 or ev==2009 or ev==2010 or ev==2011 or ev==2012 or ev==2014 or ev==2015:
        plt.xlabel(f"Hetek száma {ev}-ben")
        plt.ylabel("Fertőzések száma/hét")
        plt.title(f"Bárányhimlő fertőzések {ev}-ben abban a(z) {n} darab megyénkben, ahol éves szinten a legmagasabb volt a fertőzöttségi átlag")
        plt.show()
    else:
        plt.xlabel(f"Hetek száma {ev}-ban")
        plt.ylabel("Fertőzések száma/hét")
        plt.title(f"Bárányhimlő fertőzések {ev}-ban abban a(z) {n} darab megyénkben, ahol éves szinten a legmagasabb volt a fertőzöttségi átlag")
        plt.show()

except FileNotFoundError:
    print("Nem megfelelő elérési utat adott meg a beolvasandó fájlhoz")