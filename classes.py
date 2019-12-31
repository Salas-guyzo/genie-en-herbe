
class Joueur:
    """Classe définissant un enfant caractérisée par :
    - son identifiant
    - son nom
    - son age
    - son parent """

    def __init__(self,id,pseudo,password,age,id_parent):
        """Constructeur de notre classe"""

        self.id = id
        self.pseudo=pseudo
        self.age=age
        self.id_parent=id_parent
        self.password=password

    def afficherJoueur(self):
        if (self.id!=0):
            print(self.pseudo + "\t\t\t "+ str(self.age) +" ans")


    def isChild(self,id_tuteur):
        if (self.id_parent==id_tuteur):
            return True
        return False




class Parent:

    def __init__(self):
        self.id = 0
        self.nom = "@nom "
        self.sexe = "@sexe"
        self.email = "@email"


    def __init__(self,id,nom,sexe,email):
        """Constructeur de notre classe"""

        self.id = id
        self.nom = nom
        self.sexe=sexe
        self.email=email


        """ determine si l'enfant en parametre est celui du parent en cours"""


    def afficherParent(self):
        print(self.nom + "\t\t\t "+ (self.email))


class Categorie:

    def __init__(self,nom,description):
        """Constructeur de notre classe"""

        self.nom=nom
        self.description=description

    def describe(self):
        print ( "La categorie << " + self.nom + ">>" + self.description)


class Question:

    """Le contenu est un dictionnaire de structure
            contenu = { libelle:monLibelle,
                        a:firstChoice,
                        b:secondChoice,
                        c:thirdChoice,
                        d:fourthChoice,
                        $:trueResponse in (a,b,c,d?)
                      }"""

    def __init__(self,contenu):
        self.contenu=contenu


    def quizz(self):

        print("\n")
        print(self.contenu["libelle"])
        print()

        for clef in self.contenu:
            if clef in ("a", "b", "c", "d"):
                print("\t" + clef + '.)' + self.contenu[clef])




    """attribuer un nombre de point a une question selon la proposition du joueur"""

    def evaluate(self, choiceJoueur):

        if (self.contenu["$"] == choiceJoueur):
            return 1
        return 0



class Questionnaire:

    """Dictionnaire sous la forme qs= {id_question:question}"""

    def __init__(self):

        self.listeQuestion = {}


    def addQuestion(self,id_question,question):

        self.listeQuestion[id_question]=question


    def afficherAll(self):

        for key, value in self.listeQuestion.items():
            value.quizz()


class Partie:

    def __init__(self,nom_categorie,id_joueur,questionnaire):

        self.nom_categorie=nom_categorie
        self.id_joueur=id_joueur
        self.questionnaire=questionnaire
        self.score=0
        self.nbreQuestion=0


    """noteQuestion= 0, +1,-0,25 si on veut faire des malus en cas de mauvaise reponse"""

    def updateScore(self,noteQuestion):

        self.score=self.score+noteQuestion
        if (noteQuestion>0):
            message="  Bravo , bonne reponse"
        else:
            message="  Oups, c'etait pas le meilleur choix"
        print (message)




    """Affichage du score final en pourcentage"""

    def afficherScoreFinal(self,nbre_question):

        print ("SCORE FINAL : \t " + str(self.score) + "/" + str(self.nbreQuestion))
        print ("Good Answers:\t " + str((self.score/nbre_question)*100) + "%" )




    def play(self):


        for key,val in self.questionnaire.listeQuestion.items():
            val.quizz()
            print("\t")
            self.nbreQuestion +=1
            choiceJoueur = input("Quelle est la bonne reponse? \t ")
            point = val.evaluate(choiceJoueur)
            print("  "+ str(point) + " point ")
            self.updateScore(point)
            print("  Score actuel " +str(self.score) + "/" + str(self.nbreQuestion))

        print()
        if (self.nbreQuestion>0):
            self.afficherScoreFinal(self.nbreQuestion)


    """Afficher les details d'une partie"""


    def afficherPartie(self):
        print (self.nom_categorie + " \t " + " \t \t " + str(self.score) + "/" + str(self.nbreQuestion))










