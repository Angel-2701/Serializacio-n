import pickle

#Codificar lista a codigo binario
#lista_nombres=["Pedro","Ana","María","Isabel"]
#Escritura binaria:
#fichero_binario=open("lista_nombres","wb")

#pickle.dump(lista_nombres, fichero_binario) #Archivo guardado en disco duro y fichero guardado en memoria

#fichero_binario.close()

#del(fichero_binario)

#Leer informacion de archivo binario:

fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)

print(lista)