
#creo la plantilla de la matriz con **

def matriz_diagonal(matriz ):
    m = []
    num = len(matriz)
    for i in range(num):
        m.append(['**'] * num)
        #print(m[i])

    #ordenamos la matriz de menor a mayor
    order = sorted(matriz, key = lambda i: 0 if i == 0 else -1 / i)

    #agregamos los valores de la matriz a la plantilla en su diagonal
    n = 0
    for j in m:
        m[n][n] = order[n]
        print(m[n])
        n += 1

    return ''


print(matriz_diagonal([0,-2, -8, -14, -45, 3, 45, 52]))
        
