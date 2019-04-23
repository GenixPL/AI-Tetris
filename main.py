from board import GameController
from random import randint

gc = GameController()
gc.board.set(2, 19, 1)
gc.board.set(2, 18, 1)

# for x in range(gc.board.width):
# 	if x > 2:
# 		gc.board.set(x, 18, 3)
#
#
# for x in range(gc.board.width):
# 	# if x == 3:
# 	# 	continue
# 	gc.board.set(x, 4, 1)
#
# for x in range(gc.board.width):
# 	if x == 3:
# 		continue
# 	gc.board.set(x, 5, 1)
#
# gc.board.print()
#
# gc.add_tetromino(1, 0, -5)
# gc.remove_full_rows()
# gc.add_tetromino(5, 1, 0)
#
# gc.board.print()
# gc.add_tetromino(1, 0, 5)
# gc.add_tetromino(2, 3, 5)
# gc.board.print()
#
# gc.board.print()
# print("top two")
# gc.board.get_top_two_rows().print()


while not gc.is_game_over:
	tetro = randint(0, 6)
	rot = randint(0, 3)
	pos = randint(0, 9)

	gc.add_tetromino(tetro, rot, pos)
	gc.remove_full_rows()

gc.board.print()
print("score: " + str(gc.score))
