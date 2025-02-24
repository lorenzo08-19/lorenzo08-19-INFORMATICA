import random


def genera_matrice(n):
    
    numeri = random.sample(range(1, n * n + 1), n * n)  
    matrice = [numeri[i:i + n] for i in range(0, len(numeri), n)]  
    return matrice


def calcola_somma_riga(matrice):
    
    return sum(matrice[0])


def verifica_quadrato_magico(matrice):
    n = len(matrice)
    costante_magica = calcola_somma_riga(matrice)

    
    for riga in matrice:
        if sum(riga) != costante_magica:
            return False

    
    for col in range(n):
        if sum(matrice[riga][col] for riga in range(n)) != costante_magica:
            return False

    
    if sum(matrice[i][i] for i in range(n)) != costante_magica:
        return False

    
    if sum(matrice[i][n - i - 1] for i in range(n)) != costante_magica:
        return False

    return True


def stampa_matrice(matrice):
    for riga in matrice:
        print(' '.join(map(str, riga)))


def genera_e_verifica_quadrato_magico():
    for ordine in range(3, 11):
        while True:
            matrice = genera_matrice(ordine)
            if verifica_quadrato_magico(matrice):
                print(f"\nQuadrato Magico di ordine {ordine}:")
                stampa_matrice(matrice)
                costante = calcola_somma_riga(matrice)
                print(f"Costante di magia: {costante}")
                break



genera_e_verifica_quadrato_magico()
