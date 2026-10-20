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

sorbarendez = sorted(list)
print(sorbarendez)

maximum = max(list)
print(maximum)

minimum = min(list)
print(minimum)

suma = sum(list)
print(suma)

resto = sum(list)
print(resto)