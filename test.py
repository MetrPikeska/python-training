import math

stanice_data = [
    {"nazev" : "Ostrava", "souradnice" : (49.8209, 18.2625), "teplota" : [19]},
    {"nazev" : "Brno", "souradnice" : (49.1951, 16.6068), "teplota" : [15]},
    {"nazev" : "Praha", "souradnice" : (50.0755, 14.4378), "teplota" : [13]},
    {"nazev" : "Plzen", "souradnice" : (49.7475, 13.3776), "teplota" : [10]},
    {"nazev" : "Liberec", "souradnice" : (50.7671, 15.0562), "teplota" : [8]},
    {"nazev" : "Olomouc", "souradnice" : (49.5938, 17.2509), "teplota" : [12]},
    { "nazev" : "Hradec Kralove", "souradnice" : (50.2092, 15.8328), "teplota" : [9]}
                                                                        
]


prumerne_hodnoty = []
nadprumerne_hodnoty = []
prumerne_hodnoty = []


def vypocitej_prumer(hodnoty):
    if len(hodnoty) == 0:
        return 0
    return sum(hodnoty) / len(hodnoty)

for stanice in stanice_data:
    prumerne_hodnoty.append(vypocitej_prumer(stanice["hodnoty"])) 
    print(f"Stanice {stanice['nazev']} ma prumernou hodnotu: {prumerne_hodnoty[-1]}")
    print("Vsechny prumerne hodnoty:", prumerne_hodnoty)
    if prumerne_hodnoty[-1] > 15000:
        nadprumerne_hodnoty.append(stanice["nazev"])
    print("Stanice s nadprumernou hodnotou:", nadprumerne_hodnoty)














# northest_point = max(stanice_data, key=lambda x: x["souradnice"][0])
# print(f"Nejsevernejsi stanice je {northest_point['nazev']} na souradnicich {northest_point['souradnice']}")


# euklidovska_vzdalenost = math.sqrt((northest_point["souradnice"][0] - 49.1951) ** 2 + (northest_point["souradnice"][1] - 16.6068) ** 2)
# print(f"Euklidovska vzdalenost mezi {northest_point['nazev']} a Brnem je {euklidovska_vzdalenost:.2f} stupnu.")



# # Chci jen seznam názvů
# nazvy = [stanice["nazev"] for stanice in stanice_data]
# print(nazvy)
# # Výsledek: ['Ostrava', 'Brno', 'Praha', ...]

# # Chci jen souřadnice (jako seznam tuplů)
# souradnice = [stanice["souradnice"] for stanice in stanice_data]
# print(souradnice)