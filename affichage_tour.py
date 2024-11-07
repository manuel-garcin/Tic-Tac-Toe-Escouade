grille = ["1","2","3","4","5","6","7","8","9"]

def morpion():

    def affichage_grille():
        print("\n")
        print("-------------")
        print("|",grille[0],"|",grille[1],"|",grille[2],"|")
        print("-------------")
        print("|",grille[3],"|",grille[4],"|",grille[5],"|")
        print("-------------")
        print("|",grille[6],"|",grille[7],"|",grille[8],"|")
        print("\n")

    affichage_grille()

    def mon_tour():
        joueur1 = input("entre 1 et 3 :")
        if joueur1 == "3":
            grille[2] = "X"            
            affichage_grille()
        else:
            print("veuilliez rejouer :")
            joueur1 == input("entre 1 et 3 :")


    mon_tour()

morpion()