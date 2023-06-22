def suma(*args):
    # return sum(args) con este codigo utilizando la funcion sum puedo sumar todos los argumentos 
    total = 0
    
    for arg in args:
        total += arg
        
    return total

print(suma(1,2,3))