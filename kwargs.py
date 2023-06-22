"""def suma(**kwargs):
    
    total = 0
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
        
print(suma(x=3, y=2, z=2))"""


def prueba(num1, num2, *args, **kwargs):
    
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    
    for arg in args:
        print(f'arg = {arg}')
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [10,5,10]
kwargs = {'x':5,'y':2,'z':3}

prueba(2,5, *args, **kwargs) 