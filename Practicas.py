# Práctica Crear Funciones 1

def saludar():
    print("Hola Mundo!")
    
saludar()

# Práctica Crear Funciones 2

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

bienvenida("Daniel")

# Práctica Crear Funciones 3

def cuadrado(un_numero):
    print(un_numero ** 2)
cuadrado(4)

# Práctica Return 1

def potencia(num1,num2):
    total = num1**num2
    return total
    
resultado = potencia(3,4)
print(resultado)

# Práctica Return 2

dolares = 50
def usd_a_eur(dolar):
    conversion = dolar * 0.9
    return conversion

result = usd_a_eur(dolares)
print(result)


# Práctica Return 3

palabra = "Funciones"
def invertir_palabra(palabra):
    return palabra[::-1].upper()

respuesta = invertir_palabra(palabra)
print(respuesta)


# Práctica Funciones Dinámicas 1

lista_numeros = [-1,502,755,600,33,61]

def todos_positivos(lista_numeros):
    
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
        
    return True

resultado = todos_positivos(lista_numeros)
print(resultado)


# Práctica Funciones Dinámicas 2

lista_numeros = [100,5000,874,147,-5,1001]

def suma_menores(lista_numeros):
    suma = 0
    
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma
            
        
solucion = suma_menores(lista_numeros)
print(solucion)

# Práctica sobre Interacción entre Funciones 1

import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
# Práctica sobre Argumentos Indefinidos (*args) 1

def suma_cuadrados(*args):
    
    total = 0
    
    for arg in args:
        total += arg**2
    return total

cuadrados = suma_cuadrados(1,2,3,4)
print(cuadrados)


# Práctica sobre Argumentos Indefinidos (*args) 2

def suma_absolutos(*args):
    
    suma = 0
    
    for arg in args:
        suma += abs(arg)
    return suma

absolutos = suma_absolutos(-1,5,7,8,12-10)

print(absolutos)







