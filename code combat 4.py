import random

def crea_personaggio(classe):
    if classe == 'guerriero':
        vita = random.randint(100, 120)
        energia = random.randint(8, 10)
        difesa = random.randint(4, 8)
        attacco = sum(random.randint(1, 6) for _ in range(2))  # 2d6
        abilita = 6  # 1d6
    elif classe == 'mago':
        vita = random.randint(70, 90)
        energia = random.randint(14, 18)
        difesa = random.randint(3, 5)
        attacco = random.randint(1, 20)  # 1d20
        abilita = random.randint(1, 8)  # 1d8
    elif classe == 'ladro':
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(3, 5)
        attacco = sum(random.randint(1, 4) for _ in range(3))  # 3d4
        abilita = random.randint(1, 4)  # 1d4
    elif classe == 'chierico':
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(4, 6)
        attacco = random.randint(1, 12)  # 1d12
        abilita = random.randint(1, 6)  # 1d6
    return {
        'classe': classe,
        'vita': vita,
        'energia': energia,
        'difesa': difesa,
        'attacco': attacco,
        'abilita': abilita,
        'stato': 'attivo'  
    }

def attacco(personaggio, nemico):
    if personaggio['energia'] >= 2:
        danno = personaggio['attacco'] - nemico['difesa']
        danno = max(danno, 0)  
        nemico['vita'] -= danno
        personaggio['energia'] -= 2  
        print(f"{personaggio['classe']} attacca {nemico['classe']} causando {danno} danni!")
    else:
        print(f"{personaggio['classe']} non ha abbastanza energia per attaccare e riposa.")
        personaggio['energia'] = 12  


def abilita_speciale(personaggio):
    if personaggio['classe'] == 'guerriero':
        
        risultato = random.randint(1, 6)
        print(f"Guerriero lancia 1d6 e ottiene: {risultato}")
        if risultato >= 5:
            print("Guerriero effettua un altro attacco!")
        elif risultato >= 3:
            perdita_vita = personaggio['vita'] // 5
            personaggio['vita'] -= perdita_vita
            print(f"Guerriero perde {perdita_vita} punti vita.")
        else:
            perdita_vita = personaggio['vita'] // 5
            personaggio['vita'] -= perdita_vita
            print(f"Guerriero perde {perdita_vita} punti vita.")
    elif personaggio['classe'] == 'mago':
        
        risultato = random.randint(1, 6)
        print(f"Mago lancia 1d6 e ottiene: {risultato}")
        if risultato >= 5:
            incremento = random.randint(1, 4)
            personaggio['attacco'] += incremento
            print(f"Mago aumenta il suo attacco di {incremento}.")
    elif personaggio['classe'] == 'ladro':
        
        risultato = sum(random.randint(1, 4) for _ in range(2))  
        print(f"Ladro lancia 2d4 e ottiene: {risultato}")
        if risultato >= 7:
            print("Ladro riduce la difesa degli avversari del 25%.")
            
            for avversario in nemici:
                avversario['difesa'] = int(avversario['difesa'] * 0.75)
    elif personaggio['classe'] == 'chierico':
        
        risultato = sum(random.randint(1, 6) for _ in range(2))  # 2d6
        print(f"Chierico lancia 2d6 e ottiene: {risultato}")
        
        piu_debole = min(personaggi, key=lambda x: x['vita'])
        piu_debole['vita'] += risultato
        print(f"Chierico cura {piu_debole['classe']} di {risultato} punti vita.")

def turno_combattimento(personaggi_1, personaggi_2):
    for p1, p2 in zip(personaggi_1, personaggi_2):
        if p1['stato'] == 'attivo' and p2['stato'] == 'attivo':
            attacco(p1, p2)
            abilita_speciale(p1)
            if p2['vita'] <= 0:
                p2['stato'] = 'eliminato'
                print(f"{p2['classe']} è stato eliminato!")

            if p2['stato'] == 'attivo':
                attacco(p2, p1)
                abilita_speciale(p2)
                if p1['vita'] <= 0:
                    p1['stato'] = 'eliminato'
                    print(f"{p1['classe']} è stato eliminato!")

classi = ['guerriero', 'mago', 'ladro', 'chierico']
personaggi_1 = [crea_personaggio(classe) for classe in classi]
personaggi_2 = [crea_personaggio(classe) for classe in classi]


turno = 1
while any(p['stato'] == 'attivo' for p in personaggi_1) and any(p['stato'] == 'attivo' for p in personaggi_2):
    print(f"\n--- Turno {turno} ---")
    turno_combattimento(personaggi_1, personaggi_2)
    turno += 1

if all(p['stato'] == 'eliminato' for p in personaggi_1):
    print("\nGiocatori 2 vincono!")
elif all(p['stato'] == 'eliminato' for p in personaggi_2):
    print("\nGiocatori 1 vincono!")




















