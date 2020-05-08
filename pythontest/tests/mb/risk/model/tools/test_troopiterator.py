from unittest import TestCase, main

from mb.risk.model.tools.troopiterator import TroopIterator


class TroopIteratorTests(TestCase):
    def test_init(self):
        troops = 100

        # retrieve 10
        self.assertEqual(sum([t for t in TroopIterator(troops, take=10)]), 10)

        # retrieve all
        self.assertEqual(sum([t for t in TroopIterator(troops)]), 100)

        # retrieve available
        self.assertEqual(sum([t for t in TroopIterator(troops, take=1000)]), 100)


if __name__ == "__main__":
    main()
