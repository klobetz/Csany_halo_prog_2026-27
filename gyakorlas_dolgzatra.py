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

"""