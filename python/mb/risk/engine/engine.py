from mb.risk.service.cardservice import CardService
from mb.risk.service.gameservice import GameService
from mb.risk.service.playerservice import PlayerService


class RiskEngine:
    def __init__(self):
        """Risk Game Engine."""
        self._card_service = None
        self._player_service = None
        self._game_service = GameService()

    def new_game(self):
        """Launch new game."""
        game = self._game_service.new_game()
        self._player_service = PlayerService(game)

        return game

    def register_players(self, players):
        """Register players to a game.

        Args:
            players (list): List of dictionaries containing player data.
        """
        playing = []

        try:
            for player in players:
                playing.append(self._player_service.add_player(player["name"], player["colour"], player["mission"]))
        except KeyError as e:
            raise ValueError(f"player missing {str(e)}")

        self._player_service.sync()
        return playing

    @property
    def mission_card(self):
        if not self._card_service:
            self._card_service = CardService.deal()

        return self._card_service.mission_card

    @property
    def territory_card(self):
        if not self._card_service:
            self._card_service = CardService.deal()

        return self._card_service.territory_card
