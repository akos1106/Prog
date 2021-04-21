#6-os feladat

import sys
import numpy as np
import matplotlib.pyplot as plt

try:
    #egy listát aminek az elemei nem int-ek, int-ekké alakít
    def intte(lista):
        ls=[]
        for i in lista:
            ls.append(int(i))
        return ls

    a = input("Adjon meg egy évszámot és egy számot (pl '2010 9'): ")
    ls = a.split(" ")

    #ha betűt is tartalmaz a szöveg amit megadott
    if ls[0].isdigit()==False or ls[1].isdigit()==False:
        print("Csak számokat tartalmazhat a szöveg amit megad")
    else:
        ev = ls[0]
        n = int(ls[1])
        #ls listában van a string ev, és int n változó

        #ha arra az évszámra kíváncsi ami nincs az adatbázisba,
        # vagy túl sok/kevés megyét akar összehasonlítani, hibaüzenetet kap a felhasználó
        if int(ev)<2005 or int(ev)>2014:
            print("Sajnos csak 2005 és 2014 közötti adatokkal tudok szolgálni")
        elif n > 12 or n < 2:
            print("Sajnos csak minimum 2, és maximum 12 darab megyét tudok összehasonlítani grafikonon")
        else:

            #megnyitja a fájlt, megnézi hányszor hanyas mátrix kell,
            # amibe belefér az összes sor és oszlop abból az évből
            fajlin=open(sys.argv[1], "r")
            elsosor=fajlin.readline()              #beolvassa az első sort a fájlból, ez utáni sorral folytatódik majd a beolvasás
            listaelsosorbol=elsosor.split(",")
            oszlopokszama=len(listaelsosorbol)       #megvan az oszlopok száma
            sorokszama=0
            for sor in fajlin:
                # sor = sor.strip()
                listaegysorbol = sor.split(",")
                datum = listaegysorbol[0].split("/")    #datum listában a sor lista elő elemét szeleteli bele a "\" mentén
                if datum[2] == ev:                      #ha a dátum lista 3. eleme (az év) egyezik a kért évvel, sorok száma megnő
                    sorokszama+=1
            sorokszama+=1                               #megvan a sorok száma, de plusz egy mert majd a headert is el akarom tárolni


            #fájl elejére megy, és most fog következni a kellő adatok átpakolása a megfelelő méretű mat-ba
            fajlin.seek(0)

            mat=np.empty((sorokszama,oszlopokszama),dtype=object)   #megfelelő méretű mátrix letrehozva
            k=0
            elso=fajlin.readline()          #az első sort máshogy kell kezelni mint a többi sort, ezért külön teszem a mat-ba
            elso=elso.strip()
            elsolst=elso.split(",")
            for i in range(len(elsolst)):
                mat[k,i]=elsolst[i]
            k=1                             #a k változóval követem, a mat melyik sorába is kell tenni az adatokat
            #header-t beletette a mat első sorába

            for sor in fajlin:
                sor = sor.strip()
                lista = sor.split(",")
                datum = lista[0].split("/")
                if datum[2] == ev:                  #megfelelő évű sorokat teszi bele a mat k-adik sorába
                    for i in range(len(lista)):
                        mat[k,i]=lista[i]
                    k+=1                            #nő a k, nő hogy hanyadik sorba kell pakolni
            #a mat mátrix első sorában benne van a header, a többi sorában
            #   a megfelelő évhez tartozó adatok, és első oszlopban a dátumok

            atlagok=[]
            for j in range(oszlopokszama):
                sum=0
                for i in range(sorokszama):
                    if j>0 and i>0:                 #hogy a headert és első oszlopot ne akarja az átlagba számítani
                        sum+=int(mat[i,j])
                atlag=sum/(sorokszama-1)            #egy oszlopbal lévő számok átlaga
                if j>0:
                    atlagok.append((mat[0,j],atlag))
            #atlagok listában benne vannak a megyék nevei és hozzájuk az átlagok a megfelelő évben tuple-ökben

            atlagok.sort(key=lambda x: x[1], reverse=True)
            #az atlagok elemei 2 elemű tuple-ök, és ezen tuple-ök másdoik elemét figyelembe véve teszi sorba a átlagok elemeit, csökkenve
            atlagok=atlagok[:n]
            #atlagok listában benne van az első n db legnagyobb átlagú megye

            dict={}
            for i in range(n):
                dict["lista"+str(i)]=[]
            #szótár, amelyben a key-ek: "lista0","lista1"..."listaN"; a value-k üres listák ([])

            for i in range(n):
                for oszlop in range(oszlopokszama):
                    for sor in range(sorokszama):
                        if oszlop>0 and sor>0:
                            if mat[0,oszlop]==atlagok[i][0]:
                                dict['lista'+str(i)].append(mat[sor,oszlop])
            #n darab lista létrehozva, bennük a fertőzések száma hetente, az első listában (dict['lista0']) a
            # legmagasabb átlaggal rendelkező megye, és így csökkennek az átlagok ahogy a lista száma nő

            xteng=[]
            for i in range(len(dict['lista0'])):
                xteng.append(i)
            #x tengelyhez használandó lista (0,1,2...hetekSzama)

            # nem túl szép megoldás, de ezt máshogy nem tudtam összehozni, hogy n darab plt.plot legyen, és el lehessen őket nevezni
            s = 0
            if s < n:
                line1, = plt.plot(xteng, intte(dict["lista0"]), 'r')
                s += 1
                if s < n:
                    line2, = plt.plot(xteng, intte(dict["lista1"]), 'g')
                    s += 1
                    if s < n:
                        line3, = plt.plot(xteng, intte(dict["lista2"]), 'b')
                        s += 1
                        if s < n:
                            line4, = plt.plot(xteng, intte(dict["lista3"]), 'y')
                            s += 1
                            if s < n:
                                line5, = plt.plot(xteng, intte(dict["lista4"]), 'c')
                                s += 1
                                if s < n:
                                    line6, = plt.plot(xteng, intte(dict["lista5"]), 'm')
                                    s += 1
                                    if s < n:
                                        line7, = plt.plot(xteng, intte(dict["lista6"]), 'k')
                                        s += 1
                                        if s < n:
                                            line8, = plt.plot(xteng, intte(dict["lista7"]), 'r--')
                                            s += 1
                                            if s < n:
                                                line9, = plt.plot(xteng, intte(dict["lista8"]), 'g--')
                                                s += 1
                                                if s < n:
                                                    line10, = plt.plot(xteng, intte(dict["lista9"]), 'b--')
                                                    s += 1
                                                    if s < n:
                                                        line11, = plt.plot(xteng, intte(dict["lista10"]), 'y--')
                                                        s += 1
                                                        if s < n:
                                                            line12, = plt.plot(xteng, intte(dict["lista11"]), 'm--')
            #vonalak elnevezése
            if n == 1: plt.legend((line1), (atlagok[0][0]))
            if n == 2: plt.legend((line1, line2), (atlagok[0][0], atlagok[1][0]))
            if n == 3: plt.legend((line1, line2, line3), (atlagok[0][0], atlagok[1][0], atlagok[2][0]))
            if n == 4: plt.legend((line1, line2, line3, line4), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0]))
            if n == 5: plt.legend((line1, line2, line3, line4, line5), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0]))
            if n == 6: plt.legend((line1, line2, line3, line4, line5, line6), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0]))
            if n == 7: plt.legend((line1, line2, line3, line4, line5, line6, line7), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0]))
            if n == 8: plt.legend((line1, line2, line3, line4, line5, line6, line7, line8), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0]))
            if n == 9: plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0]))
            if n == 10:plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9, line10), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0], atlagok[9][0]))
            if n == 11:plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0], atlagok[9][0], atlagok[10][0]))
            if n == 12:plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12), (atlagok[0][0], atlagok[1][0], atlagok[2][0], atlagok[3][0], atlagok[4][0], atlagok[5][0], atlagok[6][0], atlagok[7][0], atlagok[8][0], atlagok[9][0], atlagok[10][0], atlagok[11][0]))

            #grafikon feliratok hozzáadása, jól írja a -ban/-ben -t az év után
            if ev[3]=='1' or ev[3]=='2' or ev[3]=="4" or ev[3]=='5' or ev[3]=='7' or ev[3]=='9' or ev[2:4]=='10':
                plt.xlabel(f"Hetek száma {ev}-ben")
                plt.ylabel("Fertőzések száma/hét")
                plt.title(f"Bárányhimlő fertőzések {ev}-ben abban a(z) {n} darab megyénkben, ahol éves szinten a legmagasabb volt a fertőzöttségi átlag")
                plt.show()
            else:
                plt.xlabel(f"Hetek száma {ev}-ban")
                plt.ylabel("Fertőzések száma/hét")
                plt.title(f"Bárányhimlő fertőzések {ev}-ban abban a(z) {n} darab megyénkben, ahol éves szinten a legmagasabb volt a fertőzöttségi átlag")
                plt.show()

            fajlin.close()

#ha nem jó fájlnevet adott meg a parancssori argumentumban
except FileNotFoundError:
    print("Nem megfelelő elérési utat adott meg a beolvasandó fájlhoz")