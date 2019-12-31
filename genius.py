from modules import *
from fonctions import*


choix=""
while(choix not in ("1","2","3")):
    print("\n")
    print("*******************************************************************************")
    print("*--------------------MENU PRINCIPAL GENIE EN HERBE----------------------------*")
    print("*******************************************************************************")
    print("\n \n \n ")
    print(" \t 1.) S'inscrire \n  ")
    print(" \t 2.) Se connecter \n  ")
    print(" \t 3.) Quitter \n ")
    print("\n")
    choix= (input(" \t Entrez le numero de l'action \t\t "))
    if (choix not in ("1","2","3")):
        print(" \n \t Selection invalide \n")
    if(choix=="1"):
        print("\n\n")
        print("\t Premiere inscription")
        inscrireJoueur()
        afficherListeJoueur()
        afficherListeParent()
        choix = ""
    if(choix=="2"):
        connectedPlayer=seConnecter()
        if(type(connectedPlayer) == bool ):
            print ("\n \t identifiants de connexion incorects")
        else:
            action = ""
            print("\n \n")
            while (action not in ("1", "2", "3")):
                print("\t \t *************************************************")
                print("\t \t *       Tu es connecte entend que " + connectedPlayer.pseudo +"\t\t    *")
                print("\t \t *************************************************")
                print("\n")
                print(" \t 1.) Jouer une partie \n  ")
                print(" \t 2.) Consulter performances (par le parent) \n  ")
                print(" \t 3.) Se deconnecter \n ")
                print("\n")
                action = (input("\n \t Entrez le numero de l'action \t\t "))
                if (action not in ("1", "2", "3")):
                    print(" \t Selection invalide \n \n")
                if (action == "1"):
                    jouer(connectedPlayer)
                    action = ""
                if (action=="2"):
                    verifierParente(connectedPlayer)
                    action = ""
                if (action=="3"):
                    print("\t Deconnexion effecttuee")
                    action = ""
                    break
        choix =""
    if (choix == "3"):
        print("\n \n \t FIN DE LA DEM0 ET A LA PROCHAINE")
        choix =""
        break


print(" \n \n tout est ok")


#FIN DU PROGRAMME








