# -*- encoding: utf-8 -*-
print ("Pozdravljeni v programu Jedilni List")
jedilni_list = {}
while True:
    ime_jedi = raw_input("Prosimo vnesite ime jedi: ")
    cena_jedi = raw_input("Prosimo vnesite ceno za jed: '%s': " % ime_jedi)
    jedilni_list[ime_jedi] = cena_jedi

    nova_jed = raw_input("Bi želeli vnesti novo jed? (da/ne): ")
    if nova_jed.lower() == "ne":
        break

with open("jedilni_list.txt", "w") as jedilna_datoteka:
    for jed in jedilni_list:
        jedilna_datoteka.write("%s, %s €\n" % (jed, jedilni_list[jed]))