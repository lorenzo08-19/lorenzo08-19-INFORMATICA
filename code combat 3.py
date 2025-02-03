import random

names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
surnames = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]

name1 = random.choice(names)
surname1 = random.choice(surnames)
name2 = random.choice(names)
surname2 = random.choice(surnames)

def get_full_name(name, surname):
    return f"{name} {surname}"

player1_name = get_full_name(name1, surname1)
player2_name = get_full_name(name2, surname2)
print(f"Giocatore 1: {player1_name}")
print(f"Giocatore 2: {player2_name}")

def roll_dice(player):
    if player == 1:
        # Giocatore 1: 6d6dl1dh1 (6 dadi da 6 facce, lancia il più basso e poi il più alto)
        rolls = [random.randint(1, 6) for _ in range(6)]
        rolls.sort()
        rolls = rolls[1:-1]  # Rimuove il primo e l'ultimo
    elif player == 2:
        # Giocatore 2: 4d12dl1dh1 (4 dadi da 12 facce, lancia il più basso e poi il più alto)
        rolls = [random.randint(1, 12) for _ in range(4)]
        rolls.sort()
        rolls = rolls[1:-1]  # Rimuove il primo e l'ultimo
    return rolls

rolls_player1 = roll_dice(1)
rolls_player2 = roll_dice(2)

damage_player1 = sum(rolls_player1)
damage_player2 = sum(rolls_player2)

if damage_player1 > 0:
    print(f"{player1_name} ha inflitto {damage_player1} danni.")
else:
    print(f"{player1_name} ha evitato l'attacco.")

if damage_player2 > 0:
    print(f"{player2_name} ha inflitto {damage_player2} danni.")
else:
    print(f"{player2_name} ha evitato l'attacco.")



















