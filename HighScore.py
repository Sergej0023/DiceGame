import pickle

class HighScore:
    def __init__(self):
        self.all_player_list = []

    @staticmethod
    def add_player_to_list(player, all_player_list):
        all_player_list.append(player)
   
    @staticmethod  
    def save_scores (self, player, filepath = "players_highscores.pkl"):
        self.all_player_list.sort(key = lambda player: player.turns)    # sorting player depending on their turns
        with open (filepath, "wb") as player_file:                      # dumping into binary file
            pickle.dump(self.all_player_list, player_file)

    @staticmethod
    def load_scores (self, filepath = "players_highscores.pkl"):
        with open (filepath, "rb") as player_file:  
            