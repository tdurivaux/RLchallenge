from ple.games.flappybird import FlappyBird
from ple import PLE
import numpy as np
from FlappyAgent import FlappyPolicy
import time
game = FlappyBird(graphics="fixed") # use "fancy" for full background, random bird color and random pipe color, use "fixed" (default) for black background and constant bird and pipe colors.
p = PLE(game, fps=30, frame_skip=1, num_steps=1, force_fps=True, display_screen=True)
# Note: if you want to see you agent act in real time, set force_fps to False. But don't use this setting for learning, just for display purposes.

p.init()
reward = 0.0

nb_games = 100
cumulated = np.zeros((nb_games))

for i in range(nb_games):
    p.reset_game()

    while(not p.game_over()):
        state = game.getGameState()
        screen = p.getScreenRGB()
        action=FlappyPolicy(state, screen)

        reward = p.act(action)
        cumulated[i] = cumulated[i] + reward
    print("{}\t{}\t{:.1f}".format(i, int(cumulated[i]), np.mean(cumulated[:i+1])))

average_score = np.mean(cumulated)
max_score = np.max(cumulated)
print()
print("Average: {:.2f}\t Max: {:.0f}".format(average_score, max_score))