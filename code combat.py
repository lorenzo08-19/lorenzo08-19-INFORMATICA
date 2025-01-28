import random


hp = 30  
turni = 0  


while hp > 0:
    
    danno = random.randint(1, 6)
    
    
    hp -= danno
    
    
    turni += 1
    
    
    print(f"Turno {turni}: Il personaggio subisce {danno} danni. Punti vita rimanenti: {hp}")
    

print(f"\nIl gioco è terminato dopo {turni} turni.")


















