from board.tetromino import Tetromino
from files.config import get_spawn_random_tetrominoes


class TetrominoSpawner:

	def __init__(self, tetromino_seq=None):
		if tetromino_seq is not None:
			self.tetromino_sequence = tetromino_seq.copy()
		else:
			self.tetromino_sequence = None

	def spawn(self):
		is_random = get_spawn_random_tetrominoes()

		if is_random:
			return Tetromino.get_random()

		else:
			tetromino = self.tetromino_sequence[0]
			del self.tetromino_sequence[0]

			return Tetromino(tetromino % 7)
