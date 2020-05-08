class MissionCard:
    def __init__(self, mission=None, criteria=None):
        """A Mission Card object.

        The criteria is a str that corresponds to GameRule.

        Args:
            mission (str): The mission.
            criteria (str): The criteria to complete the mission.
        """
        if not mission or not isinstance(mission, str):
            raise TypeError("mission must be a str")

        if not criteria or not isinstance(criteria, str):
            raise TypeError("criteria must be a str")

        # TODO: whitelist criteria values?

        self._mission = mission
        self._criteria = criteria

    @property
    def mission(self):
        return self._mission

    @property
    def criteria(self):
        return self._criteria
