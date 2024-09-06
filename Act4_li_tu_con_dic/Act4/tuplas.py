##Tuplas
arcoiris=("Azul", "Verde","Rojo","Amarillo")
print(arcoiris)
print("-longitud arcoiris")
print(len(arcoiris))

animales=("Pantera",20,"Estatura",1.7)
print(animales)
print("Elementos de la tupla:")
print(animales[1])

rateros=("Juan","Ana","Pedro")
y=list(rateros)
x=tuple(y)
y[0]="Polainas"
print(x)

print("Agregando elementos")
Nanimal=("Boby","Chetos")
y=list(Nanimal)
y.append("Tontolin")
otratupla=tuple(y)

print(otratupla)
print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)