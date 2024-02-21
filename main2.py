import random

def dividirLista(lista, tamano):
    resultado =  [lista[n:n + tamano] for n in range(0, len(lista), tamano)]
    return resultado

listaCompaneros = ["Eliana", "LuisV", "Guillermo", "Jorge", "Mauricio", "Alonso", "Aldo",
                   "Matias", "Mauricio", "Luigi", "LuisB", "Emmanuel", "Bastian", "keiby"]

#listaAzar = []
random.shuffle(listaCompaneros)
print("lista Azar", listaCompaneros)

divCompanneros = dividirLista(listaCompaneros, 3) 
print(divCompanneros)


print("")
print("Seleccion una subLista al azar")
print("############################################################")
print("############################################################")
print(random.choice(divCompanneros))