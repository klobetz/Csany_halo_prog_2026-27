a =1
while a <= 10:
    print(a)
    a += 1

#feladat szám kiíratása egy válaszig
beker = int(input("kérek egy számot: "))
i=0
while i <= beker:
    print(i, end=" ,")
    i = i + 1

osszeg = 0
while True:
    szambeker = input("Add meg a számot, (ha szóközt nyomsz akkor kilép): ")
    if szambeker == "":
        break
    else:
        osszeg += int(szambeker)

print(f"a számok összege: {osszeg}")
