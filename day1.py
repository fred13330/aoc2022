with open("data.txt", "r") as fichier_donnees_initiales:
    donnees_initiales = [ligne.rstrip() for ligne in fichier_donnees_initiales.readlines()]

liste_somme_calories = []
total_calories = 0

for calorie in donnees_initiales:
    if calorie != "":
        total_calories += int(calorie)
    else:
        liste_somme_calories.append(total_calories)
        total_calories = 0
liste_somme_calories.append(total_calories)

print("Partie 1 :", max(liste_somme_calories))
print("Partie 2 :", sum(sorted(liste_somme_calories)[-3:]))