from datetime import datetime as Datetime


class Game:
    def __init__(self, id=None, started=None, ended=None):
        """Represent a game object.

        Args:
            id (int): The game id.
            started (datetime): Started.
            ended (datetime): Ended.
        """
        if not id or not isinstance(id, int):
            raise TypeError("id must be int")

        if not started or not isinstance(started, Datetime):
            raise TypeError("started must be datetime")

        self._id = id
        self._started = started
        self._ended = ended

    @property
    def id(self):
        return self._id

    @property
    def started(self):
        return self._started

    @property
    def ended(self):
        return self._ended
