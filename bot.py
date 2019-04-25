from gene import Gene
from game import Game


class Bot:

	def __init__(self):
		self.gene = Gene.get_random()
		self.game = Game(self.gene)

	def examine(self):
		self.game.play()

	def prepare(self):
		self.game.restart()

	def get_mutated(self):
		new = Bot()
		new.gene = self.gene.copy()
		new.gene.mutate()

		return new
