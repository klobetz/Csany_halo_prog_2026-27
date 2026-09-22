a = 2

print(a)

b="szöveg"

print(b)

b=11

print(b)

print("teszt1")

c = a+b

print(c)

print(b//a)
print(b//a)
print(b%a)
print(b**a)


szam = 6
if szam % 2 == 0 :
    print ("a szám páros")
else:
    print ("a szám páratlan")

#**********************************************************    
bekeres = input("kérek valamit:")

print (bekeres)


szam2 = (input("kérek egy számot:"))

szam2 = int(input("kérek egy számot:"))

if szam2 % 2 == 0 :
    print ("a szám páros")
else:
    print ("a szám páratlan")



print("teszt")

name = "Kata"
age = 20
height = 1.70
bool = False

#típus ellenőrzés:
print(type(name))

print("A nevem: ", name, "Az életkorom: ", age, "A magasságom: ", height)
print(f"neven: {name}, életkor: {age}, magasság: {height} cm")


#kérj be adatot : teljes név, életkor, születési dátum, lakcím, telefonszám, e-mail cím
full_name = input("Kérem a teljes nevét: ")
age = int(input("Kérem az életkorát: "))
birth_date = input("Kérem a születési dátumát (ÉÉÉÉ-HH-NN): ")
address = input("Kérem a lakcímét: ")
phone_number = input("Kérem a telefonszámát: ")
email = input("Kérem az e-mail címét: ")
print(f"Teljes név: {full_name}, Életkor: {age}, Születési dátum: {birth_date}, Lakcím: {address}, Telefonszám: {phone_number}, E-mail cím: {email}")

#összehasonlító operátorok: ==, !=, <, >, <=, >=
print(5 == 5)  # True
print(5 != 5)  # False
print(5 < 10)   # True
print(5 > 10)   # False
print(5 <= 10)  # True
print(5 >= 10)  # False

#képrj be a felhasználótól egy számot, majd dötd el róla hogy a szám nagyobb e mint 100
szam = int(input("Kérek egy számot: "))
if szam > 100:
    print("A szám nagyobb mint 100")
elif szam == 100:
    print("A szám egyenlő 100")
else:
    print("A szám kisebb vagy egyenlő mint 100")

#szám eldöntés pozitív, negatív vagy nulla
szam = int(input("Kérek egy számot: "))
if szam > 0:
    print("A szám pozitív")
elif szam < 0:
    print("A szám negatív")
else:
    print("A szám nulla")


#jelszó ellenőrzés
jelszo = input("Kérem a jelszót: ")
if jelszo == "titkos":
    print("Helyes jelszó")
else:
    print("Helytelen jelszó")

#logikai operátorok: and, or, not
if jelszo == "titkos" and age >= 18:
    print("Hozzáférés engedélyezve")
else:
    print("Hozzáférés megtagadva") 

#or operátor
if jelszo == "titkos" or age >= 18:
    print("Hozzáférés engedélyezve")
else:
    print("Hozzáférés megtagadva")  

#not operátor
if not jelszo == "titkos":
    print("Helytelen jelszó")

#belépési rendszer:
felhasznalonev = "admin"
jelszo = "titkos"

iput_fn = input("Kérem a felhasználónevet: ")
input_jelszo = input("Kérem a jelszót: ")

if input_jelszo == jelszo and iput_fn == felhasznalonev and input_felhasznalonev != "":
    print("belépés engedélyezve")
else:
    print("belépés megtagadva")
    
    