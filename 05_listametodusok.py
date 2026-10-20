list = [1,5,8,7,4,8,666,555]

print(list)

#lista bejárása
for num in list:
    print(num, end=" ")

print("\n")
#az adott elem megszámolása, hány DB van belőle
print(f"A 8-as szám {list.count(8)} -szer szerepel a listában")

#az adott érték hol helyezkedik el a listában:
print(f"A 666-os szám {list.index(666)+1}. helyen szerepel a listában")

#lista elem hozzáadása:
list.append(5)
print(list)

#az adott helyre elem beszúrása:
list.insert(2,999)
print(list)

#lista elem eltávolítása:
list.remove(5)
print(list)

#a lista utolsó elemének a kitörlése, kivétele
list.pop()
print(list)

#a lista elemeinek a törlése
list.clear()
print(list)
print("*"*40)
list = [17,5,81,79,4,88,666,555]

print(max(list))    #a lista legnagyobb eleme
print(min(list))    #a lista legkisebb eleme
print(sum(list))    #a lista elemeinek az összege

