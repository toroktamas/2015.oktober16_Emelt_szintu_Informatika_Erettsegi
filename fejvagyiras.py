#!usr/bin/python3
# -*- coding:utf-8 -*-
import random
"""2015.oktober.16--odikai Emelt szintu Informatika erettsegi megoldas python programozasi nyelven"""
print("1. feladat ")
"""Penzfeldobast kell szimulalni random."""
print("A pezfedobas eredmenye: {}".format(random.choice("IF")))
print("2. feladat ")
"""Felhasznalotol bekerek egy tippet es le szimulalom hogy eltalalta-e a kerdeses ermet."""
tip=str(input("Tippeljen! (F/I)= "))
feldob = random.choice("IF")
if tip == feldob:
    print("On eltalalta")
else:
    print("On nem talalta el!")
print("3. feladat ")
"""Meg kell allapitani hogy hany feldobes vagyis hany sor van a kiserlet.txt--ben ugy hogy nem tarolhatjuk el az osszes adatot a memoriaban."""
n = 0
with open("kiserlet.txt", "rt",encoding="utf-8") as f:
   for a in f:
        n+=1            
print("A kiserlet {} dobasbol all.".format(n))

print("4. feladat ")
"""Meg kell hatarozni hogy milyen gyakorisaggla dobtak fejet."""
relativ = 0
with open("kiserlet.txt", "rt",encoding="utf-8") as g:
    for h in g:
        if h=="F\n":
            relativ+=1
print("A kiserlet soran afej relative gyakorisaga {}% volt.".format(round(((relativ/n)*100),2)))

print("5. feladat ")
"""Meg kell hatarozni hogy hanyszor fordult elo hogy egymas uton ketszer fejet dobtak."""
"""
3 esetet kell vizsgalni:
1. %IFFI%
2. FFI%
3. %IFF

Peldaul:
FFIIIIFFIIFFIIIIFF"""

dupla_F_szama = 0
utolso_4 = []  # az utolso negy elemet tartalmazza
with open("kiserlet.txt", "rt",encoding="utf-8") as g:
    for k, s in enumerate(g):
        utolso_4.append(s.replace('\n',''))
        if len(utolso_4) > 4:
            del utolso_4[0]  # letoroljuk az elso elemet

        if k == 3 and utolso_4 == ['F','F','I']:  # 2.-es eset vizsgalata
            dupla_F_szama += 1
        if utolso_4 == ['I','F','F','I']:  # 1.-as eset vizsgalata
            dupla_F_szama += 1

if utolso_4[1:] == ['I','F','F']:  # 3.-as eset vizsgalata
    dupla_F_szama += 1

print("A kiserlet soran {} alkalommal dobtak pontosan ket fejet egymas utan.".format(dupla_F_szama))

print("6. feladat ")
"""Meg kell alapitani hogy melyik fej sorozat volt a leghosszabb a fajlban."""
leghosszabb_kezdodik = 0
leghosszabb_hossza = 0
jelenlegi_kezdodik = 0
jelenlegi_hossza = 0
elozo_sor = ''
with open("kiserlet.txt", "rt",encoding="utf-8") as g:
    for k, s in enumerate(g):
        sor = s.replace("\n", "")
        if sor == "F":
            jelenlegi_hossza += 1
            if elozo_sor != 'F':
                jelenlegi_kezdodik = k+1
        else:
            if jelenlegi_hossza > leghosszabb_hossza:
                leghosszabb_hossza = jelenlegi_hossza
                leghosszabb_kezdodik = jelenlegi_kezdodik
            jelenlegi_hossza = 0
            jelenlegi_kezdodik = 0
        elozo_sor = sor

if jelenlegi_hossza > leghosszabb_hossza:
    leghosszabb_hossza = jelenlegi_hossza
    leghosszabb_kezdodik = jelenlegi_kezdodik

print("A leghosszabb tisztafej sorozat {0} tagbol all, kezdete a(z) {1}. dobas".format(leghosszabb_hossza, leghosszabb_kezdodik))


print("7. feladat ")
""" """

dobasok = []
for n in range(1, 1001):
    sorozat = []
    for i in range(1,5):
        sorozat.append(random.choice("IF"))
    dobasok.append(sorozat)

ffff_szama = dobasok.count(['F','F','F','F'])
fffi_szama = dobasok.count(['F','F','F','I'])

with open("dobasok.txt", "wt", encoding='utf-8') as f:
    f.write("FFFF: {0}, FFFI: {1}\n".format(ffff_szama, fffi_szama))
    f.write(' '.join([''.join(sorozat) for sorozat in dobasok]))
