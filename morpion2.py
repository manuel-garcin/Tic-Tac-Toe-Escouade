joueur_actuel = ""
grille = ["-","-","-","-","-","-","-","-","-"]
fin_du_jeu = False
gagnant = ""

def jeu():
    global fin_du_jeu, joueur_actuel, grille
    choix_joueur()
    grilledejeu()
    while not fin_du_jeu:
        tour(joueur_actuel)
        conditions_victoire()
        condition_match_nul()
        if not fin_du_jeu:
            joueur_suivant()
    resultat()

def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Choisir un signe (X), ou (O) :")
    while joueur_actuel.upper() not in ["X", "O"]:
        joueur_actuel = input("Choisir un signe valide (X), ou (O) :")
    joueur_actuel = joueur_actuel.upper()
    print(f"Vous jouez avec {joueur_actuel}. L'autre joueur jouera avec {'O' if joueur_actuel == 'X' else 'X'}.")

def grilledejeu():
    print("\n")
    print("-------------")
    for i in range(3):
        print("|", grille[i*3], "|", grille[i*3+1], "|", grille[i*3+2], "|")
        print("-------------")
    print("\n")

def tour(joueur):
    print(f"C'est au tour du joueur : {joueur}")
    valide = False
    while not valide:
        position = input("Veuillez choisir une case entre 1 et 9 : ")
        if position not in ["1","2","3","4","5","6","7","8","9"]:
            print("Choisir un chiffre valide entre 1 et 9.")
            continue
        position = int(position) - 1
        if grille[position] == "-":
            grille[position] = joueur
            valide = True
        else:
            print("Case déjà prise, choisissez une autre case.")
    grilledejeu()

def conditions_victoire():
    global fin_du_jeu, gagnant
    # Vérification des lignes
    for i in range(0, 9, 3):
        if grille[i] == grille[i+1] == grille[i+2] != "-":
            fin_du_jeu = True
            gagnant = grille[i]
            return
    # Vérification des colonnes
    for i in range(3):
        if grille[i] == grille[i+3] == grille[i+6] != "-":
            fin_du_jeu = True
            gagnant = grille[i]
            return
    # Vérification des diagonales
    if grille[0] == grille[4] == grille[8] != "-":
        fin_du_jeu = True
        gagnant = grille[0]
    elif grille[2] == grille[4] == grille[6] != "-":
        fin_du_jeu = True
        gagnant = grille[2]

def condition_match_nul():
    global fin_du_jeu
    if "-" not in grille:
        fin_du_jeu = True

def joueur_suivant():
    global joueur_actuel
    joueur_actuel = "O" if joueur_actuel == "X" else "X"

def resultat():
    if gagnant:
        print(f"Le joueur {gagnant} a gagné !")
    else:
        print("Match nul.")

# Lancer le jeu
jeu()
