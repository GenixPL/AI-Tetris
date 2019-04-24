from gene import Gene
from game import Game


gene = Gene.get_random()

game = Game(gene)
game.play()


