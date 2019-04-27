from bots.bot import Bot
from file_functions import get_bots_number_from_config, get_mutation_chance
from random import randint
from board.tetromino import Tetromino


class Population:

	# TODO: init from prev bot
	# TODO: add threads

	def __init__(self):
		self.bots_num = get_bots_number_from_config()
		self.bots = []

		for i in range(self.bots_num):
			self.bots.append(Bot())

	#
	def examine(self):
		for i in range(len(self.bots)):
			# TODO:
			Tetromino.i = 0
			self.bots[i].examine()

	def get_best_score(self):
		return self.bots[0].get_score()

	def get_best_gene(self):
		return self.bots[0].gene.copy()

	def reduce(self):
		self.__sort_bots()
		# del self.bots[int((len(self.bots) / 2)):]  # TODO: make it better
		del self.bots[1:]  # 2nd version

	def reproduce(self):
		# TODO: make it better

		# starting_bots_num = len(self.bots)
		# for i in range(int(starting_bots_num / 2)):
		# 	self.bots.append(Bot.create_child(self.bots[i * 2], self.bots[(2 * i) + 1]))
		# 	self.bots.append(Bot.create_child(self.bots[i * 2], self.bots[(2 * i) + 1]))

		for i in range(self.bots_num - 1):  # 2nd version
			new = self.bots[0].copy()
			new.mutate()

			self.bots.append(new)

	def mutate(self):
		mutation_chance = get_mutation_chance()

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
