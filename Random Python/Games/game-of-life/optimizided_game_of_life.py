import random as rand
import time

DEAD = 0
LIVE = 1

class Board:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = self.create_random_board()

	def create_dead_board(self):
		return [[DEAD for _ in range(self.width)] for _ in range (self.height)]

	def random_cell_state(self):
		if rand.random() >= 0.85:
			return LIVE
		return DEAD

	def create_random_board(self):
		self.board = self.create_dead_board()
		self.board = [[self.random_cell_state() for _ in range (self.width)] for _ in range (self.height)]
		return self.board

	def calc_next_cell_state(self, x, y):
		n_live_neighbors = 0
		# Iterate around this cell's neighbors
		for x1 in range((x-1), (x+1)+1):
			# Make sure we don't go off the edge of the board
			if x1 < 0 or x1 >= self.width: continue
			for y1 in range((y-1), (y+1)+1):
				# Make sure we don't go off the edge of the board
				if y1 < 0 or y1 >= self.height: continue
				# Make sure we don't count the cell as a neighbor of itself!
				if x1 == x and y1 == y: continue

				if self.board[x1][y1] == LIVE:
					n_live_neighbors += 1
			
		if self.board[x][y] == LIVE:
			if n_live_neighbors <= 1:
				return DEAD
			elif n_live_neighbors <= 3:
				return LIVE
			else:
				return DEAD
		else:
			if n_live_neighbors == 3:
				return LIVE
			else:
				return DEAD		

	def next_board_state(self):
		new_board = self.create_dead_board()
		for i in range (self.width):
			for j in range (self.height):
				new_board[i][j] = self.calc_next_cell_state(i, j)
		# TODO -> Check later
		return new_board

	def render_board(self):
		display_as = {
			DEAD: ' ',
			LIVE: u"\u2588"
		}
		lines = []
		for y in range (self.height):
			line = ''
			for x in range (self.width):
				line += display_as[self.board[x][y]] * 2
			lines.append(line)
		print("\n".join(lines))

	def run_forever(self):
		while True:
			self.render_board()
			self.board = self.next_board_state()
			time.sleep(0.03)


width = int(input('Enter Windows width:'))
height = int(input('Enter Windows height:'))
new_board = Board(width, height)
new_board.run_forever()