# -*-coding:UTF-8 -*
from random import randrange
from math import ceil
argentDepart=100
while (argentDepart >0): 
	print (argentDepart,"$")
	mise = input ("how much do you want play?") # recovert the variable mise
	mise = int (mise) #transform mise in int
	caseChoisi = input("on which box?") # recovert the variable caseChoisi
	caseChoisi = int(caseChoisi) # transform caseChoisi in int
	x= ceil(mise/2) #Rounded to the nearest number
	nbAlleatoire = randrange (50) #random 50
	caseRouge=nbAlleatoire%2 # determine the color
	print ("the nb winner is :", nbAlleatoire) # diplay random nb
	if (caseChoisi==nbAlleatoire): 
		argentDepart= argentDepart + mise*3
		print("well done! You win", mise*3)
	if (caseChoisi%2 == caseRouge):
		argentDepart= argentDepart + x
		print("well done, is the same color, you win!", x)
	else:
		argentDepart=argentDepart-mise
		print ("not same nb or color\nyou loose...", mise)