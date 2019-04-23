from board import BoardController

bc = BoardController()
bc.board.set(2, 19, 1)
bc.board.set(2, 18, 1)
# for x in range(bc.board.width):
# 	bc.board.set(x, 3, 3)
#
# for x in range(bc.board.width):
# 	# if x == 3:
# 	# 	continue
# 	bc.board.set(x, 4, 1)
#
# for x in range(bc.board.width):
# 	if x == 3:
# 		continue
# 	bc.board.set(x, 5, 1)

# bc.board.print()

bc.add_tetromino(1, 0, -5)
bc.board.print()
