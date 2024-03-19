class Game:
    def get_name(self):
        pass

    def get_type(self):
        pass

    def get_min_number_of_players(self):
        pass

    def get_max_number_of_players(self):
        pass

    def can_be_played_remotely(self):
        pass


class BoardGame(Game):
    def __init__(self, name, type, min_player_num, max_player_num):
        self._name = name
        self._type = type
        self._min_player_num = min_player_num
        self._max_player_num = max_player_num

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return self._min_player_num

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False

    def __str__(self):
        return f"BoardGame: name='{self._name}', type='{self._type}'"


class PCGame(Game):
    def __init__(self, name, type, min_player_num, max_player_num, is_online):
        self._name = name
        self._type = type
        self._min_player_num = min_player_num
        self._max_player_num = max_player_num
        self._is_online = is_online

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return self._min_player_num

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return self._is_online

    def __str__(self):
        return f"PCGame: name='{self._name}', type='{self._type}'"


class GameFactory:
    def create(self):
        pass


class MonopolyGameCreator(GameFactory):
    def create(self):
        return BoardGame("Monopoly", "Family game", 2, 4)


class ValorantGameCreator(GameFactory):
    def create(self):
        return PCGame("Valorant", "FPS", 4, 10, True)


class SettlersGameCreator(GameFactory):
    def create(self):
        return BoardGame("Settlers", "Family game", 3, 4)


class HeroesGameCreator(GameFactory):
    def create(self):
        return PCGame("Heroes", "Strategy", 1, 8, True)


def main():
    game_type = input("Enter the type of game [PC, Board]: ")
    game_factory = None
    if game_type == "PC":
        pc_game_type = input("Select type Valorant or Heroes [V, H]: ")
        if pc_game_type == "V":
            game_factory = ValorantGameCreator()
        elif pc_game_type == "H":
            game_factory = HeroesGameCreator()
    elif game_type == "Board":
        board_game_type = input("Select type Monopoly or Settlers [M, S]: ")
        if board_game_type == "M":
            game_factory = MonopolyGameCreator()
        elif board_game_type == "S":
            game_factory = SettlersGameCreator()

    if game_factory:
        game = game_factory.create()
        print(game)


if __name__ == "__main__":
    main()
