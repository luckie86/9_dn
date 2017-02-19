# -*- encoding: utf-8 -*-
lasje = {"CCAGCAATCGC": "Črni", "GCCAGTGCCG": "Rjavi", "TTAGCTATCGC": "Plavolasi"}
obraz = {"GCCACGG": "Kvadratast", "ACCACAA": "Okrogel", "AGGCCTCA": "Ovalen"}
oci = {"TTGTGGTGGC": "Modre", "GGGAGGTGGC": "Zelene", "AAGTAGTGAC": "Rjave"}
spol = {"TGAAGGACCTTC": "Ženska", "TGCAGGAACTTC": "Moški"}
rasa = {"AAAACCTCA": "Bela", "CGACTACAG": "Črna", "CGCGGGCCG": "Rumena"}

mozni_storilci = {"Eva":{"Spol":"Ženski", "Rasa":"Bela", "Lasje":"Plavolasi", "Oči": "Modre", "Obraz": "Ovalen"},
                   "Larisa":{"Spol":"Ženski", "Rasa":"Bela", "Lasje":"Rjavi", "Oči": "Rjave", "Obraz": "Ovalen"},
                   "Matej":{"Spol":"Moški", "Rasa":"Bela", "Lasje":"Črni", "Oči": "Modre", "Obraz": "Ovalen"},
                   "Miha":{"Spol":"Moški", "Rasa":"Bela", "Lasje":"Rjavi", "Oči": "Zelene", "Obraz": "Kvadratast"}}

with open("dna.txt", "r") as file:
    dna = file.read()

lasje_ujemanje = ""
for kljuc, vrednost in lasje.items():
    if kljuc in dna:
        lasje_ujemanje = vrednost
        break

obraz_ujemanje = ""
for kljuc, vrednost in obraz.items():
    if kljuc in dna:
        obraz_ujemanje = vrednost
        break

oci_ujemanje = ""
for kljuc, vrednost in oci.items():
    if kljuc in dna:
        oci_ujemanje = vrednost
        break

spol_ujemanje = ""
for kljuc, vrednost in spol.items():
    if kljuc in dna:
        spol_ujemanje = vrednost
        break

rasa_ujemanje = ""
for kljuc, vrednost in rasa.items():
    if kljuc in dna:
        rasa_ujemanje = vrednost
        break

ujemanje = {"Spol": spol_ujemanje, "Rasa": rasa_ujemanje, "Lasje": lasje_ujemanje, "Oči": oci_ujemanje, "Obraz": obraz_ujemanje}

storilec = None
for ime, vrednost in mozni_storilci.items():
    if vrednost == ujemanje:
        storilec = ime
        break

print ("Sladoled je pojedel: " + storilec)