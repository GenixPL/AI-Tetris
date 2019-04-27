from random import randint

from bitstring import BitArray

from files.file_functions import read_from_file
from files.config import get_mutations_num

class Genes:
	"""
	This class is responsible for abstracting and taking care of genes.

	The idea behind chromosome array is that it consists of bits representing reactions to different situations on board.
		We have 1,048,576 possible situations on board (in upper two rows with tetrominoes) and 7 different tetromino
		types. We have to choose position and number of rotations of tetromino for each situation. We have 4 possible
		rotations and 7 possible tetromino shapes.
		Array will be constructed in such a way, that:
			42 bits will represent all possible reactions to given situations on board
				42b = 6b * 7
				6b = 2b for rotation + 4b for position
				7 is a number of possible tetrominoes

			and the whole array will have 44,040,192 bits = 5.25 MB
				42 * 1,048,576
				42 possible reaction to each situations
				1,048,576 situations
	"""

	# number of possible different situations in first two rows in which tetrominoes are <0,10448575>
	SITUATIONS_NUM: int = 1048576
	# number of possible tetromino rotations <0,3>
	ROTATIONS_NUM: int = 4
	# number of possible different tetrominoes <0,6>
	TETROMINOES_NUM: int = 7
	# number of possible positions for x coordinate of left tetromino's side <0,9>
	POSITIONS_NUM: int = 10

	# number of bits needed to encode possible rotations
	ROTATION_BITS_LEN: int = 2
	# number of bits needed to encode possible positions
	POSITION_BITS_LEN: int = 4
	# number of bits needed to encode possible reactions to given tetromino in given situation
	TETROMINO_BITS_LEN: int = ROTATION_BITS_LEN + POSITION_BITS_LEN
	# number of bits needed to encode possible reactions to all tetrominoes in given situation
	SITUATION_BITS_LEN: int = TETROMINO_BITS_LEN * TETROMINOES_NUM

	# length of the whole chromosome
	CHROMOSOME_LEN: int = SITUATION_BITS_LEN * SITUATIONS_NUM

	# used to init random chromosome
	MAX_INT_REPRESENTING_CHROMOSOME = (2 ** (SITUATIONS_NUM * SITUATION_BITS_LEN)) - 1

	#
	@classmethod
	def get_random(cls):
		"""
		Creates new Gene with random chromosome.

		:return: new Gene object with random chromosome
		"""

		new = Genes()
		init = randint(0, cls.MAX_INT_REPRESENTING_CHROMOSOME)
		new.chromosomes = BitArray(uint=init, length=cls.CHROMOSOME_LEN)

		return new

	@classmethod
	def from_file(cls, file: str):
		"""
		Creates new Gene with chromosome read from file.

		:param file: path to file from which chromosome will be read
		:return: new Gene object with chromosome read from file
		"""

		new = Genes()
		data = read_from_file(file)
		init = int(data, 16)
		new.chromosomes = BitArray(uint=init, length=cls.CHROMOSOME_LEN)

		return new

	def __init__(self):
		"""
		Creates new Gene object with chromosome composed of zeros and with proper length.
		"""

		self.chromosomes = BitArray(length=self.CHROMOSOME_LEN)

	def copy(self):
		"""
		Returns new Gene object being copy of self
		:return: new Gene object
		"""

		new = Genes()
		new.chromosomes = self.chromosomes.copy()

		return new

	#
	def get_rotation(self, situation: BitArray, tetromino_num: int):
		"""
		Returns number of rotations for given tetromino in given situation

		:param situation: BitArray object representing situation in two upper rows with tetrominoes
		:param tetromino_num: int representing number of shape of tetromino
		:return: int representing number of rotations for given tetromino in given situation
		"""

		reaction = self.__get_reaction(situation, tetromino_num)

		starting_point = 0
		ending_point = self.ROTATION_BITS_LEN

		return reaction[starting_point:ending_point].uint

	def get_position(self, situation: BitArray, tetromino_num: int):
		"""
		Returns position for given tetromino in given situation

		:param situation: BitArray object representing situation in two upper rows with tetrominoes
		:param tetromino_num: int representing number of shape of tetromino
		:return: int representing position for given tetromino in given situation
		"""

		reaction = self.__get_reaction(situation, tetromino_num)

		starting_point = self.ROTATION_BITS_LEN
		ending_point = starting_point + self.POSITION_BITS_LEN

		return reaction[starting_point:ending_point].uint % self.POSITIONS_NUM

	def mutate(self):
		"""
		Mutates chromosome by taking random number of mutations (0, max number of mutation from config) and
			mutating random rotation and other random position given number of times
		"""

		max_mutations_num = get_mutations_num()
		mutations_num = randint(0, max_mutations_num)

		for i in range(mutations_num):
			self.__mutate_rotation(Genes.__get_situation_from_number(randint(0, self.SITUATIONS_NUM - 1)))
			self.__mutate_position(Genes.__get_situation_from_number(randint(0, self.SITUATIONS_NUM - 1)))

	#
	@staticmethod
	def __get_situation_from_number(situation_num: int):
		"""
		Creates BitArray object representing situation from int representing situation
		TODO: "Situation" should be moved to separate class

		:param situation_num: int representing situation
		:return: new BitArray object representing situation
		"""

		return BitArray(uint=situation_num, length=20)

	def __set_rotation(self, situation: BitArray, tetromino_num: int, rotations_num: int):
		"""
		Sets number of rotations for given tetromino in given situation.

		:param situation: situation in which tetromino's number of rotations will be set
		:param tetromino_num: number representing shape of tetromino
		:param rotations_num: number of rotations
		"""

		if rotations_num > 3:
			raise ValueError("Rotations are in range <0, 3>, not " + str(rotations_num))

		first_rotation_index = self.__get_reaction_index(situation, tetromino_num)

		if rotations_num == 0:
			self.chromosomes[first_rotation_index] = 0
			self.chromosomes[first_rotation_index + 1] = 0
		elif rotations_num == 1:
			self.chromosomes[first_rotation_index] = 0
			self.chromosomes[first_rotation_index + 1] = 1
		elif rotations_num == 2:
			self.chromosomes[first_rotation_index] = 1
			self.chromosomes[first_rotation_index + 1] = 0
		elif rotations_num == 3:
			self.chromosomes[first_rotation_index] = 1
			self.chromosomes[first_rotation_index + 1] = 1

	def __set_position(self, situation: BitArray, tetromino_num: int, position: int):
		"""
		Sets position for given tetromino in given situation.

		:param situation: situation in which tetromino's position will be set
		:param tetromino_num: number representing shape of tetromino
		:param position: int representing position
		"""

		if position > 9:
			raise ValueError("Positions are in range <0, 9>, not " + str(position))

		first_position_index = self.__get_reaction_index(situation, tetromino_num) + self.ROTATION_BITS_LEN

		if position == 0:
			self.chromosomes[first_position_index] = 0
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 0
		elif position == 1:
			self.chromosomes[first_position_index] = 1
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 0
		elif position == 2:
			self.chromosomes[first_position_index] = 0
			self.chromosomes[first_position_index + 1] = 1
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 0
		elif position == 3:
			self.chromosomes[first_position_index] = 1
			self.chromosomes[first_position_index + 1] = 1
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 0
		elif position == 4:
			self.chromosomes[first_position_index] = 0
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 1
			self.chromosomes[first_position_index + 3] = 0
		elif position == 5:
			self.chromosomes[first_position_index] = 1
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 1
			self.chromosomes[first_position_index + 3] = 0
		elif position == 6:
			self.chromosomes[first_position_index] = 0
			self.chromosomes[first_position_index + 1] = 1
			self.chromosomes[first_position_index + 2] = 1
			self.chromosomes[first_position_index + 3] = 0
		elif position == 7:
			self.chromosomes[first_position_index] = 1
			self.chromosomes[first_position_index + 1] = 1
			self.chromosomes[first_position_index + 2] = 1
			self.chromosomes[first_position_index + 3] = 0
		elif position == 8:
			self.chromosomes[first_position_index] = 0
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 1
		elif position == 9:
			self.chromosomes[first_position_index] = 1
			self.chromosomes[first_position_index + 1] = 0
			self.chromosomes[first_position_index + 2] = 0
			self.chromosomes[first_position_index + 3] = 1

	def __mutate_rotation(self, situation: BitArray):
		"""
		Mutates random rotation for given situation

		:param situation: BitArray representing situation
		"""

		tetromino_to_mutate = randint(0, 6)
		prev_rotation = self.get_rotation(situation, tetromino_to_mutate)
		new_rotation = (prev_rotation - 1) % self.ROTATIONS_NUM
		self.__set_rotation(situation, tetromino_to_mutate, new_rotation)

	def __mutate_position(self, situation: BitArray):
		"""
		Mutates random position for given situation

		:param situation: BitArray representing situation
		"""

		tetromino_to_mutate = randint(0, 6)
		prev_position = self.get_rotation(situation, tetromino_to_mutate)
		new_position = (prev_position - 1) % self.POSITIONS_NUM
		self.__set_position(situation, tetromino_to_mutate, new_position)

	def __get_reaction(self, situation: BitArray, tetromino_num: int):
		starting_index = self.__get_reaction_index(situation, tetromino_num)
		ending_index = starting_index + self.TETROMINO_BITS_LEN

		return self.chromosomes[starting_index:ending_index]

	def __get_reaction_index(self, situation: BitArray, tetromino_num: int):
		situation_int = situation.uint

		return (situation_int * self.SITUATION_BITS_LEN) + (tetromino_num * self.TETROMINO_BITS_LEN)
