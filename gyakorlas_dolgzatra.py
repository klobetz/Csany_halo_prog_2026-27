#1.lépés
"""
for szoveg in ["12", "abc","", "-5", "3.5", "0"]:
    print(repr(szoveg), "=>", szoveg.isdigit())

#egyszeri bekérés
vlan = input("Add meg a VLAN atonosítót (1-4094): ")
if not vlan.isdigit():
    print("Hibás adat, számot kell megadni")
else:
    print(f"ok, a megadott VLAN: {vlan}")

#ismételten amíg nem jó a megadott érték:
while True:
    vlan = input("Add meg a VLAN atonosítót (1-4094): ")
    if not vlan.isdigit():
        print("Hibás adat, számot kell megadni")
    else:
        print(f"ok, a megadott VLAN: {vlan}")
        break

#most a többi szűrés is:
while True:
    vlan = input("Add meg a VLAN atonosítót (1-4094): ")
    if not vlan.isdigit():
        print("Hibás adat, számot kell megadni")
    elif not 1 <= int(vlan) <= 4094:
        print("Hibás adat, 1-4094-ig kell megadni a VLAN azonosítót!")
    else:
        print(f"ok, a megadott VLAN: {vlan}")
        break


#mindez függvényekkel:
def vlan_bekeres():
    while True:
        vlan = input("Add meg a VLAN atonosítót (1-4094): ")
        if not vlan.isdigit():
            print("Hibás adat, számot kell megadni")
        elif not 1 <= int(vlan) <= 4094:
            print("Hibás adat, 1-4094-ig kell megadni a VLAN azonosítót!")
        else:
            return int(vlan)

def vlan_tipusa(vlan):
    if vlan == 1:
        return "alapértelmezett VLAN"
    elif vlan <= 1001:
        return "normal VLAN"
    elif vlan <= 1005:
        return "fentartott VLAN"
    return "kiterjesztett tartományú VLAN"

def feladat():
    vlan_ID = vlan_bekeres()
    print(f"\nVLAN azonosító: {vlan_ID}")
    print(f"Típusa: {vlan_tipusa(vlan_ID)}")

#meghívom a függvényt:
feladat()


#időbélyeg ellenőrzés:
ido_teszt = input("Add meg az időbélyeget (ÓÓ:PP:MM): ")
reszek = ido_teszt.split(":")
print(reszek)
print(type(reszek))


ido = input("Add meg az időbélyeget (ÓÓ:PP:MM): ")
reszek = ido.split(":")
if len(reszek) != 3:
    print("hibás, lista hossz")
for resz in reszek:
    if not resz.isdigit():
        print ("nem szám")
        break
    ora = int(reszek[0])
    perc = int(reszek[1])
    masodperc = int(reszek[2])
    if ora > 23 or perc > 59 or masodperc > 59:
        print("Hibás időbélyeg érték")
        break
    print(f"A megadott időbélyeg: {ora}:{perc}:{masodperc}")
    break


valasz = input("Add meg a jelszót: ")

van_benne_szam = False
van_bebbe_nagy = False


for karakter in valasz:
    if karakter.isdigit():
        van_benne_szam = True
    if karakter.isupper():
        van_bebbe_nagy = True


if van_benne_szam:
    print("van benne szám!")
if van_bebbe_nagy:
    print("van benne nagybetű!")

"""
def ip_ervenyes(ip):
    reszek = ip.split(".")
    if len(reszek) != 4:
        return False
    for resz in reszek:
        if not resz.isdigit():
            return False
        if int(resz) < 0 or int(resz) > 255:
            return False
    return True


def uj_eszkoz2():
    ip = input("Kéeke egy ip címet: ")
    if not ip_ervenyes(ip):
        print("nem érvényes IP- cím:")


while True:
    eszkozok_lista = []
    print("1 - Új eszköz\n0 - Kilépés")
    valasztas = input("add meg a menüt: ")
    if valasztas == '1':
        uj_eszkoz2(eszkozok_lista)



















