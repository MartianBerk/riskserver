from datetime import datetime

from mb.risk.model.game import Game

from mylib.globals import get_global
from mylib.myodbc import MyOdbc


class GameService:
    _db = "risk"

    def __init__(self):
        """Initialise a Game Service object."""
        db_settings = get_global("dbs", GameService._db)

        self._db = MyOdbc.connect(db_settings.get("driver"),
                                  GameService._db,
                                  db_settings.get("location"))

        self._players = []
        self._cards = []

    def new_game(self):
        """Initiate a new game.

        Returns:
            Game: Created game object.
        """
        now = datetime.now()

        game = self._db.insert_get("GAMES", {"started": now})

        return Game(**game)

    def load_game(self, id):
        """Load a previous game.

        Args:
            id (int): The games id.

        Returns:
            Game: Loaded game object.
        """
        game = self._db.get("GAMES", where={"id": id})

        return Game(**game)
