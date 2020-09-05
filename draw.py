from sys import argv
from turtle import *
from os import system

t = Turtle()
s = Screen()
t.pensize(3)
s.bgcolor('black')
t.color('white')
t.speed(10)
data = eval(argv[1])
blacklist = eval(argv[2])
keys = list(data.keys())
values = list(data.values())
jump = keys[1] - keys[0]

def main():

	scope = (max(keys) +max(values)) /2
	drawAxis(scope)
	print(data)
	draw(data)
	system("PAUSE")

def draw(data):
	t.penup()
	t.goto(keys[0], values[0])
	t.pendown()
	t.speed(10)
	iswritting = True
	for i in data:
		if not iswritting:
			t.pendown()
			iswritting = True

		if i in blacklist:
			t.penup()
			t.goto(i, data[i-jump])
			t.pendown()
			t.circle(jump)
			t.penup()
			iswritting = False
		else:
			t.goto(i, data[i])

def drawAxis(scope):
	t.color('cyan')
	t.penup()
	t.goto(scope,0)
	t.pendown()
	t.goto(-scope, 0)

	t.penup()
	t.goto(0, scope)
	t.pendown()
	t.goto(0, -scope)
	t.color('white')


main()

