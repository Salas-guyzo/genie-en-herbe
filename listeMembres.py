from modules import *



"""Creation de deux joueur toto et dora et de leurs parents respectifs"""

connectedPlayer=Joueur(0,"@pseudo","@password",50,0)


toto=Joueur(1,"toto","motDePasse",12, 11)
dad=Parent(11,"Salas",True,"salassenior@gmail.com")

dora=Joueur(2,"dora","myPassWord",8,22)
mum=Parent(22,"Sabine",False,"sabine@gmail.com")

listeJoueur=list()
listeJoueur.append(toto)
listeJoueur.append(dora)

listeParent=list()
listeParent.append(dad)
listeParent.append(mum)