from board.board import Board
from board.tetromino import Tetromino
from genes.genes import Genes


class Game:
	# TODO: check if new tetromino is not added to non-existing rows (above board)

	def __init__(self, gene: Genes):
		self.board = Board()
		self.is_game_over = False
		self.score = 0
		self.gene = gene

	def play(self):
		while not self.is_game_over:
			# debug
			# self.board.print()

			# get situation of top two rows
			situation = self.board.get_situation()
			# debug
			# print(situation.bin)

			# get new tetromino
			tetromino: Tetromino = Tetromino.get_random()
			rotations_num = self.gene.get_rotation(situation, tetromino.shape_num)
			tetromino.rotate(times=rotations_num)

			# debug
			# print(*tetromino.shape, sep="\n")

			# check if last row is empty and end if not
			if not self.board.can_place_next_tetromino(tetromino):
				self.is_game_over = True
				break

			# place tetromino
			position = self.gene.get_position(situation, tetromino.shape_num)
			self.board.add_tetromino(tetromino, position)
			# debug
			# print("position: " + str(position))

			# remove full rows and add score
			removed_count = self.board.remove_full_rows_and_return_count()
			self.score += removed_count * 1000  # give 1000 pts for each row
			self.score += 34  # give score for each dropped tetromino 30 pieces > 1 row

	# debug
	# print("score: " + str(self.score))

	def restart(self):
		self.board = Board()
		self.is_game_over = False
		self.score = 0

	def get_score(self):
		return self.score

	def get_gene(self):
		return self.gene
