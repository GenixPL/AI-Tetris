from game import Game
from genes.genes import Genes
from random import randint


class Bot:

	@classmethod
	def create_child(cls, first_bot, second_bot):
		"""
		Creates new bot from two parents, taking genes from first till random crossover point and from second
			from crossover point

		:param first_bot: Bot class representing first parent
		:param second_bot: Bot class representing second parent
		:return: new Bot object being child of two parents
		"""

		crossover_point = randint(0, Genes.CHROMOSOME_LEN)
		new = Bot()
		del new.gene.chromosomes[:]

		new.gene.chromosomes.append(first_bot.gene.chromosomes[0:crossover_point])
		new.gene.chromosomes.append(second_bot.gene.chromosomes[crossover_point:Genes.CHROMOSOME_LEN])

		return new

	def __init__(self):
		self.gene: Genes = Genes.get_random()
		self.game: Game = Game(self.gene)
		self.prev_score = 0

	def examine(self):
		self.game.play()
		self.prev_score = self.game.get_score()

	def reset(self):
		self.game.restart()

	def mutate(self):
		self.gene.mutate()

	def get_score(self):
		return self.prev_score

	def copy(self):
		new = Bot()
		new.gene = self.gene

		return new

