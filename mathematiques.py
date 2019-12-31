from modules import *


""" Questionnaire de mathematiques"""

nomCategorie="mathematiques"
descriptionCategorie=" c'est parti pour quelques formules et calcul"
mathematiques_Cat=Categorie(nomCategorie,descriptionCategorie)

mathematiques=Questionnaire()

"""1"""
monLibelle="combien font 3x2x4x0?"
firstChoice="0"
secondChoice="24"
thirdChoice="9"
fourthChoice="324"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
mathematiques.addQuestion(1,myQuestion)


"""2"""
monLibelle="Comment calculer le perimetre d'un carre ?"
firstChoice="(2 x cote)+ (2 x cote)"
secondChoice="cote+4 "
thirdChoice="cote +( 4 x cote)"
fourthChoice="cote x( 4 + cote)"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
mathematiques.addQuestion(2,myQuestion)



"""3"""
monLibelle="Qu'est ce qu'un triangle rectangle? "
firstChoice="Un triangle qui ressemble a un rectangle"
secondChoice="Un rectangle qui ressemble a un triangle"
thirdChoice="Un triangle qui a deux cotes de meme mesure"
fourthChoice="Un triangle qui a un angle droit  "
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
mathematiques.addQuestion(3,myQuestion)


"""4"""
monLibelle="Quand dit on de deux droites qu'elles sont paralleles "
firstChoice="Quand elles partent sur une aile"
secondChoice="quand elle ne se croisent jamais"
thirdChoice="quand elle peuvent se croiser plusieurs fois"
fourthChoice="quand elle ne sont pas perpendiculaires "
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
mathematiques.addQuestion(4,myQuestion)



"""5"""
monLibelle="Combien y'a t-il d'heure dans une semaine?"
firstChoice="48"
secondChoice="72"
thirdChoice="144"
fourthChoice="168 "
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
mathematiques.addQuestion(5,myQuestion)