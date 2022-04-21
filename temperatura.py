
"""Programa No. 3 :
Programa para convertir temperatura """


print("--------")
print("----conversor de temperatura----")
print("--------")

#input
c=int(input("digite grados celcius: "))

# Processing
k=c+273.15
F=1.8*c+32

#output
print("\nResultado\n")

print(str(c) + " grados celcius es igual a: " + str(F) + " grados farenheit")
print(str(c) + " grados celcius es igual a: " + str(k) + " grados kelvin")