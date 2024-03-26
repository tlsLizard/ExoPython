tableau_todo = []

while True:
    valeur = input("Entrez ce que vous voulez ajouter : ")
    if not valeur:
        print("La valeur est vide. Merci d'entrer une chaîne de caractères.")
    else:
        tableau_todo.append(valeur)
        print(f"Élément ajouté : {valeur}")

    choix = input("Voulez-vous ajouter, supprimer ou afficher un élément ? (A/S/V/N) ").lower()
    if choix == "n":
        break
    elif choix == "s":
        try:
            index = int(input("Entrez le numéro de l'élément à supprimer : "))
            if 1 <= index <= len(tableau_todo):
                element_supprime = tableau_todo.pop(index - 1)
                print(f"Élément supprimé : {element_supprime}")
            else:
                print("Numéro invalide. Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")
    elif choix == "a":
        continue
    elif choix == "v":
        print("Voici vos valeurs actuelles dans votre liste TODO :")
        for i, element in enumerate(tableau_todo, start=1):
            print(f"{i}. {element}")
    else:
        print("Choix invalide. Veuillez entrer 'A', 'S', 'V' ou 'N'.")

print("Voici vos valeurs ajoutées dans votre liste TODO :")
for i, element in enumerate(tableau_todo, start=1):
    print(f"{i}. {element}")