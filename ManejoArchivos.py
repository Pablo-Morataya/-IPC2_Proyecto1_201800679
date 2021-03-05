from xml.dom import minidom
from collections import Counter
from collections import defaultdict
import numpy as np
#from xml.dom import minidom
import os

class ManejoArchivos():
    
    def obtenerDireccion(self, direccion):
        try: 
            doc = minidom.parse(direccion)
            datos = doc.getElementsByTagName("matriz")
            matriz = []
            for d in datos:
                datos_dentro = d.getElementsByTagName("dato")
                fila = d.getAttribute("n")
                columna = d.getAttribute("m")
                
                lista = []
                contador = 1
                contadorF = 1

                for data in datos_dentro:
                    posicionX = data.getAttribute("x")
                    posicionY = data.getAttribute("y")
                    numeros = data.childNodes[0].nodeValue

                    lista.append(int(numeros))

                    if contador == int(columna):
                        matriz.append(lista)
                        contador = 0
                        lista = []
                        contadorF = contadorF + 1
                    contador = contador + 1
                    
                    if int(posicionY) > int(columna):
                        print("La posición en Y es mayor al numero de columnas")
                        print("\"m\" que le corresponde. Revise el documento")
                        break
                
                    if int(posicionX) > int(fila):
                        print("La posición en X es mayor al numero de columnas")
                        print("\"n\" que le corresponde. Revise el documento")
                        break   
            for i in matriz:
                print(i)
            return matriz
        except: 
            print("La dirección es incorrecta")

    def procesoMatriz(self, matriz):
        binaria = []
        for i in matriz:  
            lista = []
            for j in i:
                
                if int(j) > 0:
                    lista.append(1)

                if int(j) == 0:
                    lista.append(0)
            binaria.append(lista)
        print("")
        print("Calculando Matriz Binaria...")
        for h in binaria:
            print(h)
        
        print("")
        print("Analizando posiciones de tuplas...")
        return binaria
       # self.sumaTuplas(binaria, matriz)
    
    def sumaTuplas(self, binaria, matriz):
        print("")
        salida = []
        contador = 0
        for i, j in zip(binaria, matriz):
            temp = np.array(j)
            contadorA = 1

            for h, l in zip(binaria[(contador+1):(len(binaria)+1)], matriz[(contador+1):(len(binaria)+1)]):
                if i == h and l[0] != True: 
                    print("Sumando las tuplas...")
                    temp = temp + np.array(l)
                    l[0] = 's'
                contadorA = contadorA + 1
            
            if j[0] != 's':
                salida.append(temp)
            
            contador = contador + 1   
        print("Suma final de tuplas... ") 
        print(salida)
        return salida

    def escribirArchivo(self, reducida, direccion):
        
        archivo = open(direccion, "w")
        
        archivo.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        archivo.write("\n")
        archivo.write("<matriz nombre = \"Ejemplo_Salida\" n=\"" + str(len(reducida)) +"\" m=\"" +str(len(reducida[0])) +"\" g=\"" +str(len(reducida)) + "\">\n")

        for fila in range(len(reducida)):
            for columna in range(len(reducida)):
                archivo.write("     <dato x=\"" + str(fila)+ "\" y=\"" + str(columna)+ "\">" +str(reducida[fila][columna]) + "</dato>\n")
        
        archivo.write("</matriz>")
        archivo.close()