from unittest import TestCase, main

from mb.risk.model.cards.territorycard import TerritoryCard


class TerritoryCardTests(TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "territory must be a str"):
            TerritoryCard()

        mock_territory = "mock territory"
        with self.assertRaisesRegex(TypeError, "troop must be a str"):
            TerritoryCard(territory=mock_territory)

        mock_troop = "mock troop"
        card = TerritoryCard(territory=mock_territory, troop=mock_troop)
        self.assertEqual(card.territory, mock_territory)
        self.assertEqual(card.troop, mock_troop)


if __name__ == "__main__":
    main()
