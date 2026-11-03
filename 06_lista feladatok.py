#modul importálása random
import random

valasznak = random.randrange(1,100, 1)
print(valasznak)

#üres lista létrehozása
list = []

#10X hozzon létre egy véletlen számot és adja hozzá a listámhoz az elemet.
for i in range(10):
    list.append(random.randint(1,100))

print(list)

#az előző egy sorban megoldva.
lsit2 = [random.randrange(1,100) for i in range(10)]
print(lsit2)

for (index, ert) in enumerate(list):
    print(f"{index} => {ert}")

#lista elemeinek a sorba rendezése
sorbarendez = sorted(list)
print(sorbarendez)
#egy sorba kiíratás a lista elemeinek
print(sorted(list)) 

# fordított kiíratása a lista elemeinek
forditott = sorted(list, reverse=True)
print(forditott)

maximum = max(list)
print(maximum)

minimum = min(list)
print(minimum)

suma = sum(list)
print(suma)

#készítsünk egy új üres listát, majd töltsük fel 5db véletlen számmal ésszámoljuk
#ki az elemek átlagát.
list3 =[]

for i in range(7):
    list3.append(random.randint(1,30))

print(list3)
#átlag kiszámítása

#a lista elemeinek az összegét a sum() függvénnyel számoljuk ki.
lista3_osszeg = sum(list3)
print (f"Az elemek összege: {lista3_osszeg}")

#a lista elemeinek a számát a len() függvénnyel számoljuk ki.
lista3_db = len(list3)
print (f"Az elemek száma: {lista3_db}")

#az átlagot a lista elemeinek az összegét elosztjuk a lista elemeinek a számával.
atlag = lista3_osszeg / lista3_db
print (f"Az elemek átlaga: {atlag}")


#mindez egy sorban is megoldható.
print(lista3_osszeg / len(list3))

#két tizedes jegyre kerekítve
print(f"Az elemek átlaga: {atlag:.2f}")
print(f"Az elemek átlaga: {round(atlag, 2)}")
print(f"Az elemek átlaga: {round(sum(list3) / len(list3), 2)}")

#kiítarások:
szam = 1000000
print(f"A szám ezres tagolással: {szam:,}") #ez a formázás a számok ezres tagolását oldja meg.
print(f"Az elemek átlaga: {atlag:.2f}") #ez a formázás a számok tizedes jegyeinek a számát oldja meg.
print(f"Az elemek átlaga: {(sum(list3) / len(list3)):.2f}") #ez a formázás a számok ezres tagolását és tizedes jegyeinek a számát oldja meg.