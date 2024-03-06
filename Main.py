from os import startfile, system
import xml.etree.ElementTree as ET 
from Estructuras.Lista import Lista
from Piso import Piso
from Patron import Patron
import re

Listan = Lista()

def abrir_archivo(rutaArchivo):
    tree = ET.parse(rutaArchivo)
    root = tree.getroot()
    
    for piso_elem in root.findall('piso'):
        nombre = piso_elem.get('nombre')
        filas = int(piso_elem.find('R').text.strip())
        columnas = int(piso_elem.find('C').text.strip())
        precioF = int(piso_elem.find('F').text.strip())
        precioS = int(piso_elem.find('S').text.strip())
        
        
        patrones = []
        for patron_elem in piso_elem.find('patrones').findall('patron'):
            codigo = patron_elem.get('codigo')
            azulejos = patron_elem.text.strip()
            patron = Patron(codigo, azulejos)
            patrones.append(patron)
        piso = Piso(nombre, filas, columnas, precioF, precioS, patrones)
        
        Listan.insertar(piso)
    Listan.imprimir()
    pass

def Algoritmo(patroncodigo,patroncodigofin,filas, columnas,voltear,cambiar):
    if patroncodigo == patroncodigofin:
        print("el patron es el mismo por lo que el costo mínimo es de 0")
    else:
        Ini = re.findall('B', patroncodigo)
        Fina = re.findall('B', patroncodigofin)
        if len(Ini) == len(Fina):
            print("felicidades no hay que darl switch a ningun azulejo")
        else:
            preciocambio = len(Ini) - len(Fina) 
            print("hay que darle switch a"+str(preciocambio)+" azulejo y eso tiene un precio de "+str(preciocambio*voltear))
            contador = 0
            contprecio = 0
            for i in range(filas):
                for j in range(columnas):
                    if patroncodigo[(contador*columnas)+j] == patroncodigofin[(contador*columnas)+j]:
                        pass
                    else:
                        contprecio = contprecio+1     
                        print("hay que cambiar 2 azulejos")
                contador = contador +1
            total = (preciocambio*voltear)+(contprecio*cambiar)
            print("el precio optimo es:",total)
                        



def SeleccionPisoPatrones():
    Listan.imprimir()
    pisoselec = input("Estos son los pisos disponibles ingresa el código del piso que deseas seleccionar:")
    existencia = Listan.existepiso(pisoselec)
    if existencia is True:
        Listan.buscarcodigos(pisoselec)
        codpatronselec = input("Estos son los patrone disponibles para el piso "+pisoselec+" ingresa el código del patron que deseas seleccionar:")
        filas,columnas = Listan.devolverFyC(pisoselec)
        print("el patron tiene ",filas,"filas y ",columnas," columnas" )
        patroncodigo = Listan.buscarpatron(pisoselec,codpatronselec)
        print("este es el patrón del código seleccionado")
        print(patroncodigo)
        pos = "Inicial"
        generarpatronpisoinicial(pisoselec,codpatronselec,filas,columnas,patroncodigo, pos)
        Listan.buscarcodigos(pisoselec)
        codpatronselecfin = input("estos son los codigos disponibles ahora puedes seleccionar al patron que deseas cambiar:")
        patroncodigofin = Listan.buscarpatron(pisoselec,codpatronselecfin)
        print("este es el patrón del código seleccionado")
        print(patroncodigofin)
        pos = "Final"
        voltear,cambiar = Listan.devolverprecios(pisoselec)
        print(voltear,cambiar)
        generarpatronpisoinicial(pisoselec,codpatronselecfin,filas,columnas,patroncodigofin, pos)
        Algoritmo(patroncodigo,patroncodigofin,filas, columnas,voltear,cambiar )
    else:
        print("Lo siento pero el piso no se ha encontrado por favor verifica que sea el nombre correcto")

def ordenarcodigos():
    Listan.imprimir()
    pisoselec = input("Estos son los pisos disponibles ingresa el código del piso que deseas seleccionar:")
    existencia = Listan.existepiso(pisoselec)
    if existencia is True:
        Listan.ordenarcodigos1(pisoselec)
    else:
        print("Lo siento pero el piso no se ha encontrado por favor verifica que sea el nombre correcto")

def generarpatronpisoinicial(nombre,codigo, filas, columnas,patron,caracter):
    if filas == 0 or columnas == 0:
        print('DIMENSIONES INVÁLIDAS:')
        return

    textoDOT = ''' digraph G { \n
    node [shape=plaintext]; \n
    edge [style=invis]; \n

    label = \"NombrePiso = ''' + nombre + '''       Código = ''' + codigo + '''\n PATRON ''' + caracter.upper() + '''\"
    \n

    piso [\n label=<<TABLE border = \"1\" cellspacing=\"0\" cellpadding=\"10\">
        '''

    leerpalabra = patron
    contador = 0
    for i in range(filas):
        textoDOT += "         <tr>"
        for j in range(columnas):
            if leerpalabra[(contador*columnas)+j] == "B":
                textoDOT += f"<td bgcolor=\"white\"></td>"
            elif leerpalabra[(contador*columnas)+j] == "N":
                textoDOT += f"<td bgcolor=\"black\"></td>"
        textoDOT += "         </tr>\n"
        contador = contador +1
        #contador = i * columnas

    textoDOT += "</TABLE>>\n shape=none\n ];"
    textoDOT += "}\n"

    with open("ejemplo3.dot", "w") as dot_file:
        dot_file.write(textoDOT)

    system('dot -Tpdf ejemplo3.dot -o ejemplo3.pdf')
    startfile("ejemplo3.pdf")

def Ordenarpisoalf():
    Listan.BubbleDescendente()
    print("1. Seleccionar Piso y ordenar codigos ")
    print("2. regresar al menú anterior")
    opc = input("Ingrese la opción que del menú que desea realizar:")
    if opc == "1":
        ordenarcodigos()
        pass
    elif opc == "2":
        print("regresando al menu anterior...")#termina la funcion para regresar a la anterior ventana 
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")

def mostrar_menu3():# Menu tercero donde se muestran las opciones de cargar archivo y regresar a la ventana anterior
    print("1. Seleccionar Piso y Patrón ")
    print("2. regresar al menú anterior")
    print("3.ordenar en forma alfabética")
    opc = input("Ingrese la opción que del menú que desea realizar:")
    if opc == "1":
        SeleccionPisoPatrones()
        mostrar_menu3()
        pass
    elif opc == "2":
        print("regresando al menu anterior...")#termina la funcion para regresar a la anterior ventana 
    elif opc == "3":
        Ordenarpisoalf()
        mostrar_menu2()#termina la funcion para regresar a la anterior ventana   
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
        mostrar_menu3()#Mostrar de nuevo el menu por si el usuario no ingreso alguna opcion valida

def mostrar_menu2():# Menu secundario donde se muestra el modulo petmanager y salir del programa
    print("Funciones Disponibles")
    print("1. Cargar Archivo")
    print("2. Salir")   
    opc = input("Ingrese la opción que del menú que desea realizar:")
    if opc == "1":
        abrir_archivo('entrada.xml') #Funcion por si el usuario selecciona cargar archivo
        mostrar_menu3()#llamada a la siguiente ventana
        mostrar_menu2()#Regreso al menu si el usuario lo selecciona en la siguiente ventana
    elif opc == "2":
        print("saliendo del programa...")   
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
        mostrar_menu2()#Mostrar de nuevo el menu por si el usuario no ingreso alguna opcion valida

def mostrar_menu(): #Menu principal donde se muestra la caratula
    print("=== Menú Principal ===")
    print("Pisos de Guatemala, S.A.")
    print("")
    print("Bievenido a nuestra página")
    opcion = input("Presiones Enter para continuar: ")
    mostrar_menu2()#llamada a la siguiente ventana al presionar enter
    
mostrar_menu()#Llamada al menú principal 