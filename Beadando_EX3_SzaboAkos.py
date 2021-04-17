#45-ös feladat

def ellenorzo(adoszam):
    #ÁFA leíró számot szöveggé alakítő szótár
    afajelleg_dict = {"1": "Alanyi adómentes vagy adómentes tevékenységet végző (ÁFA körbe nem tartozó)",
                      "2": "Általános szabályok szerint adózó (Áfa körbe tartozó)",
                      "3": "Egyszerűsített vállalkozói adózás alá tartozó (EVA körbe tartozó)",
                      "4": "ÁFA körbe tartozó csoport adóalanyiságot választó",
                      "5": "ÁFA körbe csoport közös adószámának jelzése"}

    #területet leíró szám szóveggé alakító szótár
    terulet_dict = {"02": "Baranya", "22": "Baranya", "03": "Bács-Kiskun", "23": "Bács-Kiskun", "04": "Békés", "24": "Békés",
                    "05": "Borsod-Abaúj-Zemplén", "25": "Borsod-Abaúj-Zemplén", "06": "Csongrád", "26": "Csongrád", "07": "Fejér",
                    "27": "Fejér", "08": "Győr-Moson-Sopron", "28": "Győr-Moson-Sopron", "09": "Hajdú-Bihar", "29": "Hajdú-Bihar",
                    "10": "Heves", "30": "Heves", "11": "Komárom-Esztergom", "31": "Komárom-Esztergom", "12": "Nógrád", "32": "Nógrád",
                    "13": "Pest", "33": "Pest", "14": "Somogy", "34": "Somogy", "15": "Szabolcs-Szatmár-Bereg",
                    "35": "Szabolcs-Szatmár-Bereg", "16": "Jász-Nagykun-Szolnok", "36": "Jász-Nagykun-Szolnok", "17": "Tolna",
                    "37": "Tolna", "18": "Vas", "38": "Vas", "19": "Veszprém", "39": "Veszprém", "20": "Zala", "40": "Zala",
                    "41": "Észak-Budapest", "42": "Kelet-Budapest","43": "Dél-Budapest",
                    "44": "Kiemelt Adózók Adóigazgatósága", "45": "Kiemelt Ügyek Adóigazgatósága"}

    #aószám szétdarabolása 3 részre és ls listában tárolása
    ls = adoszam.split("-")
    if len(ls)!=3:
        return "Nem három számot adott meg, 2 darab kötőjel között"
    torzsszam = ls[0]
    afajelleg = ls[1]
    terulet = ls[2]

    #ha ismeretlen terület számot, túl kevés számjegyet vagy 5-nél nagyobb ÁFA szamot adott meg, hibát ad vissza
    if terulet_dict.get(terulet)==None or len(terulet)!=2 or len(torzsszam)!=8 or len(afajelleg)!=1 or int(afajelleg)>5:
        return "Rossz adószámot adott meg (túl kevés karakter, az ÁFAjelleget leíró szám 5-nél nagyobb vagy nem található ilyen területkód)"

    eredmeny=""

    #ÁFA jelleg és terület leírás lefordítása szavakra, eredményhez csatolása
    eredmeny=eredmeny+afajelleg_dict[afajelleg]+"; "+terulet_dict[terulet]

    #törzsszám tartományok alapján ezt is hozzácsatolja szavakkal az eredményhez
    if torzsszam[:2]=="10" and int(torzsszam[2:7])>0 and int(torzsszam[2:7])<30000:
        eredmeny+="; Vállalatok, szövetkezetek, pénzintézetek és egyéb szervezetek"
    elif torzsszam[:2]=="15" and int(torzsszam[2:7])>30000 and int(torzsszam[2:7])<70000:
        eredmeny+="; Önálló és bankszámlával rendelkező, részben önálló költségvetési szerver"
    elif torzsszam[:2]=="20" and int(torzsszam[2:7])>930000 and int(torzsszam[2:7])<1000000:
        eredmeny+="; Belföldi társaságok, megánszemélyek társaságai"
    else:
        ellenorzoszamnelkultorzsszam = torzsszam[:-1]
        inttorzsszam = int(ellenorzoszamnelkultorzsszam)

        if inttorzsszam > 1600000 and inttorzsszam < 1699999:
            eredmeny += "; Önálló bankszámlával nem rendelkező, részben önálló költségvetési szervek"
        elif inttorzsszam > 1900000 and inttorzsszam < 1999999:
            eredmeny += "; Költségvetési rend szerint gazdálkodó egyéb jogi személyek"
        elif inttorzsszam > 3000000 and inttorzsszam < 3010001:
            eredmeny += "; Költségvetési rend szerint gazdálkodó egyéb jogi személyek"
        elif inttorzsszam > 4000000 and inttorzsszam < 6000000:
            eredmeny += "; Egyéni vállalkozók (kisiparosok, magánkereskedők, szerződéses ipar és kereskedelmi szolgáltatók)"
        elif inttorzsszam > 7000000 and inttorzsszam < 7500000:
            eredmeny += "; Áltlános forgalmi adó fizetésére kötelezett magánszemélyek"
        else:
            print("Sajnos előfordulhat hogy nem megfelelő adószámot adott meg, mert ez a trözsszám egyik ismert tartományba "
                  "se tartozik. De amit biztosan tudok, hogy: ")

    #végül az eredmény string visszaadása
    return eredmeny


#MAIN
adoszam=input("Adjon meg egy adószámot (xxxxxxxx-y-zz alakban): ")
print(ellenorzo(adoszam))

#Ezekre ajánlom a tesztelést:
#10345678-4-11      nincs egyik tartományban sem ami a weboldalon szerepel, de a többi rész jó
#17000000-4-29      nincs egyik tartományban sem ami a weboldalon szerepel, de a többi rész jó
#10245678-4-11      jó tartományban van, minden jó itt
#43268753-2-36      jó tartományban van, minden jó itt
#10345678-6-11      túl nagy az áfajelleg
#10345678-4-47      ilyen területkód nincs
#1034567-4-11       nincs elég számjegy