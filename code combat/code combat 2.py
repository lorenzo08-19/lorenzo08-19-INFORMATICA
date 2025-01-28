player_1_health = 100
player_2_health = 90
import random
valore_scudo = random.randit(5, 10)
print("valore dello scudo:",valore_scudo
dadig1 = (random.randit(1, 6) for i in range(4)
danni_g1 = sum(dadi_g1)
print("giocatore 1 lancia 4d6: , dadi_g1)
print("danni inflitti dal giocatore 1:" , danni_g1)
dadi_g2= (random.randint(1,12) for i in range(2)
danni_g2 = sum(dadi_g2)
print("giocatore 2 lancia 2d12:", dadi_g2)
print("danni inflitti dal giocatore2:" , danni_g2)
vita_g1 = 100
vita_g2 = 90
while vita_g1 0 and vita_g2 0:
danni_g1 = sum(random.randint(1 ,6)
for _ in range(4))
print("giocatore 1 infligge" , danni_g1 "dadi2 )
vita_g2 = danni_g1
print("vita rimanente del giocatore 2:" , vita_g2
if vita_g2 =0:
print("giocatore 1 ha vinto")
break
danni_g2 = sum(random.randit(1,12) for _ in range(2)
print("giocatore2 infligge" , danni_g2: "danni2
 vita_g1 = danni_g2print("vita rimanente del giocatore 1." , vita_g1
 if vita_g1 =0:
  print("giocatore 2 ha vinto")
 break                       )    
