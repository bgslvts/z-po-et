# Program: Simulátor aktivismu
# Verze 0.0.1, level: policejní stanice

import random, time #opr: chybí čárka  

otazky = [
    "Jak se jmenujete?",
    "Kolik je vám let?",
    "Co na to, co děláte, říká vaše máma?",
    "Můžeme spolu mluvit jako lidé?",
    "Co jste tam dělali?",
    "Co studejete?",
    "Proč jste to dělali?",
    "Odkud jste?",
    "Není vám to blbý?",
    "Vy někde pracujete?",
    "Přijde vám to normální?",
    "Jaké důvody vás k tomu vedly?",
    "Podepíšete mi to tady?",
    "Přijeli jste tam vlakem?",
    "Znáte někoho dalšího tady?",
    "Nechcete jít už domů?",
]

neOdpovedi = [
    "Tímto mlčením ničemu nepomůžete. Ale dobrá, budu pokračovat.",
    "Tímhle tichem si na nás nepřijdete. Pokračujem!",
    "Takhle tu budeme sedět hodinu, místo toho, abysme šli za 10 minut domů. Tak už mějte rozum...",
    "Zřejmě mi nerozumíte. Zkusíme to ještě jednou.", #opr: chybí uvozovky
    "Kvůli hlásce by vás neubylo. Tak to zkuste..."
    "Nabídl bych vám kávu, ale když mi neřeknete ani ň... Ledažeby...",
    "Takových tu už bylo a všichni nakonec roztáli a začli mluvit. Tak co?",
    "Připadáte si díky tomu jako lepší člověk? Zkuste být normální člověk.", #opr: uvozovky
    "No a čemu tím prospějete? Ničemu. Tak zkuste prospět a něco mi řekněte, mě to jen zajímá jako lidsky..."
]

necoOdpovedi = ["Zajímavé, píšu si! A řekněte mi ještě...","Ale to je úžasné! Ještě se vás zeptám...","Díky za informaci. Můžete mi ještě říct..."]

random.shuffle(otazky) # zamichani otazek, at to neni porad stejne...

print("Dobrý den, zeptám se vás na pár otázek.")
print("Odpovězte mi zadáním textu a zmáčknutím enteru, můžete také mlčet - pak nic nezadávejte a jen dejte enter. Jdem na to!")

odpovedi = (0) #opr: záznam kladných odpovědí je třeba dát mimo smyčku

for otazka in otazky: #policajt postupne prochazi pres vsechny otazky
#opr: prohozeny "otazky" a "otazka"
     # pocitadlo kladnych odpovedi
    odpoved = input(otazka)

    if odpoved == "": #opr: chybí rovnítko
        random.shuffle(neOdpovedi) # zamichani seznamu neOdpovedi
        print(neOdpovedi[0])
        time.sleep(7) # menší pauzička, ať je to reálnější
    else: #opr: chybí dvojtečka
        random.shuffle(necoOdpovedi) # zamichani seznamu necoOdpovedi
        print(necoOdpovedi[0])
        odpovedi = odpovedi + 1 # za nenulovou odpoved zvedneme pocitadlo odpovedi
        time.sleep(7) # menší pauzička, ať je to reálnější
        #opr: sleep je funkce modulu time
    
    if odpovedi > 3: #opr: chybí dvojtečka
        print("To nám bude stačit, hehehe, můžete jít!")
        exit() # ukoncime program

print("Tak teda díky za nic. Můžete jít, ale my se vám ještě ozvem, na to si vemte jed. Dostanem vás. Všechny.")
