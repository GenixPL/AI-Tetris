from numpy import zeros


class TwoDimArray:
	"""
	Base class representing two-dimensional int array.
	"""

	@classmethod
	def from_matrix(cls, matrix):
		"""
		Creates TwoDimArray from specified matrix
		:param matrix: matrix for which new object will be created
		:return: new TwoDimArray object containing specified matrix
		"""

		width = len(matrix[0])
		height = len(matrix)
		new = TwoDimArray(width, height)
		new.matrix = matrix

		return new

	def __init__(self, width, height):
		"""
		Creates new two-dimensional array, with given width and height, of zeros
		:param width: width of new array
		:param height: height of new array
		"""

		self.matrix = zeros([height, width], dtype=int)
		self.width = width
		self.height = height

	def set(self, pos_x, pos_y, value):
		"""
		Sets value and abstracts matrix [row][column] notation to regular coordinate (x, y) notation
		:param pos_x: x coordinate
		:param pos_y: y coordinate
		:param value: new value
		"""

		self.matrix[pos_y][pos_x] = value

	def get(self, pos_x, pos_y):
		"""
		Returns value and abstracts matrix [row][column] notation to regular coordinate (x, y) notation
		:param pos_x: x coordinate
		:param pos_y: y coordinate
		:return: value from matrix under x and y coordinates
		"""

		return self.matrix[pos_y][pos_x]

	def get_row(self, row_num):
		"""
		Returns copy of row with specified index
		:param row_num: index of row which should be returned
		:return: int array representing row
		"""

		return self.matrix[row_num].copy()

	def get_columns(self, first, last):
		"""
		Returns copy of columns from first to last (excluding)

		:param first: first column to take
		:param last: column after last to take (first which won't be returned)
		:return: Board object representing given columns
		"""

		return TwoDimArray.from_matrix(self.matrix[:, first:last])

	def get_rows(self, first, last):
		"""
		Returns copy of rows from first to last (excluding)

		:param first: first row to take
		:param last: row after last to take (first which won't be returned)
		:return: Board object representing given rows
		"""

		return TwoDimArray.from_matrix(self.matrix[first:last, :])

	def set_row(self, row_num, new_row):
		"""
		Sets new_row as row with specified index
		:param row_num: index of row which will be changed
		:param new_row: int array representing row which will be placed inside matrix
		"""

		self.matrix[row_num] = new_row.copy()

	def is_row_empty(self, row_num):
		is_empty = True

		for x in range(self.width):
			if self.get(x, row_num) != 0:
				is_empty = False

			if not is_empty:
				break

		return is_empty

	def print(self):
		"""
		Prints matrix, with row numbers, in console
		"""

		for y in range(self.height):
			print(str(y) + "\t" + str(self.matrix[y]))

