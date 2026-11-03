#paraméter nélküli függvény
def osszeadas():
    print(3+2)

#függvény meghívása:
osszeadas()

#visszatérési érték bevezetése
def osszeadas2():
    a = 4
    b = 5
    c=a+b
    return c #visszatérési érték

print(osszeadas2())

#paraméteres függvények
def szorzas(a,b):
    return a*b

print(f"a szorzás eredménye: {szorzas(5,5)}")

#csillagok kiíratása
def csillag(x,y):
    for sor in range(y):
        for oszlop in range(x):
            print("*", end="")
        print()

csillag(10,2)

