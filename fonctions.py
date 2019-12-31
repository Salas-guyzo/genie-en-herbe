from modules import *
from listeMembres import *




def inscrireJoueur():

    smsValidation=""
    toutEstValide=False
    compteur=0


    while (toutEstValide==False):
        pseudo=input("\n\t Entrez pseudo\t")
        mot_de_passe=input("\t Entrez votre mot de passe \t")
        age = int(input("\t Entrez age \t"))
        nom_parent = input("\t Entrez le nom du parent \t")
        sexe_parent = input("\t Entrez le sexe du parent (h/f) \t")
        email_parent = nom_parent + "@jeuxgenie.com"

        if (validerPseudo(pseudo)==False):
            smsValidation+="Ce pseudo est deja attribue a un autre enfant \n"
        else:
            compteur+=1
        if (validerSexe(sexe_parent)==False):
            smsValidation+="Saisie sexe incorrecte (h/f) \n"
        else:
            compteur+=1
        if (validerAge(age)==False):
            smsValidation+="\t Age!!! Vous n'etes plus un tout petit  \n"
        else:
            compteur+=1

        if(compteur!=3):
            print("\n ECHEC LORS DE L'INSCRIPTION POUR : \n \t " + smsValidation +" \n \n NOUVELLE TENTATIVE")
        else:
            print("\n INSCRIPTION OK")
            toutEstValide = True
            new_id=len(listeJoueur) +1
            new_id_parent= len(listeParent) +1
            newPlayer=Joueur(new_id,pseudo,mot_de_passe,age,new_id_parent)
            print("\t notez l'id parent= "+ str(new_id_parent)+ " pour afficher les performances plus tard \t"  )
            if(sexe_parent=="h"):
                sexeInt=1
            else:
                sexeInt=0
            newTutor=Parent(new_id_parent,nom_parent,sexeInt,email_parent )
            listeJoueur.append(newPlayer)
            listeParent.append(newTutor)
            print("\t Verification avec les listes des autres membres \n")





def validerSexe(newSexe):

    if(newSexe in ("h","f")):
        return True
    return False



def validerAge(newAge):

    if((3<=newAge<=15)):
        return True
    return False


def validerPseudo(newPseudo):

    for j in listeJoueur:
        if(j.pseudo==newPseudo):
            return False
    return True




def afficherListeJoueur():

    print("\n LISTE DES JOUEURS DU SITE \n \nPseudo \t\t     Age \n")
    for j in listeJoueur:
        j.afficherJoueur()

def afficherListeParent():

    print("\n LISTE DES PARENTS DE JOUEUR \n \n Noms \t\t     @email \n")
    for p in listeParent:
        p.afficherParent()



def seConnecter():

    pseudo = input("\t \t saisis ton pseudo  \t\t\t  ")
    mot_de_passe = input("\t\t maintenant mot de passe \t\t")
    for j in listeJoueur:
        if(pseudo==j.pseudo):
            if(mot_de_passe==j.password):
                return j
    return False


def afficherListeCategories():
    print()
    print("SELECTION DU THEME \n \n  ")
    rang=1
    for key,val in listeCategories.items():
        print ( str(rang) +".) "+ val)
        rang+=1
        print()






def jouer(connectedPlayer):

    print ("\n Quelle categorie veux tu jouer?")
    afficherListeCategories()
    num=int(input("\n Choisissez un numero \t "))
    while (num not in range(1,len(listeCategories)+1)):
        print("\n \n Theme invalide")
        num = int(input("Choisir un autre numero \t "))
    pos=0
    for K,V in listeCategories.items():
        pos=pos+1
        if (pos==num):
            myQuestionList=K
            nom_categorie=V
            break
    print(" \n \n LET'S PLAY \t "+nom_categorie+  "\t NOW KID \n" )
    myParty=Partie(nom_categorie, connectedPlayer.id,myQuestionList)
    myParty.play()
    print("\n \t \t fin de partie \n ")
    listeParties.append(myParty)





def afficherListeParties(player):
    nbp=0
    print("\n\n \t Parties de" + player.pseudo)
    print()
    print("Theme \t\t\t " +  "  Score final\n ")
    for p in listeParties:
        if(player.id==p.id_joueur):
            p.afficherPartie()
            nbp+=1
    if (nbp==0):
        print("\n \t  Votre enfant n'a pas encore joue \n ")
    else:
        print("\n \t \t peux faire mieux \n \n ")

def verifierParente(connectedPlayer):
    print(" Pour consulter les performances veuillez")
    id_parent= int(input("Saisir l'id qu'on vous a communique a l'inscription \t "))
    if (connectedPlayer.isChild(id_parent)==False):
        print("Allo police!!! Un individu follow un enfant.. ")
    else:
        afficherListeParties(connectedPlayer)
















