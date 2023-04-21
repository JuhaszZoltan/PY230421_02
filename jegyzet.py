# "alprogramok"
# függvények, eljárások, metódusok

# onnan tudod, hogy mi function vagy method,
# hogy van mögötte kerek zárójel

# zárójelbe ún. "paramétereket" v. "attributumokat" írunk
# ezek meghatározzák az alprogram működését

# ELJÁRÁS, ha nem ad vissza értéket

# a paraméter lehet literál
print('hello, world')

# változó
hlo:str = 'helló világ!'
print(hlo)

# vagy akár kifejezés
szokoz:str = ' '
print('hello' + szokoz + 'vilag')

# FÜGGVÉNY az, aminek van visszatérési értéke
osszeg:int = sum([3, 2, 5])
print(osszeg)

# mgj: nevezéktanilag a python NEM különbözteti meg
# a függvényeket az eljárásoktól, mindkettő "function"

# METÓDUS az a függvény vagy eljárás,
# ami egy osztályon belül van
# 'tagfüggvény'-nek is szokták hívni

lst:list[int] = [4, 6, 2]

print(lst)
# példány szintű eljárás
lst.sort()
print(lst)

szoveg:str = "VaLaMi"
# példány szintű függvény
modositott_szoveg = szoveg.lower()
print(szoveg)
print(modositott_szoveg)

