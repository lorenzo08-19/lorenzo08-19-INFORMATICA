def vigenere_cifrare(testo, chiave):
    testo = testo.upper()
    chiave = chiave.upper()
    testo_cifrato = []
    j = 0
    
    for i in range(len(testo)):
        if testo[i].isalpha():
            shift = ord(chiave[j % len(chiave)]) - ord('A')
            cifrato = chr(((ord(testo[i]) - ord('A') + shift) % 26) + ord('A'))
            testo_cifrato.append(cifrato)
            j += 1
        else:
            testo_cifrato.append(testo[i])
    
    return ''.join(testo_cifrato)

def vigenere_decifrare(testo_cifrato, chiave):
    testo_cifrato = testo_cifrato.upper()
    chiave = chiave.upper()
    testo_decifrato = []
    j = 0
    
    for i in range(len(testo_cifrato)):
        if testo_cifrato[i].isalpha():
            shift = ord(chiave[j % len(chiave)]) - ord('A')
            decifrato = chr(((ord(testo_cifrato[i]) - ord('A') - shift) % 26) + ord('A'))
            testo_decifrato.append(decifrato)
            j += 1
        else:
            testo_decifrato.append(testo_cifrato[i])
    
    return ''.join(testo_decifrato)

testo = "Questo è un messaggio segreto!"
chiave = "CHIAVE"
testo_cifrato = vigenere_cifrare(testo, chiave)
print(f"Testo cifrato: {testo_cifrato}")

testo_decifrato = vigenere_decifrare(testo_cifrato, chiave)
print(f"Testo decifrato: {testo_decifrato}")



















