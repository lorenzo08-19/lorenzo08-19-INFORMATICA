import random

class Weapon:
    
    def __init__(self, name: str, min_damage: int, max_damage: int, weapon_type: str):
        if min_damage < 1 or max_damage < min_damage:
            raise ValueError("I valori di danno non sono validi.")
        if weapon_type not in ["melee", "ranged"]:
            raise ValueError("Il tipo di arma deve essere 'melee' o 'ranged'.")
            
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.weapon_type = weapon_type

    def get_damage(self) -> int:
        
        return random.randint(self.min_damage, self.max_damage)

    def __str__(self) -> str:
      
        return f"{self.name} (Danno: {self.min_damage}-{self.max_damage}, Tipo: {self.weapon_type})"

class Player:
    
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        if max_health < 1:
            raise ValueError("I punti vita massimi devono essere almeno 1.")
        if not (1 <= strength <= 20) or not (1 <= dexterity <= 20):
            raise ValueError("Forza e destrezza devono essere tra 1 e 20.")
            
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.dexterity = dexterity
        self.weapon = None  # Nessuna arma equipaggiata all'inizio

    def equip(self, weapon: Weapon):
        """Assegna un'arma al giocatore."""
        self.weapon = weapon
        print(f"{self.name} ha equipaggiato: {self.weapon.name}.")

    def modifier(self, value: int) -> int:
        
        return (value - 10) // 2

    def is_alive(self) -> bool:
        
        return self.health > 0

    def take_damage(self, damage: int) -> int:
        
        effective_damage = min(damage, self.health)
        self.health -= effective_damage
        if self.health < 0:
            self.health = 0
        return effective_damage

    def attack(self, enemy: "Player") -> int:
        
        base_damage = 1
        modifier_value = 0

        if self.weapon:
            base_damage = self.weapon.get_damage()
            if self.weapon.weapon_type == "melee":
                modifier_value = self.modifier(self.strength)
            elif self.weapon.weapon_type == "ranged":
                modifier_value = self.modifier(self.dexterity)
        
        total_damage = max(0, base_damage + modifier_value)
        
        effective_damage = enemy.take_damage(total_damage)
        
        print(f"{self.name} attacca {enemy.name} con un danno di {total_damage} ({effective_damage} effettivi).")
        return effective_damage

    def __str__(self) -> str:
        
        return f"{self.name} ({self.health}/{self.max_health} PV)"



if __name__ == "__main__":
    
    print("--- Inizio del gioco Object Code Combat! ---")

    
    p1_name = "Recluta T-800"
    p2_name = "Soldatessa Ripley"
    
    p1_health = random.randint(50, 100)
    p2_health = random.randint(50, 100)
    
    p1_str = random.randint(8, 18)
    p1_dex = random.randint(8, 18)
    
    p2_str = random.randint(8, 18)
    p2_dex = random.randint(8, 18)

    player1 = Player(p1_name, p1_health, p1_str, p1_dex)
    player2 = Player(p2_name, p2_health, p2_str, p2_dex)

    
    if player1.strength >= player1.dexterity:
        weapon1 = Weapon("Spada a due mani", 10, 15, "melee")
    else:
        weapon1 = Weapon("Arco lungo", 8, 12, "ranged")

    if player2.strength >= player2.dexterity:
        weapon2 = Weapon("Mazza ferrata", 12, 16, "melee")
    else:
        weapon2 = Weapon("Balestra pesante", 9, 14, "ranged")

    player1.equip(weapon1)
    player2.equip(weapon2)

    print("\n--- STATISTICHE INIZIALI ---")
    print(f"Giocatore 1: {player1.name}, PV: {player1.health}, Forza: {player1.strength}, Destrezza: {player1.dexterity}")
    print(f"Giocatore 2: {player2.name}, PV: {player2.health}, Forza: {player2.strength}, Destrezza: {player2.dexterity}")
    
    
    print("\n--- INIZIO DEL COMBATTIMENTO ---")
    turn = 1
    while player1.is_alive() and player2.is_alive():
        print(f"\n--- Turno {turn} ---")

        
        if player1.is_alive():
            player1.attack(player2)
            print(f"Stato: {player1} vs {player2}")
        
      
        if player2.is_alive():
            player2.attack(player1)
            print(f"Stato: {player1} vs {player2}")
            
        turn += 1

    print("\n--- FINE DEL COMBATTIMENTO ---")
    if not player1.is_alive() and not player2.is_alive():
        print("Entrambi i giocatori sono caduti. È un pareggio!")
    elif player1.is_alive():
        print(f"Il vincitore è {player1.name}!")
    else:
        print(f"Il vincitore è {player2.name}!")
































