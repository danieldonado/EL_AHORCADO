lista_numeros = [1,2,3,4,5,6]

import random

def lanzar_moneda():
    
    resultado = random.choice(["Cara","Cruz"])
    return resultado

moneda = lanzar_moneda()

def probar_suerte(moneda,lista):
    
    if moneda == "Cara":
        print("La lista se autodestruirá")
        
        return []
    
    elif moneda == "Cruz":
        print("La lista fue salvada")
        
        return lista

resultado = probar_suerte(moneda,lista_numeros)

print(resultado)
        
    
    

    
    
    
    
    
    
    
    
    

    