print("=== Tanulói adatlap ===")
nev = input("Add meg a tanuló nevét: ")
eletkor = int(input("Add meg a tanuló életkorát: "))
osztaly = input("Add meg a tanuló osztályát: ")
kedvenc_tantargy = input("Add meg a tanuló kedvenc tantárgyát: ")
heti_oraszam = int(input("Add meg a tanuló heti óraszám: "))

print("\n---Tanulói adatok---")
print(f"név: {nev}")
print(f"Életkor: {eletkor}")
print(f"osztály: {osztaly}")
print(f"kedvenc tantárgy: {kedvenc_tantargy}")
print(f"heti óraszám: {heti_oraszam}")

#kormeghatározás:
if  eletkor < 14:
    print("korcsoport: 14 év alatti")
elif eletkor <= 18:
    print("korcsoport: 14 és 18 év között")
else:
    print("18 év feletti")

#heti óra értékelése
if  heti_oraszam < 20:
    print("kevés")
elif heti_oraszam <= 35:
    print("átlagos")
else:
    print("magas")


#2. feladat
print("\n=== Osztálynyilvántartás===")
nevek = []
heti_orak = []
tanulok_szama = int(input("Add meg hány tanulót kérjek be: "))

for i in range(tanulok_szama):
    print(f"\n{i+1}. tanuló adata")
    nev2 = input("Név: ")
    heti_ora = int(input("Heti ótaszáma: "))

    nevek.append(nev2)
    heti_orak.append(heti_ora)

print("\n===Osztály összesítő===")
print(f"tanulók száma: {len(nevek)}")

print("osztály tanulói:")
for nev in nevek:
    print(nev)

max_oraszam = max(heti_orak)
max_index = heti_orak.index(max_oraszam)

print(f"a legtöbb heti óraszáma: {nevek[max_index]} óraszáma: {max_oraszam} ")

atlag = sum(heti_orak)/len(heti_orak)
print(f"átlagos óraszám: {atlag:.2f} óra")

#3. feladat:
import random
pontok = []
for i in range(len(nevek)):
    pontok.append(random.randint(1,100))

print("====tanulói eredmények====")
#tanulók neve és pontszáma:
for i in range(len(nevek)):
    print(f"{nevek[i]}: {pontok[i]} pont")

#leggyengébb:
min_pont = min(pontok)
min_index = pontok.index(min_pont)

print(f"leggyengébb tanuló: {nevek[min_index]} elért pont: {min_pont}")

#min pontok elérése:
sikeres = 0
sikertelen = 0

for pont in pontok:
    if pont >= 60:
        sikeres += 1
    else:
        sikertelen += 1
print(f"Sikeres tanulók száma: {sikeres}")
print(f"Sikertelen tanulók száma: {sikertelen}")

#4.feladat:
def kereses(keresett_nev ,nevek, heti_orak, pontok):

    if keresett_nev in nevek:

        index = nevek.index(keresett_nev)
        print("===találat===")
        print(f"Név: {nevek[index]}")
        print(f"heti óraszám: {heti_orak[index]}")
        print(f"pont: {pontok[index]}")
    else:
        print("Nincs találat!")

keresett_nev = input("Add meg a kereses nev: ")

kereses(keresett_nev, nevek, heti_orak, pontok)