name = input("Mis su nimi on?: ")

print("Tere ", name, "!", sep='')

location = input("Kus sa elad?: ")

if location == "Saaremaal" :
    print("Tere saarlane!")

age = int(input("Kui vana sa oled?: "))

if age <18:
    print("Sa pole piisavalt vana, et autotki juhtida!")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul?")
elif age >18:
    print("Sa oled piisavalt vana, et autot juhtida!")