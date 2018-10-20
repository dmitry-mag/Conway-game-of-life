from tkinter import *
import time
from random import randint as rnd


WIDTH = 440
HEIGHT = 440
DOT_SIZE = 20
DELAY = 500


class Point():
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.status = state

class Board(Canvas):
	def __init__(self, parent):
		Canvas.__init__(self, width=WIDTH, height=HEIGHT, highlightthickness=0)
		self.parent = parent
		self.initGame()
		self.pack()


	def initGame(self):
		self.array = self.initArray()
		self.temp_array = self.initArray()
		self.startPositions()
		self.onTimer()


	def initArray(self):
		a = []
		for yyy in range(0, 22):
			for xxx in range(0, 22):
				p = Point(xxx * DOT_SIZE, yyy * DOT_SIZE, 0)
				a.append(p)
		return a

	def startPositions(self):
		for y in range(6, 16):
			for x in range(6, 16):
				position = 20 * y + 2 * y + x
				self.array[position].status = rnd(0,1)


	def printAll(self, ar):
		for el in ar:
			if el.status == 1:
				color = "black"
			elif el.status == 0:
				color = "green"
			self.create_rectangle(el.x, el.y, el.x + DOT_SIZE, el.y + DOT_SIZE,
					fill=color, width=0)


	def step(self, array, temp):
		for y in range(1, 21):
			for x in range(1, 21):
				cell = 20 * y + 2 * y + x
				environ = (array[cell - 1].status + array[cell + 1].status
						+ array[cell - 23].status + array[cell - 22].status
						+ array[cell - 21].status + array[cell + 21].status
						+ array[cell + 22].status + array[cell + 23].status)
				if array[cell].status == 0:
					temp[cell].status = 0
					if environ == 3:
						temp[cell].status = 1
				else:
					temp[cell].status = 1
					if environ < 2 or environ > 3:
						temp[cell].status = 0
		return temp


	def onTimer(self):
		self.printAll(self.array)
		self.temp_array = self.step(self.array, self.temp_array)
		self.array = self.temp_array
		self.after(DELAY, self.onTimer)


class Life(Frame):
	def __init__(self,parent):
		Frame.__init__(self, parent)
		parent.title('The Life')
		self.board = Board(parent)
		self.pack()


def main():
	root = Tk()
	life = Life(root)
	root.mainloop()


if __name__ == '__main__':
 	main()
 