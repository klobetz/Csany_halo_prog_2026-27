bekeres = int(input("Kérek egy számot ami 10-nél nagyobb: "))
if bekeres >= 10:
    print(f"a bekért szám: {bekeres} nagyobb mint 10")

#kérj be egy betűt: "a" vagy "b" vagy "c" ennek megfelelően írja ki, hogy melyik választ adtad meg.
# PL: b akkor kiírja hogy a b a hzelyes válasz.
bekeres1 = input("Kérek egy betűt: a,b vagy c ")

if bekeres1 == "a":
    print("a megadott válasz az 'a'")
elif bekeres1 == "b":
    print("a megadott válasz az 'b'")
elif bekeres1 == "c":
    print("a megadott válasz az 'c'")

#kérj be egy számot: döntsd el róla hogy pozítív negatív vagy 0-a
bekeres3 = int(input("Kérek egy számot: "))
if bekeres3 < 0:
    print("a szám negatív")
else:
    if bekeres3 > 0:
        print("a szám pozitív")
    else:
        print("A bekért szám 0-a")