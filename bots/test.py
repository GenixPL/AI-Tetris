from bots.genes import Genes
import files.file_functions as ff
from bitstring import BitArray
from bots.bot import Bot

# gene = Genes.get_random()
# print("gene bin: " + str(len(gene.chromosomes.bin)))
# print("gene: " + str(gene.chromosomes[:25]))
#
# ff.write_to_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\test.txt", gene.chromosomes.hex)
#
# data = ff.read_from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\test.txt")
#
# s = "0x" + str(data)
# print("data: " + str(s[:100]))
# i = int(s, 16)
#
# new = Genes()
#
# arr = BitArray(uint=i, length=gene.CHROMOSOME_LEN)
# new.chromosomes = arr
#
# print("gene bin: " + str(len(new.chromosomes.bin)))
# print("gene: " + str(new.chromosomes[:25]))
# ff.write_to_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\test2.txt", arr.hex)
#
# # for i in range(len(new.chromosomes)):
# # 	if new.chromosomes[i] != gene.chromosomes[i]:
# # 		print("ERR")
#
# sit = BitArray('0b00001111000011110000')
# print(gene.get_rotation(sit, 3))
# print(new.get_rotation(sit, 3))

# data4 = ff.read_from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-4.txt")
# data5 = ff.read_from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-4.txt")
#
# s4 = "0x" + str(data4)
# i4 = int(s4, 16)
# new4 = Genes()
# arr4 = BitArray(uint=i4, length=new4.CHROMOSOME_LEN)
#
# s5 = "0x" + str(data5)
# i5 = int(s5, 16)
# new5 = Genes()
# arr5 = BitArray(uint=i5, length=new5.CHROMOSOME_LEN)
#
# print(str(arr5.len) + " " + str(arr4.len))
# print(arr4[:25])
# print(arr5[:25])
#
# bot4 = Bot.from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-4.txt")
# bot5 = Bot.from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-4.txt")
#
# print(str(bot4.gene.chromosomes.len) + " " + str(bot5.gene.chromosomes.len))
# print(bot4.gene.chromosomes[:25])
# print(bot5.gene.chromosomes[:25])

# for i in range(0, len(arr4), 2):
# 	if bot4[i] != arr5[i]:
# 		print("ERR" + str(i))


best1 = Bot.from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-1.txt")
best2 = Bot.from_file("C:\\Users\\lnied\Projects\\tetris-ai\\files\logs\\best-2.txt")

print(str(best1.gene.chromosomes.len) + " " + str(best2.gene.chromosomes.len))

for i in range(0, len(best1.gene.chromosomes.hex), 2):
	if best1.gene.chromosomes.hex[i] != best2.gene.chromosomes.hex[i]:
		print(str(i) + ": " + str(best1.gene.chromosomes.hex[i]) + " " + str(best2.gene.chromosomes.hex[i]))
