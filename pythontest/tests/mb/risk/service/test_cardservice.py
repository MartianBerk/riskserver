from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.risk.service.cardservice import CardService


class CardServiceTests(TestCase):
    @patch("mb.risk.service.cardservice.MissionCard")
    def test_load_mission_cards(self, mock_card):
        mock_card.side_effect = lambda **kwargs: kwargs

        mock_db = Mock()
        mock_db.get.return_value = [{"id": 1}, {"id": 2}]

        self.assertListEqual(CardService._load_mission_cards(mock_db),
                             [{"id": 1}, {"id": 2}])

    @patch("mb.risk.service.cardservice.random")
    @patch("mb.risk.service.cardservice.TerritoryCard")
    def test_load_territory_cards(self, mock_card, mock_random):
        mock_card.side_effect = lambda **kwargs: kwargs
        mock_random.shuffle.side_effect = lambda x: x  # ensure shuffle doesn't actually shuffle the lists

        mock_db = Mock()
        mock_db.get.return_value = [{"name": f"mock{i}"} for i in range(0, 42)]

        expected_cards = [{"territory": f"mock{i}", "troop": "infantry"} for i in range(0, 24)]
        expected_cards.extend([{"territory": f"mock{i}", "troop": "cavalry"} for i in range(24, 36)])
        expected_cards.extend([{"territory": f"mock{i}", "troop": "artillery"} for i in range(36, 42)])
        expected_cards.extend([{"territory": f"wild", "troop": "wild"} for _ in range(0, 2)])

        self.assertListEqual(CardService._load_territory_cards(mock_db), expected_cards)

    @patch("mb.risk.service.cardservice.random")
    def test_shuffle_deck(self, mock_random):
        mock_mission_cards = [1, 2, 3]
        mock_territory_cards = [4, 5, 6]
        mock_self = Mock(_mission_cards=mock_mission_cards,
                         _territory_cards=mock_territory_cards)

        # test one - error
        with self.assertRaisesRegex(ValueError, "unknown card_deck"):
            CardService.shuffle_deck(mock_self, "mock")

        # test two - shuffle
        CardService.shuffle_deck(mock_self, "mission")
        mock_random.shuffle.assert_called_with(mock_mission_cards)

        CardService.shuffle_deck(mock_self, "territory")
        mock_random.shuffle.assert_called_with(mock_territory_cards)

    @patch("mb.risk.service.cardservice.random")
    @patch("mb.risk.service.cardservice.CardService._load_territory_cards")
    @patch("mb.risk.service.cardservice.CardService._load_mission_cards")
    @patch("mb.risk.service.cardservice.MyOdbc")
    @patch("mb.risk.service.cardservice.get_global")
    def test_deal(self, mock_global, mock_db, mock_mission_cards, mock_territory_cards, mock_random):
        mock_random.shuffle.side_effect = lambda x: x  # ensure shuffle doesn't actually shuffle the lists
        mock_global.return_value = {"driver": "mock_driver", "location": "mock_location"}
        mock_mission_cards.return_value = [1, 2, 3]
        mock_territory_cards.return_value = ["x", "y", "z"]

        service = CardService.deal()
        self.assertListEqual([service.mission_card for _ in range(0, 3)], [1, 2, 3])
        self.assertListEqual([service.territory_card for _ in range(0, 3)], ["x", "y", "z"])

    @patch("mb.risk.service.cardservice.random")
    @patch("mb.risk.service.cardservice.CardService._load_territory_cards")
    @patch("mb.risk.service.cardservice.CardService._load_mission_cards")
    @patch("mb.risk.service.cardservice.MyOdbc")
    @patch("mb.risk.service.cardservice.get_global")
    def test_load(self, mock_global, mock_db, mock_mission_cards, mock_territory_cards, mock_random):
        mock_random.shuffle.side_effect = lambda x: x  # ensure shuffle doesn't actually shuffle the lists
        mock_global.return_value = {"driver": "mock_driver", "location": "mock_location"}
        mock_mission_cards.return_value = [1, 2, 3]
        mock_territory_cards.return_value = ["x", "y", "z"]

        service = CardService.load([3], ["z"])
        self.assertListEqual([service.mission_card for _ in range(0, 2)], [1, 2])
        self.assertListEqual([service.territory_card for _ in range(0, 2)], ["x", "y"])

    def test_mission_card(self):
        # test one - no cards
        service = CardService(mission_cards=[], territory_cards=[])
        with self.assertRaisesRegex(AttributeError, "no mission cards"):
            _ = service.mission_card

        # test two - one card
        service = CardService(mission_cards=[1], territory_cards=[])
        self.assertEqual(service.mission_card, 1)
        with self.assertRaisesRegex(AttributeError, "no mission cards"):
            _ = service.mission_card

        # test three - more than one card
        service = CardService(mission_cards=[1, 2], territory_cards=[])
        self.assertEqual(service.mission_card, 1)
        self.assertEqual(service.mission_card, 2)

    def test_territory_card(self):
        # test one - no cards
        service = CardService(mission_cards=[], territory_cards=[])
        with self.assertRaisesRegex(AttributeError, "no territory cards"):
            _ = service.territory_card

        # test two - one card
        service = CardService(mission_cards=[], territory_cards=[1])
        self.assertEqual(service.territory_card, 1)
        with self.assertRaisesRegex(AttributeError, "no territory cards"):
            _ = service.territory_card

        # test three - more than one card
        service = CardService(mission_cards=[], territory_cards=[1, 2])
        self.assertEqual(service.territory_card, 1)
        self.assertEqual(service.territory_card, 2)

        # test four - add to deck
        service.territory_card = 1
        self.assertEqual(service.territory_card, 1)
        service.territory_card = 1
        service.territory_card = 2
        self.assertListEqual([service.territory_card, service.territory_card], [1, 2])


if __name__ == "__main__":
    main()
