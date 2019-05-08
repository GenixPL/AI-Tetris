from board.tetromino import Tetromino
from files.config import get_spawn_random_tetrominoes


class TetrominoSpawner:

	def __init__(self):
		self.tetromino_counter = 0

	def spawn(self):
		is_random = get_spawn_random_tetrominoes()

		if is_random:
			return Tetromino.get_random()
		else:
			self.tetromino_counter += 1
			return Tetromino(self.tetromino_counter % 7)
