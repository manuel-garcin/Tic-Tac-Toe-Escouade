import random

plateau = [" " for _ in range(9)]

def grille():
    print(' ' + plateau[0] + ' | ' + plateau[1] + ' | ' + plateau[2])
    print('---|---|---')
    print(' ' + plateau[3] + ' | ' + plateau[4] + ' | ' + plateau[5])
    print('---|---|---')
    print(' ' + plateau[6] + ' | ' + plateau[7] + ' | ' + plateau[8])

def condition():
    if plateau[0] == plateau[4] == plateau[8] != " ":
        return True
    elif plateau[2] == plateau[4] == plateau[6] != " ":
        return True
    elif plateau[0] == plateau[3] == plateau[6] != " ":
        return True
    elif plateau[1] == plateau[4] == plateau[7] != " ":
        return True
    elif plateau[2] == plateau[5] == plateau[8] != " ":
        return True
    elif plateau[0] == plateau[1] == plateau[2] != " ":
        return True
    elif plateau[3] == plateau[4] == plateau[5] != " ":
        return True
    elif plateau[6] == plateau[7] == plateau[8] != " ":
        return True
    else:
        return False
        
def demander_case():
    while True:
        try:
            case = int(input("Choisissez une case de 1 à 9 : "))
            if 1 <= case <= 9:
                return case - 1
            print('Veuillez choisir une case valide !')
        except ValueError:
            print('Vous devez choisir un chiffre de 1 à 9.')

def verification_match_nul():
    return " " not in plateau

def jouer():
    joueur_1 = input('Quel est votre nom ? ')
    joueur_2 = input('Quel est votre nom ? ')
    joueurs = [(joueur_1, "X"), (joueur_2, "O")]
    joueur_actuel = random.choice(joueurs)
    print(f"{joueur_actuel[0]}, vous commencez avec {joueur_actuel[1]}")
    
    while True:
        grille()
        print(f"C'est le tour de {joueur_actuel[0]}")
        case = demander_case()
        if plateau[case] != " ":
            print("Cette case est déjà prise !")
            continue
        plateau[case] = joueur_actuel[1]
        
        if condition():
            grille()
            print(f"Félicitations ! {joueur_actuel[0]}, vous avez gagné")
            break
        elif verification_match_nul():
            grille()
            print("Match nul !")
            break
            
            
        joueur_actuel = joueurs[0] if joueur_actuel == joueurs[1] else joueurs[1]

jouer()
