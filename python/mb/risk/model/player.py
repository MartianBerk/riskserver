from .cards.missioncard import MissionCard
from .cards.territorycard import TerritoryCard
from .game import Game
from .tools.troopiterator import TroopIterator


class Player:
    def __init__(self, name=None, game=None, mission=None, colour=None, has_dice=None, game_data=None):
        """Player object.

        Args:
            name (str): Player name.
            game (Game): Players game.
            mission (MissionCard): Players mission.
            colour (str): Players colour.
            has_dice (bool): Player holding dice.
            game_data (dict): Players game data.
        """
        if not name or not isinstance(name, str):
            raise TypeError("name must be str")

        if not game or not isinstance(game, Game):
            raise TypeError("game must be Game")

        if not mission or not isinstance(mission, MissionCard):
            raise TypeError("mission must be MissionCard")

        if not colour or not isinstance(colour, str):
            raise TypeError("colour must be str")

        self._name = name
        self._game = game
        self._mission = mission
        self._colour = colour
        self._has_dice = has_dice or False
        self._game_data = game_data or {}

    def has_won(self):
        """Determine if a player has won the game."""
        return False

    def take_troops(self, troops):
        """Take a number of troops. If troops exceeds available, will return available.

        Args:
            troops (int): Number of troops.

        Returns:
            int: Number of troops
        """
        troops = sum([t for t in TroopIterator(self._game_data.get("troops", 0), take=troops)])
        self._game_data["troops"] = self._game_data.get("troops", 0) - troops

        return troops

    @property
    def name(self):
        return self._name

    @property
    def game(self):
        return self._game.id

    @property
    def mission(self):
        return self._mission.mission

    @property
    def colour(self):
        return self._colour

    @property
    def has_dice(self):
        return self._has_dice

    @property
    def cards(self):
        return [TerritoryCard(territory=t["territory"], troop=t["troop"]) for t in self._game_data.get("cards", [])]

    @property
    def territories(self):
        return self._game_data.get("territories", [])

    @property
    def troops(self):
        """Get troop one at a time until no more remain."""
        return self._game_data.get("troops", 0)

    @troops.setter
    def troops(self, value):
        """Add to current troop level."""
        self._game_data["troops"] += value
