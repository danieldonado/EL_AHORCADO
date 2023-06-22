precios_cafe = [('capuccino', 2.7), ('expresso', 1.2), ('mocca', 1.9)]

precios_cafe.append(('Tinto', 5.7))

def cafe_mas_caro(lista_precios):
    
    precio_mayor = 0
    cafe_mas_caro = ''
    
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    
    return (cafe_mas_caro,precio_mayor)

cafe,precio = cafe_mas_caro(precios_cafe)

print(f'El cafe mas caro es {cafe} es cuyo precio es {precio}')
