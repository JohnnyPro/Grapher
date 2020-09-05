from sys import argv, exit
from os import system, execv

def main():
	blacklist = []
	start = -10
	end = 10
	jump = 1
	coordinates = {}
	if (len(argv) == 1):
		print("Usage: grapher.py \"FORMULA\"")
		exit(1)

	formula = ""
	for i in range(1, len(argv)):
		if argv[i][:5].lower() == "start":
			start = eval(argv[i][6:])

		elif argv[i][:3].lower() == "end":
			end = eval(argv[i][4:])
		
		elif argv[i][:4].lower() == "jump":
			jump = eval(argv[i][5:])
		
		else:
			formula += argv[i]

	
	for i in range(formula.count("x")):
		place = formula.find('x')
		if place != 0  and formula[place-1].isdigit():
			formula = formula[0:place] + '*(y)' + formula[place+1:len(formula)]
		else:
			formula = formula[0:place] + '(y)' + formula[place+1:len(formula)]
		
		
	i = start	
	while i < end+1:
		x = str(i)
		temp = formula.replace("y", x)
		try:
			coordinates[i] = eval(temp)
		except ZeroDivisionError:
			coordinates[i] = .21
			blacklist.append(i)

		i += jump

	dataToExport = str(coordinates).replace(" ", "")
	system("draw.py " + dataToExport + " " + str(blacklist)) # try to improve this to work with execv


main()

