"""
import random

#1.feladat:
print("=== Belépés a hálózatfelügyeleti rendszerbe ===")
felhasznalonev = "admin"
jelszo = "Halo2026"
probalkozas = 0
while probalkozas < 3:
    fn = input("Felhasználónév: ")
    jsz = input("Jelszó: ")
    if fn != "" and fn == felhasznalonev and jsz == jelszo:
        print("Belépés engedélyezve. Üdvözlünk, admin!")
        break
    probalkozas += 1

    if probalkozas < 3:
        print(f"Hibás adatok! Hátralévő próbálkozások: {3 - probalkozas}")
    else:
        print("Háromszor hibás adat. A fiók zárolva.")

# 2. feladat:
print("=== Port ellenőrző ===")
while True:
    szam = input("Add meg a portszámot (1-65535): ")
    if not szam.isdigit():
        print("Hibás adat! Számot kell megadni.")
    elif not 1 <= int(szam) <= 65535:
        print("Hibás adat! A portszám 1 és 65535 között lehet.")
    else:
        print(f"\nPortszám: {szam}")
        break

port = int(szam)

if port <= 1023:
    print("Típusa: jól ismert port")
elif port <= 49151:
    print("Típusa: regisztrált port")
else:
    print("Típusa: dinamikus port")

if port == 22:
    print("Szolgáltatás: SSH")
elif port == 53:
    print("Szolgáltatás: DNS")
elif port == 80:
    print("Szolgáltatás: HTTP")
elif port == 443:
    print("Szolgáltatás: HTTPS")
elif port == 3389:
    print("Szolgáltatás: RDP")
else:
    print("ismeretlen szolgáltatás")


#3. Feladat
print("=== Forgalomfigyelés ===")
meresek = [random.randint(1, 100) for i in range(10)]
for sorszam, ertek in enumerate(meresek, 1):
    print(f"{sorszam}. mérés: {ertek} Mbit/s")

print(f"\nLegnagyobb forgalom: {max(meresek)} Mbit/s ({meresek.index(max(meresek)) + 1}. mérés)")
print(f"Legkisebb forgalom: {min(meresek)} Mbit/s")
print(f"Átlagos forgalom: {sum(meresek) / len(meresek):.2f} Mbit/s")
print("Csökkenő sorrendben:", *sorted(meresek, reverse=True))
db = sum(1 for m in meresek if m >= 80)
print(f"Túlterhelt mérések (80 Mbit/s vagy több): {db} db")
"""

#4.feladat:
def ip_ervenyes(ip):
    reszek = ip.split(".")
    if len(reszek) != 4:
        return False
    for resz in reszek:
        if not resz.isdigit():
            return False
        if int(resz) > 255:
            return False
    return True


def uj_eszkoz(eszkozok):
    ip = input("Add meg az IP-címet: ")
    if not ip_ervenyes(ip):
        print("Érvénytelen IP-cím!")
    elif ip in eszkozok:
        print("Ez az IP-cím már szerepel a listában.")
    else:
        eszkozok.append(ip)
        print("Az eszköz rögzítve.")


def listaz(eszkozok):
    if len(eszkozok) == 0:
        print("Nincs rögzített eszköz.")
    for sorszam, ip in enumerate(eszkozok, 1):
        print(f"{sorszam}. {ip}")


def torol(eszkozok):
    ip = input("Melyik IP-című eszközt töröljem? ")
    if ip in eszkozok:
        eszkozok.remove(ip)
        print("Az eszköz törölve.")
    else:
        print("Nincs ilyen eszköz.")


def eszkoz_nyilvantartas():
    eszkozok = []
    while True:
        print("\n=== Eszköznyilvántartás ===")
        print("1 - Új eszköz\n2 - Eszközök listázása\n3 - Eszköz törlése\n0 - Kilépés")
        valasztas = input("Választás: ")
        if valasztas == "1":
            uj_eszkoz(eszkozok)
        elif valasztas == "2":
            listaz(eszkozok)
        elif valasztas == "3":
            torol(eszkozok)
        elif valasztas == "0":
            print("Viszlát!")
            break
        else:
            print("Ismeretlen menüpont!")

eszkoz_nyilvantartas()