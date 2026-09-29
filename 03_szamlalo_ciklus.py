print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

print(f"\n")
for i in range(5):
    print("szeretem a programozást")

print(f"\n")
for i in range(1, 11):
    print(i)

print(f"\n", *range(1, 11))

for i in range(1, 11):
    print(i, end=" ,")
else:
    print("lefutott a ciklus")

gyumolcsok = ["alma", "körte", "banán", "narancs", "kiwi"]
print(gyumolcsok)

for gyumolcs in gyumolcsok:
    print(gyumolcs)

tulajdonsagok = ["érett", "nagy", "nyers"]

for tuladonsag in tulajdonsagok:
    for gyumolcs in gyumolcsok:
        print(tuladonsag, gyumolcs)

for i in gyumolcsok:
    print(i, end=" ,")

print(f"\na listám elemei: {len(gyumolcsok)}")
print(f"\na listám utolsó eleme: {gyumolcsok[len(gyumolcsok)-1]}")
print(f"a gyümölcs változó tartalma: {gyumolcs}")
print(f" a lista első eleme: {gyumolcs[0]}")

valtozo = "szövegbevitel"
print(valtozo[0])

for i in valtozo:
    print(i)
print(len(valtozo))


print(f"\naz első gyümölcs a listából: {gyumolcsok[0]}")


