from random import randint

from numpy import array

shapes = [  # Define the shapes of the single parts
	array([  # 0
		[1, 1, 1],
		[0, 1, 0]
	], dtype=int),

	array([  # 1
		[0, 2, 2],
		[2, 2, 0]
	], dtype=int),

	array([  # 2
		[3, 3, 0],
		[0, 3, 3]
	], dtype=int),

	array([  # 3
		[4, 0, 0],
		[4, 4, 4],
	], dtype=int),

	array([  # 4
		[0, 0, 5],
		[5, 5, 5],
	], dtype=int),

	array([  # 5
		[6, 6, 6, 6],
	], dtype=int),

	array([  # 6
		[7, 7],
		[7, 7]
	], dtype=int)
]


class Tetromino:

	@classmethod
	def get_random(cls):
		"""
		Creates new Tetromino with random shape
		:return: new Tetromino object with random shape
		"""

		num = randint(0, 6)

		return Tetromino(num)

	def __init__(self, shape_num):
		"""
		Creates new object with given shape.

		:param shape_num: number representing shape from shapes array
		"""

		self.shape_num = shape_num
		self.shape = shapes[shape_num].copy()
		self.width = len(self.shape[0])
		self.height = len(self.shape)

	def rotate(self, times=1):
		"""
		Rotates tetromino (clockwise).

		:param times: number of times tetromino will be rotated
		"""

		for i in range(times):
			self.shape = [[self.shape[y][x] for y in range(self.height)] for x in range(self.width - 1, -1, -1)]
			self.width = len(self.shape[0])
			self.height = len(self.shape)

	def get(self, pos_x: int, pos_y: int):
		"""
		Returns number representing block under (x, y) coordinate.

		:param pos_x: x coordinate of block
		:param pos_y: y coordinate of block
		:return: int number presenting block
		"""

		return self.shape[pos_y][pos_x]
