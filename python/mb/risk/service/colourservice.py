from mylib.globals import get_global
from mylib.myodbc import MyOdbc

from mb.risk.model.colour import Colour


class ColourService:
    _db = "risk"

    def __init__(self):
        """ColourService object."""
        db_settings = get_global("dbs", self._db)

        self._db = MyOdbc.connect(db_settings.get("driver"),
                                  ColourService._db,
                                  db_settings.get("location"))

    def list_colours(self):
        """Get a list of colours."""
        return [Colour(**c) for c in self._db.get("COLOURS")]
