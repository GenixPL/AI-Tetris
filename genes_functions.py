from bitstring import BitArray
from two_dim_array import TwoDimArray


def get_situation(rows: TwoDimArray):
	"""
	This function takes rows and produces BitArray representing their situation

	rows:
		0: K L M N O P R S T U
		1: A B C D E F G H I J
		   0 1 2 3 4 5 6 7 8 9

	situation:
		ABCDEFGHIJKLMNOPRSTU
		- bit array where each letter is 0 if there is no block on board in given place and 1 otherwise

	:param rows: rows which situation will be taken
	:return: BitArray representing situation in given rows (structured as in example above)
	"""

	width = rows.width
	height = rows.height
	situation = BitArray(length=(width * height))
	i = 0  # for simplicity inside loops

	for y in range(height - 1, -1, -1):
		for x in range(width):
			if rows.get(x, y) != 0:
				situation[i] = 1

			i += 1

	return situation
