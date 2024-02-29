import pickle
import Player

class HighScore:
     
    def __init__(self):
        self.allPlayerList = []
        self.filepath = "players_highscores.pkl"
        self.load_scores()

    
    def add_player_to_list(self, player):
        self.allPlayerList.append(player)

  
    def save_scores (self):
        with open (self.filepath, "wb") as playerFile:               
            pickle.dump(self.allPlayerList, playerFile)

   
    def load_scores (self):
        try: 
            with open (self.filepath, "rb") as playerFile:
                self.allPlayerlist = pickle.load(playerFile)

        except FileNotFoundError:
             print(f"File not found: {self.filepath}. ")
            
    def displayScores(self, player):
        self.allPlayerList.sort(key = lambda player: player.turns)
        for player in self.allPlayerList:
            print(f"Player name:  {player.name}, Ammount of turns: {player.turns}")
