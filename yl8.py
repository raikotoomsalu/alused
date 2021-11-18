x = int(input("Sisesta positviine täisarv: "))

if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print("Tegu on liigaastaga.")

else:
    print("Tegu pole liigaastaga.")
