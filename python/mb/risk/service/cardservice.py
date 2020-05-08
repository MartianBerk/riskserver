from mylib.globals import get_global
from mylib.myodbc import MyOdbc


class CardService:
    _db = "risk"

    def __init__(self):
        """Initialize a Card Service object."""
        db_settings = get_global("dbs", CardService._db)

        self._db = MyOdbc.connect(db_settings.get("driver"),
                                  CardService._db,
                                  db_settings.get("location"))

        self._mission_cards = []
        self._territory_cards = []
