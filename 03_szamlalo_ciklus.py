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
