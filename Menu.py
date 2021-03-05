
from numpy import mat
from ManejoArchivos import ManejoArchivos
from Graficar import Graficar

a = ManejoArchivos()
b= Graficar()

def menu():
    matrizces = []
    matrizBinaria = []
    matrizReducida = None
    #C:\Users\pablo\Desktop\Nueva carpeta\entrada.xml
    estado = True
    print("════════════════════════════════════════════════")
    print("║                BIENVENIDO                    ║ ")
    print("════════════════════════════════════════════════")
    reporte = ""
    while estado:
        print("")
        print("════════════════════════════════════════════════")
        print("║                                              ║")
        print("║ Escoja una opción :                          ║")
        print("║                                              ║")
        print("════════════════════════════════════════════════")
        print("║ 1. Cargar archivo de entrada  :              ║")
        print("║ 2. Procesar Archivos           :             ║")
        print("║ 3. Escribir Archivo Salida  :                ║")
        print("║ 4. Mostrar Datos Del Estudiante :            ║")
        print("║ 5. Generar Gráfica :                         ║")
        print("║ 6. Salir :                                   ║")
        print("════════════════════════════════════════════════")
        print(">>")
        entrada = input()

        if int(entrada) == 1:
            print("")
            print("════════════════════════════════════════════════")
            print("║         INGRESE LA RUTA DEL ARCHIVO:         ║")
            print("════════════════════════════════════════════════")
            print(">>")
            direccion = input()
            print("")
            matrizces.append(a.obtenerDireccion(direccion))

        elif int(entrada) == 2:
            
            if matrizces == None:
                print("Debe ingresar una matriz para podre analizar")
            else:
                print("")
                print("════════════════════════════════════════════════")
                print("║             PROCESO DE ARCHIVOS              ║")
                print("════════════════════════════════════════════════")
                print("")
                print("║ Qué matriz desea procesar:                   ║")
                posicion = (input())
                
                if int(posicion) > len(matrizces): 
                    print("No existe ese número de matriz")
                if int(posicion) <= len(matrizces):
                    matrizBinaria = a.procesoMatriz(matrizces[int(posicion)-1])
                    matrizReducida = a.sumaTuplas(matrizBinaria, matrizces[int(posicion)-1])
                else:
                    print("Escriba un valor númerico")
                print("")

        elif int(entrada) == 3:
            
            if matrizReducida == None:
                print("No se ha procesado ninguna matriz")
            else: 
                print("")
                print("════════════════════════════════════════════════")
                print("║          ESCRIBIR ARCHIVO DE SALIDA          ║")
                print("════════════════════════════════════════════════")
                print("Escriba la dirección del archivo")
                direccion = input()
                a.escribirArchivo(matrizReducida, direccion)
        elif int(entrada) == 4:
            print("")
            print("")
            print("════════════════════════════════════════════════")
            print("║             DATOS DEL ESTUDIANTE             ║")
            print("════════════════════════════════════════════════")
            print("║                                              ║")
            print("║ Nombre: Pablo Fernando Victorio Morataya     ║")
            print("║ Carnet: 201800679                            ║")
            print("║ Correo: moratayapablo.06@gmail.com           ║")
            print("║ Curso: Lenguajes Formales, Sección A-        ║")
            print("║ Fecha: 16 de Febrero de 2021                 ║")
            print("║                                              ║")
            print("════════════════════════════════════════════════")
            
        elif int(entrada) == 5:
            
            if matrizces == None:
                print("Debe ingresar una matriz para podre analizar")
            else:
                print("")
                print("════════════════════════════════════════════════")
                print("║          SE HA GENERADO LA GRÁFICA           ║")
                print("════════════════════════════════════════════════")
                print("")
                print("║ Qué matriz desea graficar:                   ║")
                print(">>")
                posicion = (input())
                #b.graficar(matrizces[0])
                if int(posicion) > len(matrizces): 
                        print("No existe ese número de matriz")
                if int(posicion) <= len(matrizces):  
                    b.graficar(matrizces[0])
                else:
                    print("Escriba un valor númerico")
                print("")

        elif int(entrada) == 6:
            print("")
            print("════════════════════════════════════════════════")
            print("║ Gracias :D                                   ║")
            print("════════════════════════════════════════════════")
            estado = False
        else:
            print("Escriba una opción valida")

a = menu()