import random

def dividirLista(lista, tamano):
    resultado =  [lista[n:n + tamano] for n in range(0, len(lista), tamano)]
    return resultado


lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
listaCompaneros = ["Eliana", "LuisV", "Guillermo", "Jorge", "Mauricio", "Alonso", "Aldo",
                   "Matias", "Mauricio", "Luigi", "LuisB", "Emmanuel", "Bastian", "keiby",
                   "JuaP", "Diego", "Daniel"]

div = dividirLista(lista, 4)
print(div)

div = dividirLista(lista, 3)
print(div)

divCompanneros = dividirLista(listaCompaneros, 3) 
print(divCompanneros)


print("Seelccion una subLista al azar")
print("############################################################")
print("############################################################")
print(random.choice(divCompanneros))