# -*-coding:UTF-8 -*
from random import randrange
from math import ceil
argentDepart=100
while (argentDepart >0):
	print (argentDepart,"$")
	mise = input ("combien voulez vous jouer?")
	mise = int (mise)
	caseChoisi = input("sur quelle case?")
	caseChoisi = int(caseChoisi)
	x= ceil(mise/2)
	nbAlleatoire = randrange (50)
	caseRouge=nbAlleatoire%2
	print ("le numero gagnant est le", nbAlleatoire)
	if (caseChoisi==nbAlleatoire):
		argentDepart= argentDepart + mise*3
		print("bravo! c'est le bon num, vous gagnez", mise*3)
	if (caseChoisi%2 == caseRouge):
		argentDepart= argentDepart + x
		print("bravo! c'est la bonne couleur, vous gagnez", x)
	else:
		argentDepart=argentDepart-mise
		print ("pas la bonne couleur\nvous avez perdu", mise)

