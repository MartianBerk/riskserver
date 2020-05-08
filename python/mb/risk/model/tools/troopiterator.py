class TroopIterator:
    def __init__(self, troops, take=None):
        """Iterator to return troops one at a time until depleted.

        Args:
            troops (int): Number of troops.
            amount (int): Number of troops to take.
        """
        self._troops = min(take, troops) if take else troops
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count >= self._troops:
            raise StopIteration

        self._count += 1
        return 1
