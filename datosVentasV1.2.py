# Vamos a hacer todo Amuñuñado #
################################
def pantallaPrincipal(mensaje):
    print(f"""{mensaje}""")
#Termino pantallaPrincipal()
def variableAux(): #Defino valiables que me puedan ayudar
    #contador01, contador02, acumulador00, acumulador01, acumulador02, acumulador03 
    contFemeninas = 0
    contMasculinos = 0
    acumGenMontoTotal = 0
    acumGenCantFacturas = 0
    acumMascMontoTotal = 0
    acumMascCantFacturas = 0
    terminar = False
    return terminar, contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas
#Termino variableAux() ###########################################################################################
def datosListas(): #Defino mis listas
    listasNombres = []
    listasCedulas = []
    listasGeneros = []
    listasMontosFinales = []
    listasCantFacturas = []
    listasPromEmpleado = []
    return listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, listasPromEmpleado
#Termino datosListas() ###########################################################################################
def menuOpciones(contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas, terminar):
    while True:
        print("Seleccione una opcion:\n:::>>> (1) Ingresar Empleados\n:::>>> (2) Mostrar datos de todos los Empleados\n:::>>> (3) Mostrar datos de un Empleado en especifico\n:::>>> (4) Mostrar promedio General y Promedio por Empleados\n:::>>> (5) Mostrar promedio de ventas total del Genero Masculino\n:::>>> (6) Mostrar el empleado con Mayor monto de venta\n:::>>> (7) Mostrar el empleado con Menor monto de venta\n:::>>> (8) Mostrar listado con empleados con monto Mayor ( > ) a 500$\n:::>>> (9) Porcentaje de Empleados Masculinos y de Empleados Femeninos\n:::>>> (10) Salir del programa y mostrar todos los Resultados")
        if len(listasNombres) == 0: print("\n:::>>>Por favor ingrese por lo menos 1 registro si desea entrar en las opciones del 2 al 9")
        opcion = int(input("\nIngrese la Opcion\n:::>>> "))
        if (opcion>0 and opcion<11):
            if (opcion > 1 and opcion < 10 and len(listasNombres) == 0): print("\n:::>>>Por favor ingrese por lo menos 1 registro si desea entrar en las opciones del 2 al 9\n")
            else: break
        else: print("\n:::>>>Opcion no valida\n")
    match opcion:
        case 1:
            while True:
                contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas = datosCargar(contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas)
                finalizarRegistro = terminarPrograma(terminar, "\nDesea volver a ingresar otro empleado?\n:::>>>Presione cualquier tecla y/o Enter para registrar a otro empleado\n:::>>>Escriba (NO) para entrar al menu de opciones\n:::>>>")
                if finalizarRegistro == True: break
        case 2: datosMostrar(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, True, False)
        case 3: datosMostrar(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, False, False)
        case 4: calcPromedio(acumGenMontoTotal, acumGenCantFacturas, listasNombres, listasPromEmpleado, True, "El promedio General de la empresa por monto total vendido es de:")
        case 5: calcPromedio(acumMascMontoTotal, acumMascCantFacturas, listasNombres, listasPromEmpleado, False, "El promedio de ventas de todos los vendedores de género masculino es de")
        case 6: calcExtremos(True, listasNombres, listasMontosFinales, -1, "alta")
        case 7: calcExtremos(False, listasNombres, listasMontosFinales, 9999999999, "bajo")
        case 8: datosMostrar(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, True, True)
        case 9: porcEntreGeneros(contMasculinos, contFemeninas, listasGeneros)
        case 10:
            terminar = terminarPrograma(terminar, "\nDesea volver al menu o terminar el programa?\n:::>>>Presione cualquier tecla y/o Enter para volver al menu de opciones\n:::>>>Escriba (NO) para finalizar el programa\n:::>>>")
            if terminar == True:
                if len(listasNombres) > 0:
                    datosMostrar(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, True, False)
                    calcPromedio(acumGenMontoTotal, acumGenCantFacturas, listasNombres, listasPromEmpleado, True, "El promedio General de la empresa por monto total vendido es de:")
                    calcPromedio(acumMascMontoTotal, acumMascCantFacturas, listasNombres, listasPromEmpleado, False, "El promedio de ventas de todos los vendedores de género masculino es de")
                    calcExtremos(True, listasNombres, listasMontosFinales, -1, "alta")
                    calcExtremos(False, listasNombres, listasMontosFinales, 9999999999, "bajo")
                    datosMostrar(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, True, True)
                    porcEntreGeneros(contMasculinos, contFemeninas, listasGeneros)
        case _: print("Error Fatal")
    if opcion > 1 and opcion < 10: pausa = input("\n:::>>> Presiona enter para continuar\n")
    return contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas, terminar
#Termino menuOpciones() ##########################################################################################
def datosCargar(contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas):
    while True:
        nombre = input("\n- Ingrese su Nombre -\n  Datos no permitidos:\n:::>>>Campo Vacio\n\n:::>>>  ")
        cedula = int(input("\n- Ingrese su numero de cedula -\n  Datos no permitidos:\n:::>>>Numero igual a Cero\n:::>>>Numeros negativos\n:::>>>Cedula ya Registrada\n\n:::>>>  "))
        genero = input("\n- Ingrese su Genero -\n  Datos Permitidos:\n:::>>>(F) para Mujeres\n:::>>>(M) para hombres\n  Datos no permitidos:\n:::>>>Cualquier caso contrario a las anteriores dos\n\n:::>>> ").upper()
        montoFinal = float(input("\n- Ingrese el monto total vendido -\n  Datos no permitidos:\n:::>>>Numeros negativos\n\n:::>>> "))
        if montoFinal > 0: cantFacturas = int(input("\n- Ingrese la cantidad de facturas vendidas -\n  Datos no permitidos:\n:::>>>Numero igual a Cero\n:::>>>Numeros negativos\n\n:::>>>  "))
        condicion01 = datosValidarString(nombre,"", False)
        condicion02 = datosValidarIntOrFloat(cedula, 0, listasCedulas, False, True)
        condicion03 = (datosValidarString(genero, "F", True) or datosValidarString(genero, "M", True))
        condicion04 = datosValidarIntOrFloat(montoFinal, -1, listasMontosFinales, False, False)
        if montoFinal > 0: condicion05 = datosValidarIntOrFloat(cantFacturas, 0, listasCantFacturas, False, False)
        else: 
            condicion05 = True
            cantFacturas = 0
        if condicion01 and condicion02 and condicion03 and condicion04 and condicion05 == True: break
        else: print("\nError en un dato por favor lea detenidamente los datos permitidos")
    contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas, promEmpleado = contarAndAcumular(genero, montoFinal, cantFacturas, contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas)
    listasNombres.append(nombre)
    listasCedulas.append(cedula)
    listasGeneros.append(genero)
    listasMontosFinales.append(montoFinal)
    listasCantFacturas.append(cantFacturas)
    listasPromEmpleado.append(promEmpleado)
    return contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas
#Termino datosCargar() ###########################################################################################
def contarAndAcumular(dato01, dato02, dato03, contador01, contador02, acumulador00, acumulador01, acumulador02, acumulador03):
    datoPromedio = 0
    if dato01 == "F":
        contador01 = contador01 + 1
    elif dato01 == "M":
        contador02 = contador02 + 1
        acumulador02 = acumulador02 + dato02
        acumulador03 = acumulador03 + dato03
    acumulador00 = acumulador00 + dato02
    acumulador01 = acumulador01 + dato03
    if dato02>0 and dato03>0: datoPromedio = dato02/dato03
    else: datoPromedio = 0
    return contador01, contador02, acumulador00, acumulador01, acumulador02, acumulador03, datoPromedio  
#Termino contarAndAcumular() #####################################################################################
def datosMostrar(arreglo01, arreglo02, arreglo03, arreglo04, arreglo05, tipoMostrar, filtrado):
    if tipoMostrar == True:
        print("- Lista de Empleados -\n")
        for pos in range(len(arreglo01)):
            if filtrado == True:
                if arreglo04[pos]>500: print(f"#{pos+1} | Nombre: {arreglo01[pos]} | Cedula: {arreglo02[pos]} | Genero: {arreglo03[pos]} | Monto total Vendido: {arreglo04[pos]} | Cantidad de Facturas: {arreglo05[pos]}")
            else: print(f"#{pos+1} | Nombre: {arreglo01[pos]} | Cedula: {arreglo02[pos]} | Genero: {arreglo03[pos]} | Monto total Vendido: {arreglo04[pos]} | Cantidad de Facturas: {arreglo05[pos]}")
    else:
        while True:
            indice = int(input("- Ingrese el indice del empleado a Buscar -\n  Datos no permitido:\n:::>>>Numero igual a 0\n:::>>>Numeros negativos\n:::>>>Numeros fuera del rango\n\n:::>>> "))
            condicion01 = datosValidarIntOrFloat(indice, 0, listasNombres, False, False)
            condicion02 = indice<=len(arreglo01)
            if condicion01 and condicion02 == True:
                print(f"#{indice} | Nombre: {arreglo01[indice-1]} | Cedula: {arreglo02[indice-1]} | Genero: {arreglo03[indice-1]} | Monto total Vendido: {arreglo04[indice-1]} | Cantidad de Facturas: {arreglo05[indice-1]}")
                break
            else: print("\nError en un dato por favor lea detenidamente los datos permitidos\n")
#Termino datosMostrar() ##########################################################################################
def calcPromedio(dato01, dato02, arreglo01, arreglo02, mostrarTodo, mensaje):
    if mostrarTodo == True or mostrarTodo == False:
        if dato01 > 0 and dato02 > 0: promGeneral = dato01/dato02
        else: promGeneral = 0
        print(f"{mensaje} {promGeneral}")
    if mostrarTodo == True:
        print("- Lista de promedios por empleados -")
        for pos in range(len(arreglo01)):
            print(f"#{pos+1} Nombre: {arreglo01[pos]} | Promedio por Factura: {arreglo02[pos]}")
#Termino calcPromedio() ##########################################################################################
def calcExtremos(MayorOrMenor, arreglo01, arreglo02, rango, mensaje):
        for pos in range(len(arreglo01)):
            if MayorOrMenor == True:
                if arreglo02[pos]>rango:
                    indice=pos
                    rango=arreglo02[pos]
            if MayorOrMenor == False:
                if arreglo02[pos]<rango:
                    indice=pos
                    rango=arreglo02[pos]
        print(f"El Empleado {arreglo01[indice]} obtuvo la venta mas {mensaje} de: {rango}")
#Termino calcExtremos() ##########################################################################################
def porcEntreGeneros(dato01, dato02, arreglo):
    porcHombres = dato01/len(arreglo)
    porcMujeres = dato02/len(arreglo)
    print(f"Hay registrado {len(arreglo)} Empleados (100%)\nHay registradas {dato02} Empleadas ({porcMujeres*100}%)\nHay registrados {dato01} Empleados ({porcHombres*100}%)")
#Termino porcEntreGeneros ########################################################################################
def datosValidarString(dato, condicion, boolean):
    validado = False
    if boolean == True:
        if dato==condicion: validado = True
    else:
        if dato!=condicion: validado = True
    return validado
#Termino datosValidarNumero ######################################################################################
def datosValidarIntOrFloat(dato, condicion, arreglo, boolean, hacerCiclo): #boolean lo uso para encontrar un numero y para que ese mismo valor retorne la validacion
    if hacerCiclo == True:
        pos = 0
        while pos<len(arreglo):
            if arreglo[pos] == dato: boolean = True
            pos=pos+1
        if dato>condicion and (boolean == False or len(arreglo) == 0): boolean = True
        else:
            if dato == condicion: print(":::>>> Cedula no puede ser igual a 0...\n")
            if dato < condicion: print(":::>>> Cedula no puede ser numero negativo...\n")
            if dato > condicion and boolean == True:
                print(":::>>> Cedula ya registrada por favor contacte a soporte...\n")
                boolean = False
    else:
        boolean = False
        if dato>condicion: boolean = True
    return boolean
#Termino datosValidar() ##########################################################################################
def terminarPrograma(terminar, mensaje):
    terminar = False
    pregunta = input(f"{mensaje}  ")
    if pregunta.upper() != "NO": print(":::>>> Por favor espere...\n:::>>> Listo...\n")
    else: terminar = True
    return terminar
#Termino terminarPrograma(terminar) ##############################################################################

#Cuerpo Principal
pantallaPrincipal("---------------------------------------------------------------\n        Bienvenidos al sistema de Gestion para Ventas\nCampos Solicitados: Nombre, Monto Vendido, Cantidad de Facturas\n---------------------------------------------------------------\n")
terminar, contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas = variableAux()
listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas, listasPromEmpleado = datosListas()
while True:
    contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas, terminar = menuOpciones(contFemeninas, contMasculinos, acumGenMontoTotal, acumGenCantFacturas, acumMascMontoTotal, acumMascCantFacturas, terminar)
    if terminar == True: break