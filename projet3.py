nb_de_vies = 7

mot_mystère = "bougie"
print("Bienvenie dans le jeu du pendu !")
mot_deviné = ["_"] * len(mot_mystère)
while nb_de_vies > 0 and mot_mystère != mot_deviné:

print(f"Le mot à deviner a {len(mot_mystère)} lettres.")
print("Vous avez 7 vies pour deviner le mot.")
lettre = input("Veuillez entrer une lettre : ").lower()
if lettre in mot_mystère:
    print("Bravo ! La lettre est dans le mot.")
else:
    print("Désolé, la lettre n'est pas dans le mot.")
    nb_de_vies -= 1
    print(f"Vous avez {nb_de_vies} vies restantes.")
for i in range(len(mot_mystère)):
    if mot_mystère[i] == lettre:
        mot_deviné = mot_deviné[:i] + lettre + mot_deviné[i+1:]
        print(lettre, end=" ")
    else:
        print("_", end=" ")
