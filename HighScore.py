import pickle
import os
from Player import Player
from HumanPlayer import HumanPlayer


class highscore:

    def __init__(self):

        self.allPlayerList = []
        self.filepath = "players_highscores.pkl"

        # Added this so if the list is not empty, it loads. Must be loaded once only, at the very beginning.
        if os.path.getsize(self.filepath) > 0:
            self.allPlayerList = self.load_scores()


    def add_player_to_list(self, player):
        self.allPlayerList.append(player)


    def save_scores(self):
        with open(self.filepath, "wb") as playerFile:
            pickle.dump(self.allPlayerList, playerFile)


    def load_scores(self):
        try:
            with open(self.filepath, "rb") as playerFile:
                self.allPlayerlist = pickle.load(playerFile)

        except FileNotFoundError:
            print(f"File not found: {self.filepath}. ")
            return []


    def display_scores(self):
        try:
            self.allPlayerList.sort(key=lambda player: player.turns)
            for player in self.allPlayerList:
                print(f"Player name:  {player.name}, Ammount of turns: {player.turns}")

        except TypeError:
            print("The player list is not properly defined.")

