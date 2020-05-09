class MissionCard:
    def __init__(self, id=None, mission=None, criteria=None):
        """A Mission Card object.

        The criteria is a str that corresponds to GameRule.

        Args:
            id (int): Mission Id.
            mission (str): The mission.
            criteria (str): The criteria to complete the mission.
        """
        if not id or not isinstance(id, int):
            raise TypeError("id must be int")

        if not mission or not isinstance(mission, str):
            raise TypeError("mission must be a str")

        if not criteria or not isinstance(criteria, str):
            raise TypeError("criteria must be a str")

        self._id = id
        self._mission = mission
        self._criteria = criteria

    def dict(self):
        """Return a dict representing the MissionCard."""
        return {
            "id": self._id,
            "mission": self._mission
        }

    @property
    def id(self):
        return self._id

    @property
    def mission(self):
        return self._mission

    @property
    def criteria(self):
        return self._criteria
