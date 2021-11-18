import math

radius = input("Raadius: ")

ümbermõõt = math.pi * float(radius) * 2
pindala = math.pi * float(radius) * float(radius)

print("Ümbermõõt on: ", round(ümbermõõt), "cm")
print("Pindala on: ", round(pindala), "cm2")

