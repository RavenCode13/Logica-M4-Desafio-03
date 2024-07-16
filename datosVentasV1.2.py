###################################################################
############### DECLARO MIS VARIABLES AUXILIARES ##################
##############  PUEDEN EXISTIR DOS MODULOS DE AUX #################
###################################################################
def variablesAux():
    print()
###################################################################
####################### DEFINO MIS LISTAS #########################
###################################################################
def datosListas():
    #Datos Personales
    nombres = []
    cedulas = []
    generos = []
    #Datos Ventas
    montosVend = []
    facturasCant = []
    return nombres, cedulas, generos, montosVend, facturasCant
###################################################################
######################## CARGO MIS LISTAS #########################
###################################################################
def datosRegistro(nombres, cedulas, generos, montosVend, facturasCant):
    while True:
        print("\nRegistro de vendedores por favor ingrese valores correctos")
        print("\n - Campo nombre no debe estar vacio - ")
        nombre=input(":::>>> Ingrese el nombre:\n:::>>> ")
        print("\n - Campo cedula no debe estar vacio ni ser numero negativo ó cero - ")
        cedula=int(input(":::>>> Ingrese la cedula:\n:::>>> "))
        print("\n - Campo genero debe contener la letra (F) para las mujeres o (M) para los hombres - ")
        genero=input(":::>>> Ingrese el genero:\n:::>>> ").upper()
        print("\n - Campo monto vendido no puede ser numero negativo - ")
        montoTotal = float(input(":::>>> Ingrese el monto total vendido:\n:::>>> "))
        if montoTotal>-1:
            print("\n - Campo cantidad de facturas no puede ser numero menor a uno - ")
            facturaCant = int(input(":::>>> Ingrese la cantidad de facturas:\n:::>>> "))
        elif montoTotal==0:
            print(" - Como el vendedor no realizo ventas no hubo facturacion por parte del vendedor - ")
            facturaCant = 0
        
        if nombre=="" or cedula<1 or  not genero=="F" or not genero=="M" or (montoTotal<0 and facturaCant<1) or (montoTotal>0 and facturaCant==0):
            print(" - Error en un campo, especificamente en: - ")
            if nombre=="": #Mensaje para error en nombre
                print("Nombre - campo vacio no es permitido")

            if cedula==0: #Mensaje para error en cedula
                print("Cedula - campo no puede ser igual a 0")
            elif cedula<0:
                print("Cedula - campo no puede ser un numero negativo")

            if not genero=="F" or not genero=="M": #Mensaje para error en genero
                print("Genero - campo no puede ser una letra distinta de F o M")

            if montoTotal<0: #Mensaje para error en monto total
                print("Monto  - campo no puede ser un numero negativo")

            if facturaCant==0: #Mensaje para error en cantidad de facturas
                print("Factura - campo no puede ser igual a 0")
            elif facturaCant<0:
                print("Factura - campo no puede ser un numero negativo")
        else:
            print("\n Todos los campos fueron validos registro exitoso")
            break
    nombres.append(nombre)
    cedulas.append(cedula)
    generos.append(genero)
    montosVend.append(montoTotal)
    facturasCant.append(facturaCant)

###################################################################
########################## REPETIR CICLO ##########################
###################################################################
def repetir():
    i = 0
    while True:
        datosRegistro(nombres, cedulas, generos, montosVend, facturasCant)
        pregunta = input("Desea registrar otro Empleado?\n:::>>> Presione cualquier tecla y/ó Enter para continuar\n:::>>> Escriba (NO) para finalizar\n:::>>> ")
        if pregunta.upper() != "NO":
            i=i+1
            print("\nRegistrando Vendedor... ... ... Listo...\n")
        else:
            i=i+1
            print("\nSe registraron ",i)
            print("\nCerrando sesion...\nCerrando programa...")
            break

#******************************************************************#
#************************ Cuerpo Principal ************************#
#******************************************************************#
variablesAux()
nombres, cedulas, generos, montosVend, facturasCant = datosListas()

repetir()
print(nombres)
print(cedulas)
print(generos)
print(montosVend)
print(facturasCant)
