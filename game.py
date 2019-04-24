from board import Board
from gene import Gene
from genes_functions import get_situation
from tetromino import Tetromino


class Game:
	# TODO: check if new tetromino is not added to non-existing rows (above board)

	def __init__(self, gene: Gene):
		self.board = Board()
		self.is_game_over = False
		self.score = 0
		self.gene = gene

	def play(self):
		while not self.is_game_over:
			# get situation of top two rows
			top_rows = self.board.get_top_two_rows()
			situation = get_situation(top_rows)

			# get reactions
			reactions = self.gene.get_reactions(situation)

			# get new tetromino
			tetromino = Tetromino.get_random()
			rotations_num = self.gene.get_rotations(reactions, tetromino)
			tetromino.rotate(times=rotations_num)

			# place tetromino
			position = self.gene.get_position(reactions, tetromino)
			self.board.add_tetromino(tetromino, position)

			# remove full rows and add score
			removed_count = self.board.remove_full_rows_and_return_count()
			self.score += removed_count

			# check if last row is empty and end if not
			if not self.board.is_top_row_empty():
				self.is_game_over = True

	def get_score(self):
		return self.score

	def get_gene(self):
		return self.gene
