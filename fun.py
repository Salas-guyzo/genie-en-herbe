from modules import *


""" Questionnaire fun"""

nomCategorie="fun"
descriptionCategorie=" Ok un peu de detente avant de faire les devoirs!!!!!"
fun_Cat=Categorie(nomCategorie,descriptionCategorie)


fun=Questionnaire()

"""1"""
monLibelle="Lequel de ces Schtroumpf n'existe pas?"
firstChoice="Celui qui n'existe pas"
secondChoice="Le schtroumpf a lunette"
thirdChoice="Le schtroumpf cosmonaute"
fourthChoice="Le grand schtroumpf"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(1,myQuestion)



"""2"""
monLibelle="Quelle est la couleur du cheval blanc du roi HENRY IV?"
firstChoice="bleu"
secondChoice="vert"
thirdChoice="blanc"
fourthChoice="rouge"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(2,myQuestion)


"""3"""
monLibelle="Sur quelle planete vivons nous?"
firstChoice="Namek"
secondChoice="Krypton"
thirdChoice="La Terre"
fourthChoice="La planete Vegeta"
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(3,myQuestion)


"""4"""
monLibelle="Tom est un chat, et Jerry est?"
firstChoice="un chien"
secondChoice="un porc"
thirdChoice="Une souris"
fourthChoice="Un perroquet"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(4,myQuestion)


"""5"""
monLibelle="De quel super heros  Robin est -il l'acolyte"
firstChoice="Superman"
secondChoice="Aquaman"
thirdChoice="Spiderman"
fourthChoice="Batman"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(5,myQuestion)



"""6"""
monLibelle="De quelle espece vivante est <<Tortue Genial>>"
firstChoice="Un genie"
secondChoice="Une tortue"
thirdChoice="Un dragon"
fourthChoice="Une tortue de mer"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(6,myQuestion)


"""7"""
monLibelle="Que doit tu prendre quand tu es malade"
firstChoice="Un haricot magique"
secondChoice="La potion magique"
thirdChoice="Le yaourt"
fourthChoice="Des medicaments"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
fun.addQuestion(7,myQuestion)