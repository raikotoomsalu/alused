x = int(input("Sisesta esimene arv: "))
y = int(input("Sisesta teine arv: "))
z = int(input("Sisesta kolmas arv: "))

if x>y and x>z:
    print("Kõige suurim number on X: ", x)
if y>x and y>z:
    print("Kõige suurim number on Y: ", y)
if z>y and z>x:
    print("Kõige suurim number on X: ", z)

