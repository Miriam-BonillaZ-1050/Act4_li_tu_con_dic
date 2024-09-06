## Ejemplo del uso de listas 
misnovias = ["Agripina", "Anastacia", "Maria"]
misnumeros= [666,77,10]

##Mostrando mis novias
print(misnovias)

##Mostrando mis numeros raros
print(misnumeros)

print("---Accediendo a los elementos de la lista---")
print(misnovias[-2])
if "Anastacia" in misnovias:
    print("Si, 'Anastacia' esta en la lista de mis novias")
else:
    print("Chale no eres mi novia")

print("Numero de novias: ")
Nnovias=len(misnovias)
print(f"Numero de novias = {Nnovias}")

print("Ciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1
