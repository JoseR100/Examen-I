import pandas as pd


#Carga el padron nacional en una varialble llamada miPadronm se utiliza el ISO para poder utilizar los difentes unicodes.
miPadron = pd.read_csv('./Data/PADRON_COMPLETO.csv',encoding='ISO-8859-1')



print(miPadron.head(5))
print (miPadron['Cedula'])



