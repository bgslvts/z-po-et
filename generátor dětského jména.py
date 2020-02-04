import random #importujeme modul random

jmenaKluk = ["Jakub",
"Jan",
"Adam",
"Matyáš",
"Tomáš",
"Vojtěch",
"Matěj",
"Filip",
"Ondřej",
"Dominik",
"Daniel",
"Martin",
"David",
"Lukáš",
"Marek",
"Václav",
"Antonín",
"Jiří",
"Kryštof",
"Tobiáš"] #databáze 20 nejoblíběnějších klučičích jmen za rok 2019

jmenaHolka = ["Eliška",
"Anna",
"Sofie",
"Ema",
"Tereza",
"Karolína",
"Adéla",
"Viktorie",
"Natálie",
"Kristýna",
"Emma",
"Julie",
"Amalie",
"Nela",
"Anežka",
"Marie",
"Klára",
"Laura",
"Barbora",
"Kateřina"] #databáze 20 holčičích jmen za rok 2019

print("Dobrý den, asi budete mít dítě! Nevíte jak ho pojmenovat? Poradíme vám! Bude to kluk nebo holka?") #dotaz
pohlavi = input() #odpověď
pohlavi = pohlavi.lower()
if pohlavi == "kluk": #odpověď pokud uživatel bude mít kluka
    random.shuffle(jmenaKluk)
    print("Můžete svého syna pojemnovat třeba", jmenaKluk[0])

elif pohlavi == "holka": #odpověď pokud uživatel bude mít holku
    random.shuffle(jmenaHolka)
    print("Můžete svojí dceru pojmenovat třeba", jmenaHolka[0])
else:
  print(pohlavi + " není pohlaví. Pohlaví jsou přece jen 2.") #odpověď pokud uživatel napíše něco jiného než holka/kluk, osobně si nemyslím že jsou jen 2 pohlaví je to vtípek
