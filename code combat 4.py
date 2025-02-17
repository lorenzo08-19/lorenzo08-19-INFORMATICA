import random



def random_range(min_val, max_val):
    return random.randint(min_val, max_val)


def roll_attack(dice):
    return sum(random_range(1, dice) for _ in range(dice))



def create_character(role):
    if role == 'guerriero':
        return {
            'classe': 'Guerriero',
            'vita': random_range(100, 120),
            'energia': random_range(8, 10),
            'difesa': random_range(4, 8),
            'attacco': roll_attack(6),
            'abilità': roll_attack(6)
        }
    elif role == 'mago':
        return {
            'classe': 'Mago',
            'vita': random_range(70, 90),
            'energia': random_range(14, 18),
            'difesa': random_range(3, 5),
            'attacco': roll_attack(20),
            'abilità': roll_attack(8)
        }
    elif role == 'ladro':
        return {
            'classe': 'Ladro',
            'vita': random_range(80, 100),
            'energia': random_range(10, 12),
            'difesa': random_range(3, 5),
            'attacco': sum(random_range(1, 4) for _ in range(3)),
            'abilità': roll_attack(4)
        }
    elif role == 'chierico':
        return {
            'classe': 'Chierico',
            'vita': random_range(80, 100),
            'energia': random_range(10, 12),
            'difesa': random_range(4, 6),
            'attacco': roll_attack(12),
            'abilità': roll_attack(6)
        }


def berserk(character):
    roll = random_range(1, 6)
    if roll in [5, 6]:
        return "Guerriero attacca due volte."
    elif roll in [3, 4]:
        character['vita'] -= int(character['vita'] * 0.2)
        return "Guerriero attacca e perde il 20% della vita."
    else:
        character['vita'] -= int(character['vita'] * 0.2)
        return "Guerriero perde il 20% della vita."



def concentrazione_assoluta(character):
    roll = random_range(1, 6)
    if roll in [5, 6]:
        character['attacco'] += random_range(1, 4)
        return f"Mago ha migliorato il suo attacco permanentemente."
    return "Mago non attiva l'abilità."



def pugnali_acidi(opponent_party):
    roll = sum(random_range(1, 4) for _ in range(2))
    if roll in [7, 8]:
        for opponent in opponent_party:
            opponent['difesa'] -= int(opponent['difesa'] * 0.25)
        return "Ladro riduce la difesa degli avversari."
    return "Ladro non attiva l'abilità."

def favore_degli_dei(character, ally_party):
    roll = sum(random_range(1, 6) for _ in range(2))
    weakest_ally = min(ally_party, key=lambda x: x['vita'])
    weakest_ally['vita'] += roll
    return f"Chierico cura {weakest_ally['classe']} di {roll} punti vita."



def determine_attack_order(attacker, defender):
    if attacker['classe'] == 'Guerriero':
        target = max(defender, key=lambda x: x['vita'])
    elif attacker['classe'] == 'Mago':
        middle = len(defender) // 2
        if len(defender) % 2 == 0:
            target = defender[middle] if random.choice([True, False]) else defender[middle - 1]
        else:
            target = defender[middle]
    elif attacker['classe'] == 'Ladro':
        target = min(defender, key=lambda x: x['vita'])
    elif attacker['classe'] == 'Chierico':
        target = random.choice([defender[0], defender[-1]])
    return target



def attack(attacker, defender):
    if attacker['energia'] >= 2:
        attacker['energia'] -= 2
        target = determine_attack_order(attacker, defender)
        damage = attacker['attacco'] - target['difesa']
        target['vita'] -= max(damage, 0)  # I danni non possono essere negativi
        print(f"{attacker['classe']} attacca {target['classe']} infliggendo {max(damage, 0)} danni.")

        
        if attacker['classe'] == 'Guerriero':
            print(berserk(attacker))
        elif attacker['classe'] == 'Mago':
            print(concentrazione_assoluta(attacker))
        elif attacker['classe'] == 'Ladro':
            print(pugnali_acidi(defender))
        elif attacker['classe'] == 'Chierico':
            print(favore_degli_dei(attacker, defender))


def check_victory(party):
    return all(character['vita'] <= 0 for character in party)



def create_team():
    roles = ['guerriero', 'mago', 'ladro', 'chierico']
    team = [create_character(role) for role in roles]
    return team



def battle():
    team1 = create_team()
    team2 = create_team()

    turn = 0
    while True:
        print(f"\nTurno {turn + 1}")
        print("Team 1:", [(char['classe'], char['vita']) for char in team1])
        print("Team 2:", [(char['classe'], char['vita']) for char in team2])

        for attacker, defender in zip(team1, team2):
            attack(attacker, team2)

        for attacker, defender in zip(team2, team1):
            attack(attacker, team1)

        if check_victory(team1):
            print("Team 2 vince!")
            break
        elif check_victory(team2):
            print("Team 1 vince!")
            break

        turn += 1


battle()




















