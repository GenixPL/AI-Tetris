from bots.population import Population
import file_functions as ff

# TODO: reduce bot creation time
# TODO: maybe the tetrominoes shouldn't spawn randomly during early stage of learning
# TODO: maybe removing 90% of bots and reproducing them with many mutated copies of best ones will be better
# TODO: add messages to log files
# TODO: add auto increase log file number
# TODO: we can divide chromosome to imaginary e.g. 10 parts and take 5 from one parent and 5 from second
#  (randomly chosen, this should give us better diversity)
# TODO: maybe in case of constant tetro spawn removing evry bot except best and mutating the best will give better results

log_file = ff.LOGS_DIR + "log7.txt"
best_file = ff.LOGS_DIR + "best7.txt"

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
	# population.mutate()  # 2nd version

	msg = "iteration: " + str(i) + " best: " + str(population.get_best_score()) + "\n"
	print(msg)
	ff.add_to_file(log_file, msg)
	ff.write_to_file(best_file, population.get_best_gene().chromosomes.hex)
	i += 1
