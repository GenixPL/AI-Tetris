from bots.population import Population
import file_functions as ff


# TODO: reduce bot creation time

log_file = ff.LOGS_DIR + "log1.txt"
best_file = ff.LOGS_DIR + "best1.txt"

# START
print("init starts")
population = Population()
print("init done")

i = 0
while True:
	population.examine()
	population.reduce()
	population.reset()
	population.reproduce()
	population.mutate()

	msg = "iteration: " + str(i) + " best: " + str(population.get_best_score()) + "\n"
	print(msg)
	ff.add_to_file(log_file, msg)
	ff.write_to_file(best_file, population.get_best_gene().chromosomes.hex)
	i += 1
