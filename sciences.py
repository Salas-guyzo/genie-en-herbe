from modules import *


""" Questionnaire de sciences"""

nomCategorie="sciences"
descriptionCategorie=" regroupe tous les themes scientifiques, physiques et metaphysiques BIG BANG!!!!!"
sciences_Cat=Categorie(nomCategorie,descriptionCategorie)


sciences=Questionnaire()

"""1"""
monLibelle="Quel est l'animal terrestre le plus rapide?  "
firstChoice="la tortue"
secondChoice="le serpent"
thirdChoice="le lievre"
fourthChoice="Le guepard"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(1,myQuestion)


"""2"""
monLibelle="De quoi sont recouvertes tes dents ?  "
firstChoice="d'email"
secondChoice="d'os"
thirdChoice="d'ivoire"
fourthChoice="d'ecaille"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(2,myQuestion)



"""3"""
monLibelle="De quel cote de ton coprs se trouve ton coeur  ?  "
firstChoice="a gauche"
secondChoice="a droite"
thirdChoice="au milieu"
fourthChoice="en bas"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(3,myQuestion)



"""4"""
monLibelle="Quelle partie du corps te permet de sentir ?  "
firstChoice="le nez"
secondChoice="la bouche"
thirdChoice="les yeux"
fourthChoice="les oreilles"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(4,myQuestion)



"""5"""
monLibelle="Combien avons-nous de poumons ? "
firstChoice="un"
secondChoice="quatre"
thirdChoice="aucun"
fourthChoice="deux"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(5,myQuestion)




"""6"""
monLibelle="Que faut-il faire avant de manger ? "
firstChoice="preparer"
secondChoice="se laver les mains"
thirdChoice="boire"
fourthChoice="dormir"
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(6,myQuestion)



"""7"""
monLibelle="Sur quelle feuille le médecin écrit-il quand tu es malade?"
firstChoice="Un recu"
secondChoice="Une convocation"
thirdChoice="Une ordonnance"
fourthChoice="Une facture"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(7,myQuestion)



"""8"""
monLibelle="Combien de mois y-a-t-il en une année?"
firstChoice="12"
secondChoice="29"
thirdChoice="52"
fourthChoice="6"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(8,myQuestion)


"""9"""
monLibelle="Combien de planetes comptent le systeme solaire ?"
firstChoice="Trois"
secondChoice="Six"
thirdChoice="Neuf"
fourthChoice="Douze"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(9,myQuestion)


"""10"""
monLibelle="Que transporte le sang dans le corps?"
firstChoice="l'oxygene"
secondChoice="l'eau"
thirdChoice="la nourriture"
fourthChoice="le paludisme "
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
sciences.addQuestion(10,myQuestion)




