
def calcular_mediana(tempos):
    if len(tempos) == 0:
        print("Precisa adicionar um tempo")
        return None
    
    tempos.sort()
    meio = len(tempos) // 2

    if len(tempos) % 2 == 0:
        return (tempos[meio - 1] + tempos[meio]) / 2
    else:
        return tempos[meio]


tempos = []
resultado = calcular_mediana(tempos)
print(resultado)
