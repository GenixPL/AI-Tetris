from tetrominoes import Tetromino
import numpy as np


class Board:
	"""
	This class represents Tetris board. It can also be used to handle board sub parts
	[0][0] coordinate represents upper left corner
	TODO: if someone is bored, this can be moved to separate class and interface can be created

	"set" and "get" methods have been crated in order to be able to abstract
		matrix notation ([row, col]) to (x, y) notation
	"""

	def __init__(self, matrix=None, width=10, height=20):
		# width = 10 and height = 20 are standard Tetris board sizes
		if matrix is None:
			self.matrix = np.zeros([height, width], dtype=int)
			self.width = width
			self.height = height

		else:
			self.matrix = matrix
			self.width = len(matrix[0])
			self.height = len(matrix)

	def print(self):
		for y in range(self.height):
			print(str(y) + "\t" + str(self.matrix[y]))

	def set(self, pos_x, pos_y, value):
		self.matrix[pos_y][pos_x] = value

	def get(self, pos_x, pos_y):
		return self.matrix[pos_y][pos_x]

	def remove_row_and_add_empty(self, row_num):
		for i in range(row_num, -1, -1):
			if i == 0:
				self.matrix[i] = np.zeros(self.width, dtype=int)
			else:
				self.matrix[i] = self.matrix[i - 1]

	def get_columns(self, first_col, last_col):
		"""
		Returns columns from first to last (excluding)
		:param first_col: first column to take
		:param last_col: last column to take
		:return: Board object representing given columns
		"""

		return Board(matrix=self.matrix[:, first_col:last_col])

	def is_row_empty(self, row_num):
		"""
		Checks if given row is empty
		:param row_num: index of row to check
		:return: True - row is empty / False - row isn't empty
		"""

		is_row_empty = True
		for x in range(self.width):
			if self.get(x, row_num) != 0:
				is_row_empty = False
				break

		return is_row_empty

	def is_row_fully_occupied(self, row_num):
		"""
		Checks if given row is fully occupied
		:param row_num: index of row to check
		:return: True - row is fully occupied / False - row isn't fully occupied
		"""

		is_row_occupied = True
		for x in range(self.width):
			if self.get(x, row_num) == 0:
				is_row_occupied = False
				break

		return is_row_occupied

	def get_num_of_full_rows(self):
		"""
		Returns number of full rows
		:return: number of full rows
		"""
		full_rows = 0

		for y in range(self.height):
			is_full = True

			for x in range(self.width):
				if self.get(x, y) == 0:
					is_full = False
					break
				else:
					continue

			if is_full:
				full_rows += 1

		return full_rows


class BoardController:

	# TODO: check if new tetromino is not added to non-existing rows (above board)
	# TODO: get top 2 rows
	def __init__(self):
		self.board = Board()

	def remove_full_rows(self):
		"""
		Removes full rows and adds empty rows at the top
		:return: number of removed rows
		"""
		removed_rows = 0

		for y in range(self.board.height):
			is_full = True

			for x in range(self.board.width):
				if self.board.get(x, y) != 0:
					continue
				else:
					is_full = False
					break

			if is_full:
				self.board.remove_row_and_add_empty(y)
				removed_rows += 1

		return removed_rows

	def add_tetromino(self, shape_num, rotations_num, x_position):
		"""
		Places new tetromino on board.

		:param shape_num: index for tetrominoes.shapes <0,6>
		:param rotations_num: number of rotations for given tetromino <0,3>
		:param x_position: index of column for tetromino's first block (from left) <0,9>
			(if it doesn't fit it will be move to the left)
		:return:
		"""

		tetromino = Tetromino(shape_num)  # get tetromino with given shape

		for i in range(rotations_num):  # rotate given tetromino given number of times
			tetromino.rotate_clockwise()

		if (x_position + (tetromino.width - 1)) >= self.board.width:  # we are outside the board bounds (right)
			x_position = self.board.width - 1 - (tetromino.width - 1)
		elif x_position < 0:  # we are outside the board bounds (left)
			x_position = 0

		self.__place_tetromino(tetromino, x_position)

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
					self.board.set(board_x, board_y, tetromino.get(x, y))

	def __get_first_empty_row(self, tetromino: Tetromino, x_position):
		"""
		Returns index of first empty row (first row in which tetromino can be placed)
		:param tetromino: given Tetromino
		:param x_position: position of tetromino's left coordinate
		:return: index of first row in which tetromino can be placed
		"""

		first_non_empty_row = 0
		columns = self.board.get_columns(x_position, x_position + tetromino.width)

		can_move: bool = True
		while (first_non_empty_row < self.board.height) and can_move:  # we iterate through columns from top to bottom

			if self.board.is_row_empty(first_non_empty_row):  # if current row is empty go row below
				first_non_empty_row += 1
				continue
			elif self.board.is_row_fully_occupied(first_non_empty_row):
				break

			for y in range((tetromino.height - 1), -1, -1):  # iterate through tetromino from bottom to top
				if not can_move:
					break

				for x in range(tetromino.width):  # iterate through tetromino from left to right
					if not can_move:
						break

					if tetromino.get(x, y) == 0:
						continue  # continue if current tetromino's block is empty
					else:
						if columns.get(x, first_non_empty_row) == 0:
							continue  # continue if tetromino's block isn't empty, but column's is
						else:
							can_move = False

			if can_move:
				first_non_empty_row += 1

		return first_non_empty_row - 1
