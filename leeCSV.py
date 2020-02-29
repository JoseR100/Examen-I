import pandas as pd


#Carga el padron nacional en una varialble llamada miPadronm se utiliza el ISO para poder utilizar los difentes unicodes.
miPadron = pd.read_csv('./Data/PADRON_COMPLETO.csv',encoding='ISO-8859-1')
miDistrito = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')

#variableas globales
varProvincia = "Cartago"
varCedula = 0000000000

def agregaColumnas():
#agrega columna provincia y usando los numeros de la cedula convierte ese numero en nombre de provincias
    miPadron['Provincia'] = miPadron['Cedula'].astype(str)
    miPadron['Provincia'] = miPadron['Provincia'].str[0:1]
    miPadron['Provincia'] = miPadron['Provincia'].replace({'1':'San Jose', '2':'Alajuela', '3':'Cartago','4':'Heredia','5':'Guanacaste','6':'Puntarenas','7':'Limon','8':'Nacionalizado','9':'CasosEspeciales'})
    miPadron['Count'] = 1
    miDistrito['Count'] = 1
    return miPadron, miDistrito

#Calcula votantes por provincia
def votantesPorProvincia():
    resultado = miPadron['Provincia'].value_counts().reset_index()
    resultado.columns = ['Provincia','Catidad de Votantes']
    return print(resultado)

#ListaVotantes por variable selecionada
def ListaVotantesPorProvincia():
    resultado = miPadron.loc[miPadron['Provincia'] == varProvincia]
    return print(resultado)

def ListaVotantePorCedula():
    filter1 =miPadron['Cedula'].isin([varCedula]) 
    resultado = miPadron.loc[miPadron['Cedula'] == varCedula]
    return print(resultado,filter1)

#Calcula vontantes por sexo
def votantesPorSexo():
    miPadron['Sexo'] = miPadron['Sexo'].astype(str)
    miPadron['Sexo'] = miPadron['Sexo'].replace({'1':'Masculino','2':'Fememino'})
    resultado = miPadron['Sexo'].value_counts().reset_index()
    resultado.columns = ['Sexo','Cantidad']
    return print(resultado)

#cuenta distritos electorales por provincia 
def DistritoPorProvincia():
    resultado = miDistrito['Provincia'].value_counts().reset_index()
    resultado.columns = ['Provincia','Cantidad Distritos']
    return print(resultado)

#cuenta distritos electorales por Canton
def DistritoPorCanton():
    resultado = miDistrito['Canton'].value_counts().reset_index()
    resultado.columns = ['Canto','Distritos Electorales']
    return print(resultado)

##def CantonPorProvincia():
 #   cantonProvincia = miDistrito.groupby('Provincia').agg({'Canton'})
     #resultado = miDistrito['Canton'].value_counts().reset_index()
#    return print(cantonProvincia)




agregaColumnas()
#ListaVotantesPorProvincia()
ListaVotantePorCedula()
#votantesPorProvincia()
#votantesPorSexo()
#DistritoPorProvincia()
#DistritoPorCanton()
#DistritoPorProvincia()
#CantonPorProvincia()






