import random

def genera_griglia(dimensione, numero_mine):
    griglia = [['' for _ in range(dimensione)] for _ in range(dimensione)]
    posiziona_mine(griglia, numero_mine)
    calcola_numeri(griglia)
    return griglia

def posiziona_mine(griglia, numero_mine):
    dimensione = len(griglia)
    mine_posizionate = 0
    while mine_posizionate < numero_mine:
        riga = random.randint(0, dimensione - 1)
        colonna = random.randint(0, dimensione - 1)
        if griglia[riga][colonna] != '':
            griglia[riga][colonna] = ''
            mine_posizionate += 1

def calcola_numeri(griglia):
    dimensione = len(griglia)
    for r in range(dimensione):
        for c in range(dimensione):
            if griglia[r][c] == '':
                continue
            conta = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nr, nc = r + i, c + j
                    if 0 <= nr < dimensione and 0 <= nc < dimensione and griglia[nr][nc] == '':
                        conta += 1
            griglia[r][c] = conta if conta > 0 else ' '

def rivela_cella(griglia, riga, colonna, celle_rivelate):
    if (riga, colonna) in celle_rivelate:
        return False
    celle_rivelate.add((riga, colonna))
    if griglia[riga][colonna] == '':
        return True
    if griglia[riga][colonna] == ' ':
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                nr, nc = riga + i, colonna + j
                if 0 <= nr < len(griglia) and 0 <= nc < len(griglia[0]):
                    if (nr, nc) not in celle_rivelate:
                        rivela_cella(griglia, nr, nc, celle_rivelate)
    return False

def visualizza_griglia(griglia, celle_rivelate):
    dimensione = len(griglia)
    print("   " + " ".join(f"{i:2}" for i in range(dimensione)))
    print("  +" + "--" * dimensione + "+")
    for r in range(dimensione):
        riga_vis = f"{r:2}|"
        for c in range(dimensione):
            if (r, c) in celle_rivelate:
                riga_vis += f"{griglia[r][c]:2}"
            else:
                riga_vis += " "
        riga_vis += " |"
        print(riga_vis)
    print("  +" + "--" * dimensione + "+")

def gioco_finito(griglia, celle_rivelate):
    for r in range(len(griglia)):
        for c in range(len(griglia)):
            if griglia[r][c] != '' and (r, c) not in celle_rivelate:
                return False
    return True

def main():
    N = int(input("Inserisci la dimensione della griglia (es. 10): "))
    M = int(N * N * 0.15)
    print(f"Ci saranno {M} mine.")
    griglia = genera_griglia(N, M)
    celle_rivelate = set()

    while True:
        visualizza_griglia(griglia, celle_rivelate)
        try:
            r = int(input("Inserisci la riga: "))
            c = int(input("Inserisci la colonna: "))
            if not (0 <= r < N and 0 <= c < N):
                print("Coordinate fuori dai limiti!")
                continue
        except ValueError:
            print("Input non valido. Inserire numeri interi.")
            continue

        if rivela_cella(griglia, r, c, celle_rivelate):
            visualizza_griglia(griglia, {(r, c) for r in range(N) for c in range(N)})
            print(" BOOM! Hai colpito una mina. Fine del gioco.")
            break

        if gioco_finito(griglia, celle_rivelate):
            visualizza_griglia(griglia, celle_rivelate)
            print(" Complimenti! Hai vinto!")
            break

if __name__ == "__main__":
    main()



















