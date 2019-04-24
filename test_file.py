import file_functions as ff
from genes import Gene

file = ff.LOGS_DIR + "gene.txt"
# ff.write_to_file(file, str(Gene(random=True).gene.hex))

g1 = Gene(random=True)
ff.write_to_file(file, g1.gene.hex)
g2 = Gene(file=file)


print(g1.gene.hex[-40:-1])
print(g2.gene.hex[-40:-1])


