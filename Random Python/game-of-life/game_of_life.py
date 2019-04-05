import random as rand
import time

DEAD = 0
LIVE = 1

def create_dead_board(width, height):
	return [[DEAD for _ in range (width)] for _ in range (height)]

def randomize_cell_state():
	if rand.random() >= 0.85:
		return LIVE
	return DEAD

def board_width(board):
	return len(board)

def board_height(board):
	return len(board[0])

def create_random_board(width, height):
	board = create_dead_board(width, height)
	board = [[randomize_cell_state() for _ in range(width)] for _ in range(height)]
	return board

def render_board(board):
    """Displays a state by printing it to the terminal.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    Nothing - this is purely a display function.
    """
    display_as = {
        DEAD: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick
        # "ASCII" character like a '$' or '#'.
        LIVE: u"\u2588"
    }
    lines = []
    for y in range(0, board_height(board)):
        line = ''
        for x in range(0, board_width(board)):
            line += display_as[board[x][y]] * 2
        lines.append(line)
    print ("\n".join(lines))


def next_cell_state(cell_coords, board):
	width = board_width(board)
	height = board_height(board)
	x = cell_coords[0]
	y = cell_coords[1]
	n_live_neighbors = 0

    # Iterate around this cell's neighbors
	for x1 in range((x-1), (x+1)+1):
        # Make sure we don't go off the edge of the board
		if x1 < 0 or x1 >= width: continue
		for y1 in range((y-1), (y+1)+1):
			# Make sure we don't go off the edge of the board
			if y1 < 0 or y1 >= height: continue
			# Make sure we don't count the cell as a neighbor of itself!
			if x1 == x and y1 == y: continue

			if board[x1][y1] == LIVE:
				n_live_neighbors += 1
		
	if board[x][y] == LIVE:
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

	
def next_board_state(old_board):
	width = board_width(old_board)
	height = board_height(old_board)
	new_board = create_dead_board(width, height)

	for i in range (width):
		for j in range (height):
			new_board[i][j] = next_cell_state([i, j], old_board)
	return new_board

def run_game_forever(board):
	new_board = board
	while True:
		render_board(new_board)
		new_board = next_board_state(new_board)
		time.sleep(0.03)

if __name__ == "__main__":
	board = []
	board = create_random_board(100, 100)
	run_game_forever(board)