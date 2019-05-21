from bots.population import Population
from files.config import init_new_session, add_log, save_best, get_spawn_random_tetrominoes
import random

# TODO: we can divide chromosome to imaginary e.g. 10 parts and take 5 from one parent and 5 from second
#  (randomly chosen, this should give us better diversity)
# TODO: init from file

init_new_session()

print("init starts")
population = Population()
print("init done")

i = 0
while True:
	if get_spawn_random_tetrominoes():
		population.examine(None)
	else:
		tetromino_seq = [random.randint(0, 6) for i in range(500)]
		population.examine(tetromino_seq.copy())

	population.reduce()
	population.reset()
	population.reproduce()
	population.mutate()

	msg = "\niteration: " + str(i) + " best: " + str(population.get_best_score())
	print(msg)
	add_log(msg)
	save_best(population.get_best_gene().chromosomes)

	i += 1

	if population.get_best_score() >= 10000000:
		break
