# Program: cvičení počítání
import random

def soucet(a,b):
    """
    Funkce přijímá dva argumenty a vrací jejich součet.
    """
    result = a + b
    return result
levels = int(input("Kolik chcete hrát levelů?")) #opr: string převést na integer
correct = 0
for x in range(levels): 
    a = random.randint(1,999)
    b = random.randint(1,999)

    otazka = "Kolik je " + str(a) + "+" + str(b) + " ?"
    result = int(input(otazka))

    if result == soucet(a, b): 
        print("To sedí!")
        correct +=1 #opr: hodnotu je třeba přičíst k proměnné correct
    else: 
        print("Nene...")

print("Z", levels, "jste měla/měl", correct, "správně.")
if correct > 0: #opr: musíme zkontrolovat jestli je proměnná correct větší než nula = nulou nelze dělit
  print("Úspěšnost =", str(correct/levels*100), "%") #opr: prohodit correct a levels - odpvědi dělíme počtem levelů
else:
  print("Úspěšnost 0%")
