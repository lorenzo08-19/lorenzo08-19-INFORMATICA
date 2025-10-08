def calcola_sconto_negozio1(spesa):
    if spesa > 500:
        sconto = spesa * 0.20
    else:
        sconto = spesa * 0.10
    totale = spesa - sconto
    return sconto, totale

def calcola_sconto_negozio2(spesa):
    if spesa <= 300:
        sconto = spesa * 0.10
    else:
        sconto = 300 * 0.10 + (spesa - 300) * 0.20
    totale = spesa - sconto
    return sconto, totale

def confronta_negozi(spesa):
    sconto1, totale1 = calcola_sconto_negozio1(spesa)
    sconto2, totale2 = calcola_sconto_negozio2(spesa)

    print(f"\nRisultati per una spesa di €{spesa:.2f}:")
    print("\n Negozio 1:")
    print(f"Sconto applicato: €{sconto1:.2f}")
    print(f"Importo finale: €{totale1:.2f}")

    print("\n Negozio 2:")
    print(f"Sconto applicato: €{sconto2:.2f}")
    print(f"Importo finale: €{totale2:.2f}")

    print("\nConfronto:")
    if totale1 < totale2:
        print(" Conviene acquistare nel *Negozio 1*.")
    elif totale2 < totale1:
        print(" Conviene acquistare nel *Negozio 2*.")
    else:
        print(" È indifferente: il costo finale è lo stesso in entrambi i negozi.")


try:
    spesa_input = input("Inserisci l'importo della spesa (€): ").replace(",", ".")
    spesa = float(spesa_input)

    if spesa <= 0:
        print(" Errore: l'importo della spesa deve essere positivo e maggiore di zero.")
    else:
        confronta_negozi(spesa)

except ValueError:
    print("Errore: inserisci un numero valido per la spesa.")
   Risultati per una spesa di €550.00:

 Negozio 1:
Sconto applicato: €110.00
Importo finale: €440.00

 Negozio 2:
Sconto applicato: €85.00
Importo finale: €465.00

Confronto:
 Conviene acquistare nel *Negozio 1*.

