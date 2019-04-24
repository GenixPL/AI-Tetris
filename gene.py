from bitstring import BitArray
from random import randint
from file_functions import read_from_file
from tetromino import Tetromino


class Gene:
	"""
	This class is responsible for abstracting and taking care of genes.

	The idea behind gene array is that it consists of bits representing reactions to different situations on board.
		We have 1,048,576 possible situations on board (in upper two rows with tetrominoes) and 7 different tetromino
		types. We have to choose position and number of rotations of tetromino for each situation. We have 4 possible
		rotations and 7 possible tetromino shapes.
	Array will be constructed in such a way, that:
		42 bits will represent all possible reaction to given situations on board
			42b = 6b * 7
			6b = 2b for rotation + 4b for position
			7 is a number of possible tetrominoes

		and the whole array will have 44,040,192 bits = 5.25 MB
			42 * 1,048,576
			42 possible reaction to each situations
			1,048,576 situations
	"""

	# number of possible different situations in first two rows in which tetrominoes are <0,10448575>
	situations_num: int = 1048576
	# number of possible tetromino rotations <0,3>
	rotations_num: int = 4
	# number of possible different tetrominoes <0,6>
	tetrominoes_num: int = 7
	# number of possible positions for x coordinate of left tetromino's side <0,9>
	positions_num: int = 10

	rotations_bits: int = 2  # number of bits needed to encode possible rotations
	positions_bits: int = 4  # number of bits needed to encode possible positions
	situation_bits: int = (rotations_bits + positions_bits) * tetrominoes_num

	GENE_LEN = situation_bits * situations_num

	@classmethod
	def get_random(cls):
		new = Gene()
		init = randint(0, 2**44040192 - 1)
		new.gene = BitArray(uint=init, length=cls.GENE_LEN)

		return new

	@classmethod
	def from_file(cls, file):
		new = Gene()
		data = read_from_file(file)
		init = int(data, 16)
		new.gene = BitArray(uint=init, length=cls.GENE_LEN)

		return new

	def __init__(self):
		self.gene = BitArray(length=self.GENE_LEN)

	def get_reactions(self, situation: BitArray):
		situation_int = situation.uint

		starting_point = situation_int * self.situation_bits
		ending_point = starting_point + self.situation_bits

		return self.gene[starting_point:ending_point]

	def get_rotations(self, reactions: BitArray, tetromino: Tetromino):
		starting_point = (self.rotations_bits + self.positions_bits) * tetromino.shape_num
		ending_point = starting_point + 2

		return reactions[starting_point:ending_point].uint

	def get_position(self, reactions: BitArray, tetromino: Tetromino):
		starting_point = (self.rotations_bits + self.positions_bits) * tetromino.shape_num + 2
		ending_point = starting_point + 4

		return reactions[starting_point:ending_point].uint % self.positions_num

	def get_index_for_situation_and_tetromino(self, situation: int, tetromino: int):
		return (situation * self.situation_bits) + (tetromino * (self.rotations_bits + self.positions_bits))
