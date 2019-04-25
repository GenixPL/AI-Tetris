from bitstring import BitArray
from numpy import zeros

from board.tetromino import Tetromino
from board.two_dim_array import TwoDimArray


class Board:
	"""
	This class represents Tetris board.
	[0][0] coordinate represents upper left corner
	"""

	WIDTH = 10
	HEIGHT = 20

	#
	def __init__(self):
		"""
		Creates empty matrix with proper width and height
		"""

		self.matrix = TwoDimArray(self.WIDTH, self.HEIGHT)

	#
	def remove_full_rows_and_return_count(self):
		"""
		Removes full rows and adds empty rows at the top.

		:return: number of removed rows
		"""

		removed_rows = 0

		for y in range(self.HEIGHT):
			is_full = True

			for x in range(self.WIDTH):
				if self.matrix.get(x, y) != 0:
					continue
				else:
					is_full = False
					break

			if is_full:
				self.__remove_row(y)
				removed_rows += 1

		return removed_rows

	def is_top_row_empty(self):
		"""
		Checks if upper (first) row is empty

		:return: True - is empty / False - isn't empty
		"""

		is_empty = True

		for x in range(self.WIDTH):
			if self.matrix.get(x, 0) != 0:
				is_empty = False

		return is_empty

	def add_tetromino(self, tetromino: Tetromino, x_position):
		"""
		Places new tetromino on board.

		:param tetromino: tetromino which will be placed
		:param x_position: index of column for tetromino's first block (from left) <0,9>
			(if it doesn't fit it will be move to the left)
		:return:
		"""

		if (x_position + (tetromino.width - 1)) >= self.WIDTH:  # we are outside the board bounds (right)
			x_position = self.WIDTH - 1 - (tetromino.width - 1)
		elif x_position < 0:  # we are outside the board bounds (left)
			x_position = 0

		self.__place_tetromino(tetromino, x_position)

	def print(self):
		self.matrix.print()

	def get_situation(self):
		"""
		Returns BitArray representing situation in top rows which contain tetrominoes

		rows:
			0: K L M N O P R S T U
			1: A B C D E F G H I J
			   0 1 2 3 4 5 6 7 8 9

		situation:
			ABCDEFGHIJKLMNOPRSTU
			- bit array where each letter is 0 if there is no block on board in given place and 1 otherwise

		:return: BitArray representing situation (structured as in example above)
		"""

		width = self.WIDTH
		height = 2
		situation = BitArray(length=(width * height))
		i = 0  # for simplicity inside loops

		top_rows = self.__get_top_two_rows()
		for y in range(height - 1, -1, -1):
			for x in range(width):
				if top_rows.get(x, y) != 0:
					situation[i] = 1

				i += 1

		return situation

	#
	def __get_top_two_rows(self):
		"""
		This method finds first two rows in which tetrominoes occur (looking from top) and returns them

		:return: TwoDimArray object representing first two rows with tetrominoes
		"""

		top_row = 0
		has_found = False

		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				if self.matrix.get(x, y) != 0:
					top_row = y
					has_found = True
					break

			if has_found:
				break

		if top_row == self.HEIGHT - 1:
			top_row = self.HEIGHT - 2

		return self.matrix.get_rows(top_row, top_row + 2)

	def __remove_row(self, row_num):
		"""
		Removes specified row, lowers each row from above, and adds new empty row on top
		:param row_num: index of row which will be removed
		"""

		for i in range(row_num, -1, -1):
			if i == 0:
				self.matrix.set_row(i, zeros(self.WIDTH, dtype=int))
			else:
				self.matrix.set_row(i, self.matrix.get_row(i - 1))

	def __is_row_full(self, row_num):
		"""
		Checks if given row is fully occupied (there is no empty space)
		:param row_num: index of row to check
		:return: True - row is fully occupied / False - row isn't fully occupied
		"""

		is_row_occupied = True
		for x in range(self.WIDTH):
			if self.matrix.get(x, row_num) == 0:
				is_row_occupied = False
				break

		return is_row_occupied

	def __place_tetromino(self, tetromino: Tetromino, x_position):
		"""
		Takes first row in which tetromino can be placed and adds it to the board

		:param tetromino: Tetromino object which should be placed
		:param x_position: position of tetromino's left coordinate
		:return:
		"""

		first_empty_row = self.__get_first_empty_row(tetromino, x_position)

		for y in range((tetromino.height - 1), -1, -1):  # iterate through tetromino from top to bottom
			for x in range(tetromino.width):  # iterate through tetromino from left to right
				if tetromino.get(x, y) != 0:  # if it's not empty place it on board
					board_x = x_position + x
					board_y = first_empty_row - (tetromino.height - 1) + y
					self.matrix.set(board_x, board_y, tetromino.get(x, y))

	def __get_first_empty_row(self, tetromino: Tetromino, x_position):
		"""
		Returns index of first empty row (first row in which tetromino can be placed)

		:param tetromino: given Tetromino
		:param x_position: position of tetromino's left coordinate
		:return: index of first row in which tetromino can be placed
		"""

		first_non_empty_row = 0
		columns: TwoDimArray = self.matrix.get_columns(x_position, x_position + tetromino.width)

		can_move: bool = True
		while (first_non_empty_row < self.HEIGHT) and can_move:  # we iterate through columns from top to bottom

			if columns.is_row_empty(first_non_empty_row):  # if current row is empty go row below
				if can_move and (first_non_empty_row + 1 <= self.HEIGHT):
					first_non_empty_row += 1
					continue
				else:
					break
			elif self.__is_row_full(first_non_empty_row):
				break

			for y in range((tetromino.height - 1), -1, -1):  # iterate through tetromino from bottom to top
				if not can_move or not (first_non_empty_row < self.HEIGHT):
					break

				for x in range(tetromino.width):  # iterate through tetromino from left to right
					if not can_move or not (first_non_empty_row < self.HEIGHT):
						break

					if tetromino.get(x, y) == 0:
						continue  # continue if current tetromino's block is empty
					else:
						if columns.get(x, first_non_empty_row) == 0:
							continue  # continue if tetromino's block isn't empty, but column's is
						else:
							can_move = False

				if can_move and (first_non_empty_row + 1 <= self.HEIGHT):
					first_non_empty_row += 1  # add one row since we are moving one up
				else:
					break

			if can_move and (first_non_empty_row + 1 <= self.HEIGHT):
				first_non_empty_row += 1
			else:
				break

		return first_non_empty_row - 1
