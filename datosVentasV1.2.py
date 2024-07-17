# Vamos a hacer todo Amuñuñado #
################################
def variableAux(): #Defino valiables que me puedan ayudar
    terminar = False
    return terminar
#Termino variableAux()
def datosListas(): #Defino mis listas
    listasNombres = []
    listasCedulas = []
    listasGeneros = []
    listasMontosFinales = []
    listasCantFacturas = []
#Termino datosListas()
#def datosCargar():
def terminarPrograma(terminar):
    terminar = False
    pregunta = input("Desea guardar y repetir el proceso?\n:::>>>Presione cualquier tecla y/o Enter para continuar\n:::>>>Escriba (NO) para finalizar\n:::>>>  ")
    if pregunta.upper() != "NO":
        print(":::>>> Guardando datos...\n:::>>> Listo...")
    else:
        terminar = True
    return terminar
        

#Cuerpo Principal
terminar = variableAux()
while True:
    datosListas()
    terminar = terminarPrograma(terminar)
    if terminar == True:
        break
