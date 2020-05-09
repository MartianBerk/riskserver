from mylib.globals import get_global
from mylib.myodbc import MyOdbc

from mb.risk.model import Player


class PlayerService:
    _db = "risk"

    def __init__(self, game):
        """Initialize a PlayerService object.

        Args:
            game (Game): A Game object.
        """
        db_settings = get_global("dbs", self._db)

        self._db = MyOdbc.connect(db_settings.get("driver"),
                                  self._db,
                                  db_settings.get("location"),
                                  autocommit=False)
        self._game = game

    def add_player(self, name, colour, mission):
        """Add a player.

        Args:
            name (str): Players name.
            colour (Colour): Colour object.
            mission (MissionCard): MissionCard object.

        Returns:
            Player: The created player.
        """
        player = self._db.insert_get("PLAYERS", {"name": name,
                                                 "game_id": self._game.id,
                                                 "mission_id": mission.id,
                                                 "colour_id": colour.id,
                                                 "has_dice": False,
                                                 "game_data": {"troops": 0,
                                                               "territories": [],
                                                               "cards": []}})

        return Player(**player)

    def list_players(self):
        """List players in a game."""
        return [Player(**p) for p in self._db.get("PLAYERS", where={"game_id": self._game.id})]

    def sync(self):
        """Sync the latest game changes."""
        self._db.commit()
