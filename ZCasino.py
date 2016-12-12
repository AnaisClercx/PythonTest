# -*-coding:UTF-8 -*
from random import randrange
from math import ceil
argentDepart=100
while (argentDepart >0):
	print (argentDepart,"$")
	mise = input ("how much do you want play?")
	mise = int (mise)
	caseChoisi = input("on which box?")
	caseChoisi = int(caseChoisi)
	x= ceil(mise/2)
	nbAlleatoire = randrange (50)
	caseRouge=nbAlleatoire%2
	print ("the nb winner is :", nbAlleatoire)
	if (caseChoisi==nbAlleatoire):
		argentDepart= argentDepart + mise*3
		print("well done! You win", mise*3)
	if (caseChoisi%2 == caseRouge):
		argentDepart= argentDepart + x
		print("well done, is the same color, you win!", x)
	else:
		argentDepart=argentDepart-mise
		print ("not same nb or color\nyou loose...", mise)