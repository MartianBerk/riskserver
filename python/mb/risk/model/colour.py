class Colour:
    def __init__(self, id=None, colour=None):
        """Colour object.

        Args:
            id (int): Colour ID.
            colour (str): Colour.
        """
        if not id or not isinstance(id, int):
            raise TypeError("id must be int")

        if not colour or not isinstance(colour, str):
            raise TypeError("colour must be str")

        self._id = id
        self._colour = colour

    def dict(self):
        """Return a dictionary representing the Colour."""
        return {
            "id": self._id,
            "colour": self._colour
        }

    @property
    def id(self):
        return self._id

    @property
    def colour(self):
        return self._colour
