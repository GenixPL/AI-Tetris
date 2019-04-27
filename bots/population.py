from random import randint

from bots.bot import Bot
from files.config import get_bots_num, get_mutation_chance
from files.config import get_keep_only_best


class Population:

	# TODO: init from prev bot
	# TODO: add threads

	def __init__(self):
		self.bots_num = get_bots_num()
		self.bots = []

		for i in range(self.bots_num):
			self.bots.append(Bot())

	#
	def examine(self):
		for i in range(len(self.bots)):
			self.bots[i].examine()

	def get_best_score(self):
		return self.bots[0].get_score()

	def get_best_gene(self):
		return self.bots[0].gene.copy()

	def reduce(self):
		self.__sort_bots()

		if get_keep_only_best():
			del self.bots[1:]
		else:
			del self.bots[int((len(self.bots) / 2)):]

	def reproduce(self):
		if get_keep_only_best():
			for i in range(self.bots_num - 1):
				self.bots.append(self.bots[0].copy())

		else:
			starting_bots_num = len(self.bots)

			for i in range(int(starting_bots_num / 2)):
				self.bots.append(Bot.create_child(self.bots[i * 2], self.bots[(2 * i) + 1]))
				self.bots.append(Bot.create_child(self.bots[i * 2], self.bots[(2 * i) + 1]))

	def mutate(self):
		mutation_chance = get_mutation_chance()

		if get_keep_only_best():
			for i in range(1, len(self.bots)):  # we don't mutate the best in this case
				r = randint(0, 99)
				if r < mutation_chance:
					self.bots[i].mutate()

		else:
			for i in range(len(self.bots)):
				r = randint(0, 99)
				if r < mutation_chance:
					self.bots[i].mutate()

	def reset(self):
		for i in range(len(self.bots)):
			self.bots[i].reset()

	#
	def __sort_bots(self):
		self.bots.sort(key=lambda x: x.game.get_score(), reverse=True)  # TODO: check it
