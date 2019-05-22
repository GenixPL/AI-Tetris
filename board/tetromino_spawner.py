from board.tetromino import Tetromino
from files.config import get_spawn_mode


class TetrominoSpawner:

	def __init__(self, tetromino_seq=None):
		self.i = 0

		if tetromino_seq is not None:
			self.tetromino_sequence = tetromino_seq.copy()
		else:
			self.tetromino_sequence = None

	def spawn(self):
		self.i += 1

		spawn_mode = get_spawn_mode()

		if spawn_mode == 0:
			return Tetromino.get_random()

		elif spawn_mode == 1:
			tetromino = self.tetromino_sequence[0]
			del self.tetromino_sequence[0]

			return Tetromino(tetromino % 7)

		elif spawn_mode == 2:
			return Tetromino(self.i % 7)
