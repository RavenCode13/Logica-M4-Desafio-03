# Vamos a hacer todo Amuñuñado #
################################
def variableAux(): #Defino valiables que me puedan ayudar
    terminar = False
    return terminar
#Termino variableAux() ####################################################################################
def datosListas(): #Defino mis listas
    listasNombres = []
    listasCedulas = []
    listasGeneros = []
    listasMontosFinales = []
    listasCantFacturas = []
    return listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas
#Termino datosListas() ####################################################################################
def datosCargar():
    while True:
        nombre = input("- Ingrese su Nombre -\n  Datos no permitidos:\n:::>>>Campo Vacio\n\n:::>>>  ")
        cedula = int(input("- Ingrese su numero de cedula -\n  Datos no permitidos:\n:::>>>Numero igual a Cero\n:::>>>Numeros negativos\n\n:::>>>  "))
        genero = input("- Ingrese su Genero -\n  Datos Permitidos:\n:::>>>(F) para Mujeres\n:::>>> (M) para hombres\n  Datos no permitidos:\nCualquier caso contrario a las anteriores dos\n\n:::>>> ").upper()
        montoFinal = float(input("- Ingrese el monto total -\n  Datos no permitidos:\n:::>>>Numeros negativos\n\n:::>>> "))
        condicion01 = datosValidarString(nombre,"", False)
        condicion02 = datosValidarIntOrFloat(cedula, 0, listasCedulas, False, True)
        condicion03 = (datosValidarString(genero, "F", True) or datosValidarString(genero, "M", True))
        condicion04 = datosValidarIntOrFloat(montoFinal, -1, listasMontosFinales, False, False)
        print(f"Cond 1 {condicion01} , Cond 2 {condicion02} , Cond 3 {condicion03} , Cond 4 {condicion04} ,")
        if condicion01 and condicion02 and condicion03 and condicion04 == True: break
    listasNombres.append(nombre)
    listasCedulas.append(cedula)
    listasGeneros.append(genero)
    listasMontosFinales.append(montoFinal)
#Termino datosCargar() #####################################################################################
def datosValidarString(dato, condicion, boolean):
    validado = False
    if boolean == True:
        if dato==condicion: validado = True
    else:
        if dato!=condicion: validado = True
    return validado
#Termino datosValidarNumero ################################################################################
def datosValidarIntOrFloat(dato, condicion, arreglo, boolean, hacerCiclo):
    if hacerCiclo == True:
        pos = 0
        while pos<len(arreglo):
            if arreglo[pos] == dato: boolean = True
            pos=pos+1
        if dato>condicion and (boolean == False or len(arreglo) == 0): boolean = True
        else:
            if dato == condicion: print(":::>>> Cedula no puede ser igual a 0...\n")
            if dato < condicion: print(":::>>> Cedula no puede ser numero negativo...\n")
            if dato > condicion and boolean == True: print(":::>>> Cedula ya registrada por favor contacte a soporte...\n")
    else:
        boolean = False
        if dato>condicion: boolean = True
    return boolean
#Termino datosValidar() ##########################################################################################
def terminarPrograma(terminar):
    terminar = False
    pregunta = input("Desea guardar y repetir el proceso?\n:::>>>Presione cualquier tecla y/o Enter para continuar\n:::>>>Escriba (NO) para finalizar\n:::>>>  ")
    if pregunta.upper() != "NO": print(":::>>> Guardando datos...\n:::>>> Listo...\n")
    else: terminar = True
    return terminar
#Termino terminarPrograma(terminar) ##############################################################################

#Cuerpo Principal
terminar = variableAux()
listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas = datosListas()
while True:
    datosCargar()
    print(listasNombres, listasCedulas, listasGeneros, listasMontosFinales, listasCantFacturas)
    terminar = terminarPrograma(terminar)
    if terminar == True: break