def lista_atributos(**kwargs):
    
    lista_valor = []
    
    for valor in kwargs.values():
        lista_valor.append(valor)
        
    return lista_valor

print(lista_atributos(x=2,y=1,z=3))