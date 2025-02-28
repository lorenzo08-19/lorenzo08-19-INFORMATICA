import random

print('\n#1: CREAZIONE DEL PERSONAGGIO\n')

nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]


def create_character():
    name = random.choice(nomi)
    character_class = input("Scegli una classe (Guerriero, Mago, Chierico, Ladro): ")
    
    
    character = {
        "nome": name,
        "classe": character_class
    }
    
    
    character["punti_vita"] = random.randint(80, 100)
    character["armatura"] = random.randint(5, 10)
    character["dado_attacco"] = input("Scegli il tipo di dado per l'attacco (es. 1d6): ")
    
    
    oggetti = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
    armi = {
        "fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
        "magico": ["Bastone magico", "Bacchetta"]
    }
    
    
    zaino = {
        "monete": random.randint(20, 50),
        "oggetti": random.sample(oggetti, 2),
        "arma": random.choice(armi["fisico"] + armi["magico"])
    }
    
    character["zaino"] = zaino
    
    return character

print('\n#2: STAMPA DEL PERSONAGGIO\n')

def print_character(character):
    for key, value in character.items():
        if isinstance(value, dict):
            print(f"{key.capitalize()}:")
            for subkey, subvalue in value.items():
                print(f"  {subkey.capitalize()}: {subvalue}")
        else:
            print(f"{key.capitalize()}: {value}")


def create_party():
    party_size = int(input("Quanti personaggi vuoi nel tuo party? "))
    party = []
    for _ in range(party_size):
        party.append(create_character())
    return party


def print_party(party):
    for i, character in enumerate(party, 1):
        print(f"\nPersonaggio {i}:")
        print_character(character)

print('\nFUNZIONE PRINCIPALE\n')


def main():
    party = create_party()
    print_party(party)
    
main()


















