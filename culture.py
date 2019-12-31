from modules import *


""" Questionnaire de culture generale"""

nomCategorie="culture"
descriptionCategorie=" regroupe tous les themes scientifiques, physiques et metaphysiques BIG BANG!!!!!"
culture_Cat=Categorie(nomCategorie,descriptionCategorie)


culture=Questionnaire()

"""1"""
monLibelle="Qui a decouvert l'Amerique?"
firstChoice="Leopold Sedar Senghor"
secondChoice="Micheal Jordan"
thirdChoice="Christophe Colomb"
fourthChoice="Saddam Hussein "
trueResponse="c"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(1,myQuestion)


"""2"""
monLibelle="Quelle civilisation ancienne est symbolisee les pyramides?"
firstChoice="Egypte"
secondChoice="Maya"
thirdChoice="Les Romains"
fourthChoice="Les nazi"
trueResponse="a"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(2,myQuestion)


"""3"""
monLibelle=" Une année c'est le temps que met la terre à tourner autour?"
firstChoice="De la lune "
secondChoice="Du soleil"
thirdChoice=" D'elle meme"
fourthChoice="du ciel "
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(3,myQuestion)



"""4"""
monLibelle=" Combien de jours dure le mois d'aout?"
firstChoice="Trente"
secondChoice="vingt huit"
thirdChoice="vingt neuf"
fourthChoice="trente et un"
trueResponse="d"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(4,myQuestion)



"""5"""
monLibelle="Qui soigne les animaux?"
firstChoice="Le Docteur "
secondChoice="Le veterinaire"
thirdChoice="L'animalogue"
fourthChoice="Papa"
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(5,myQuestion)


"""6"""
monLibelle="Dans quel de ces pays d'afrique parle t-on le portuguais?"
firstChoice="La Lesotho"
secondChoice="L'angola"
thirdChoice="Le Bostwana"
fourthChoice="Le zimbabwe"
trueResponse="b"

contenu = { "libelle":monLibelle,
                        "a":firstChoice,
                        "b":secondChoice,
                        "c":thirdChoice,
                        "d":fourthChoice,
                        "$":trueResponse
                      }

myQuestion=Question(contenu)
culture.addQuestion(6,myQuestion)















