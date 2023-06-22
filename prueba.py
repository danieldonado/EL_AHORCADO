def numeros_persona(nombre, *args):
    
    suma_numeros = sum(args)
    
    return f'{nombre}, la suma de tus números es {suma_numeros}' 

print(numeros_persona("Daniel",1,2,3))

    
