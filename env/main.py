from random import randint

from ludo import Ludo

game = Ludo()
game_state = game.initialize()

c = 0
while game_state is not None:
    print(game_state)
    game_state = game.step(randint(1, 4))
    c += 1

print(c)
