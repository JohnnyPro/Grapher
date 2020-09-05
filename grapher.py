from sys import argv, exit
from os import system, execv

#This file deals with the maths part of the graphing
# things like formulating the value of "Y" for a certain "X"
def main():
	blacklist = [] # this is to store the X value of the "holes" of the graph
	start = -10 #Default value for start of X
	end = 10 # Default value for the end of X
	jump = 1 # value for smoothing out the graph
	coordinates = {} 
	formula = ""
	if (len(argv) > 1):
		rawFormula = argv[1::]
		
	else:
		rawFormula = Input("Formula: ")
		rawFormula = rawFormula.split(' ')
	
	for i in range(0, len(rawFormula)):
		if rawFormula[i][:5].lower() == "start":
			start = eval(rawFormula[i][6:])

		elif rawFormula[i][:3].lower() == "end":
			end = eval(rawFormula[i][4:])
		
		elif rawFormula[i][:4].lower() == "jump":
			jump = eval(rawFormula[i][5:])
		
		else:
			formula += rawFormula[i]
	
	for i in range(formula.count("x")):
		place = formula.find('x')
		if place != 0  and formula[place-1].isdigit():
			formula = formula[0:place] + '*(t)' + formula[place+1:len(formula)]
		else:
			formula = formula[0:place] + '(t)' + formula[place+1:len(formula)]
	
		
	i = start	
	while i < end+1:
		x = str(i)
		temp = formula.replace("t", x)
		try:
			coordinates[i] = eval(temp)
		except ZeroDivisionError:
			coordinates[i] = .21
			blacklist.append(i)

		i += jump

	dataToExport = str(coordinates).replace(" ", "")
	system("draw.py " + dataToExport + " " + str(blacklist)) # try to improve this to work with execv


main()

