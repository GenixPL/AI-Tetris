from bot import Bot

BOTS_NUM = 100
bots = []


def initialize():
	for i in range(BOTS_NUM):
		bots.append(Bot())


def play():
	for i in range(BOTS_NUM):
		bots[i].examine()


def sort_bots():
	bots.sort(key=lambda x: x.game.get_score(), reverse=True)


def remove_worst():
	del bots[50:-1]


def reset_bots():
	for i in range(50):
		bots[i].prepare()


def add_new_bots():
	for i in range(50):
		bots.append(bots[0].get_mutated())


# START
initialize()

while True:
	play()
	sort_bots()
	remove_worst()
	reset_bots()
	add_new_bots()

	print("best: " + str(bots[0].game.get_score()))

