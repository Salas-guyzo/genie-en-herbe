from modules import *


""" Questionnaire geographie"""

nomCategorie="fun"
descriptionCategorie=" testons tes connaissances de ton environnement!!!!!"
geographie_Cat=Categorie(nomCategorie,descriptionCategorie)


geographie=Questionnaire()

"""1"""
monLibelle="Ou se trouve le fleuve Nil"
firstChoice="En Egypte"
secondChoice="Au Congo"
thirdChoice="En France"
fourthChoice="En Mauritanie"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
geographie.addQuestion(1,myQuestion)


"""2"""
monLibelle="Sur quel continent se trouve le Kosovo"
firstChoice="Afrique"
secondChoice="Amerique"
thirdChoice="Europe"
fourthChoice="Asie"
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
geographie.addQuestion(2,myQuestion)