from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.risk.engine.engine import RiskEngine


class RiskEngineTests(TestCase):
    def setUp(self):
        mock_card_service = Mock()
        mock_game_service = Mock()
        mock_player_service = Mock()

        patches = {
            "mb.risk.engine.engine.CardService": mock_card_service,
            "mb.risk.engine.engine.GameService": mock_game_service,
            "mb.risk.engine.engine.PlayerService": mock_player_service
        }

        for p, d in patches.items():
            patch(p, d).start()

        self.mock_self = Mock(_card_service=mock_card_service,
                              _game_service=mock_game_service,
                              _player_service=mock_player_service)

        self.mock_card_service = mock_card_service
        self.mock_game_service = mock_game_service
        self.mock_player_service = mock_player_service

    def tearDown(self):
        patch.stopall()

    def test_init(self):
        self.mock_card_service.deal.return_value = Mock(mission_card="mock mission",
                                                        territory_card="mock territory")

        risk = RiskEngine()

        self.assertEqual(risk._game_service, self.mock_game_service.return_value)
        self.assertIsNone(risk._card_service)

        self.assertEqual(risk.mission_card, "mock mission")
        self.assertEqual(self.mock_card_service.deal.call_count, 1)

        # check card service not loaded twice
        self.assertEqual(risk.territory_card, "mock territory")
        self.assertEqual(self.mock_card_service.deal.call_count, 1)

    def test_new_game(self):
        self.mock_game_service.new_game.return_value = "mock game"
        self.mock_player_service.return_value = "mock player"

        mock_game = RiskEngine.new_game(self.mock_self)
        self.assertEqual(mock_game, "mock game")

        self.mock_game_service.new_game.assert_called_once()
        self.mock_player_service.asset_called_once_with("mock_game")

    def test_register_players(self):
        self.mock_player_service.add_player.side_effect = lambda *args: "-".join(args)

        # test one - second player erroneous
        mock_players = [{"name": "player one", "colour": "red", "mission": "mission"},
                        {"name": "player two", "colour": "blue"}]

        with self.assertRaisesRegex(ValueError, "player missing 'mission'"):
            RiskEngine.register_players(self.mock_self, mock_players)

            self.mock_player_service.add_player.assert_called_once()
            self.mock_player_service.sync.assert_not_called()

        # test two - success
        self.mock_player_service.reset_mock()
        mock_players = [{"name": "player one", "colour": "red", "mission": "mission"},
                        {"name": "player two", "colour": "blue", "mission": "mission two"}]
        players = RiskEngine.register_players(self.mock_self, mock_players)
        self.assertEqual(players, ["player one-red-mission",
                                   "player two-blue-mission two"])
        self.assertEqual(self.mock_player_service.add_player.call_count, 2)
        self.mock_player_service.sync.assert_called_once()


if __name__ == "__main__":
    main()
