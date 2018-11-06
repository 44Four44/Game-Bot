from Game import *
roblox = Game()
ai = Bot(roblox)
roblox.new(1)

for i in range (0, 100):
    roblox.new_player('random')

roblox.run()


