from Displays import Displays
from Turn import Turn
from enum import Enum, auto


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one  # enforces string on player name
        self.player_two = player_two
        self.max_score = 50


    def pig(self):

        print(f"\n\n{self.player_one.username}")
        input("Continue...")
        playing = self.player_turn(Turn.player_turn(self.player_one, self.max_score), self.player_one)

        if playing != GameOptions.PLAYING:
            return None

        print(f"\n\n{self.player_two.username}")
        playing = self.player_turn(Turn.player_turn(self.player_two, self.max_score), self.player_two)

        if playing != GameOptions.PLAYING:
            return None

        Game.pig(self)


    def player_turn(self, game_option, player):
        match game_option:
            case GameOptions.CHEAT:
                print("Cheater...")
                player.score = input("input score: ")

            case GameOptions.ENDTURN:
                self.reset_turn(player)
                return GameOptions.PLAYING

            case GameOptions.WIN:
                self.reset_turn(player)
                self.reset()
                Displays.print_win(player)
                input("Continue...")

            case GameOptions.QUIT:
                self.reset_turn(player)
                self.reset()




    @staticmethod
    def reset_turn(player):
        player.running_score = 0


    def reset(self):
        self.player_one.resetGame()
        self.player_two.resetGame()


class GameOptions(Enum):
    WIN = auto()
    QUIT = auto()
    ENDTURN = auto()
    PLAYING = auto()
    CHEAT = auto()

