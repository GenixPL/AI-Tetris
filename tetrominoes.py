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

	def __init__(self, shape_num):
		self.shape = shapes[shape_num].copy()
		self.width = len(self.shape[0])
		self.height = len(self.shape)

	def rotate_clockwise(self):
		self.shape = [[self.shape[y][x] for y in range(self.height)] for x in range(self.width - 1, -1, -1)]
		self.width = len(self.shape[0])
		self.height = len(self.shape)

	def get(self, pos_x, pos_y):
		return self.shape[pos_y][pos_x]
