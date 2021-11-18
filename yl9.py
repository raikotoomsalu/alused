a = int(input("Sisesta esimese haara väärtus: "))
b = int(input("Sisesta teise haara väärtus: "))
c = int(input("Sisesta aluse väärtus: "))

if a + b <= c or b + c <= a or a + c <= b:
    print("Sellist kolmnurka ei eksisteeri.")

elif a == b and b == c: 
    print("Tegu on võrdkülgse kolmnurgaga.")

elif a == b or b == c or a == c:
    print("Tegu on võrdhaarse kolmnurgaga.")

else:
    print("Tegu on erikülgse kolmnurgaga.")