class TerritoryCard:
    def __init__(self, territory=None, troop=None):
        """A Territory Card object.

        Args:
            territory (str): The territory name.
            troop (str): The troop value for the territory.
        """
        if not territory or not isinstance(territory, str):
            raise TypeError("territory must be a str")

        if not troop or not isinstance(troop, str):
            raise TypeError("troop must be a str")

        # TODO: whitelist territory & troop values?

        self._territory = territory
        self._troop = troop

    @property
    def territory(self):
        return self._territory

    @property
    def troop(self):
        return self._troop
