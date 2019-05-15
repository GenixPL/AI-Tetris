from board.board import Board
from board.tetromino import Tetromino
from board.tetromino_spawner import TetrominoSpawner
from bots.genes import Genes


class Game:
	# TODO: check if new tetromino is not added to non-existing rows (above board)

	def __init__(self, gene: Genes):
		self.board = Board()
		self.tetromino_spawner = TetrominoSpawner()
		self.is_game_over = False
		self.score = 0
		self.gene = gene

	def play(self):
		for i in range(1):  # this range changes the number of times single game is played (more games are better in case of random spawning)
			self.is_game_over = False  # TODO
			self.board = Board()

			while not self.is_game_over:
				# get situation of top two rows
				situation = self.board.get_situation()

				# get new tetromino
				tetromino: Tetromino = self.tetromino_spawner.spawn()
				rotations_num = self.gene.get_rotation(situation, tetromino.shape_num)
				tetromino.rotate(times=rotations_num)

				# check if last row is empty and end if not
				if not self.board.can_place_next_tetromino(tetromino):
					self.is_game_over = True
					break

				# place tetromino
				position = self.gene.get_position(situation, tetromino.shape_num)
				self.board.add_tetromino(tetromino, position)

				# remove full rows and add score
				removed_count = self.board.remove_full_rows_and_return_count()
				self.score += removed_count * 10000  # give 1000 pts for each row
				self.score += 1  # give score for each dropped tetromino 30 pieces > 1 row

	def restart(self):
		self.board = Board()
		self.tetromino_spawner = TetrominoSpawner()
		self.is_game_over = False
		self.score = 0

	def get_score(self):
		return self.score

	def get_gene(self):
		return self.gene
