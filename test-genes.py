from genes import GeneController
from bitstring import BitArray

gc = GeneController()
print(gc.gene)
print("len: " + str(gc.gene.len))

gc.gene.set(1, 1048576 * 42 - 1)
gc.gene.set(1, 1048576 * 42 - 1)

print()


genes = gc.get_situation_genes(BitArray('0b11111111111111111111'))
print(genes.bin)
print("len: " + str(genes.len))

situation0 = BitArray('0b0')
situation1 = BitArray('0b00000000000000000001')

gc.gene.set(0, gc.get_index_for_situation_and_tetromino(0, 0))
gc.gene.set(1, gc.get_index_for_situation_and_tetromino(0, 0) + 1)

gc.gene.set(1, gc.get_index_for_situation_and_tetromino(1, 1))
gc.gene.set(1, gc.get_index_for_situation_and_tetromino(1, 1) + 1)

gc.gene.set(1, gc.get_index_for_situation_and_tetromino(0, 1) + 2)
gc.gene.set(0, gc.get_index_for_situation_and_tetromino(0, 1) + 3)
gc.gene.set(0, gc.get_index_for_situation_and_tetromino(0, 1) + 4)
gc.gene.set(0, gc.get_index_for_situation_and_tetromino(0, 1) + 5)

gc.gene.set(1, gc.get_index_for_situation_and_tetromino(1, 3) + 2)
gc.gene.set(0, gc.get_index_for_situation_and_tetromino(1, 3) + 3)
gc.gene.set(0, gc.get_index_for_situation_and_tetromino(1, 3) + 4)
gc.gene.set(1, gc.get_index_for_situation_and_tetromino(1, 3) + 5)

situation0_genes = gc.get_situation_genes(situation0)
situation1_genes = gc.get_situation_genes(situation1)

rot = gc.get_rotations_num_for_situation_and_tetromino(situation0_genes, 0)
rot2 = gc.get_rotations_num_for_situation_and_tetromino(situation1_genes, 1)
print("rot: " + str(rot))
print("rot2: " + str(rot2))

pos = gc.get_position_for_situation_and_tetromino(situation0_genes, 1)
pos1 = gc.get_position_for_situation_and_tetromino(situation1_genes, 3)
print("pos: " + str(pos))
print("pos1: " + str(pos1))

