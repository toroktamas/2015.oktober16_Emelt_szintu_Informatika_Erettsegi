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
elozo=""
n = 0
with open("kiserlet.txt", "rt",encoding="utf-8") as g:
    for s in g:
        sor = s.replace("\n","")
        if sor == elozo and sor == "F" and elozo=="F":
            n+=1
        elozo=sor
print("A kiserlet soran {} alkalommal dobtak pontosan ket fejet egymas utan.".format(n))

print("6. feladat ")
"""Meg kell alapitani hogy melyik fej sorozat volt a leghosszabb a fajlban."""
legnagyon = {}
leghosszab = {}
n = 0
with open("kiserlet.txt", "rt",encoding="utf-8") as g:
    for k, s in enumerate(g):
        sor = s.replace("\n", "")
        if sor =="F" and elozo == sor and elozo == "F":
            pass





print("7. feladat ")
""" """
