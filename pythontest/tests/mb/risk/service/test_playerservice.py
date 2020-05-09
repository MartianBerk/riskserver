from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.risk.model.game import Game
from mb.risk.service.playerservice import PlayerService


class PlayerServiceTests(TestCase):
    def setUp(self):
        mock_game = Mock(spec=Game)
        type(mock_game).id = 1

        mock_db = Mock()
        mock_db.insert_get.side_effect = lambda *args: args[1]

        mock_player = Mock()
        mock_player.side_effect = lambda **kwargs: kwargs

        patches = {
            "mb.risk.service.playerservice.MyOdbc.connect": mock_db,
            "mb.risk.service.playerservice.Player": mock_player
        }

        for p, d in patches.items():
            patch(p, d).start()

        self.mock_db = mock_db
        self.mock_self = Mock(_game=mock_game,
                              _db=mock_db)

    def tearDown(self):
        patch.stopall()

    @patch("mb.risk.service.playerservice.get_global")
    def test_init(self, mock_global):
        mock_global.return_value = {"driver": "mock_driver", "location": "mock_location"}

        mock_game = Mock(spec=Game)

        service = PlayerService(mock_game)
        self.assertEqual(service._game, mock_game)
        self.assertEqual(service._db, self.mock_db.return_value)
        self.mock_db.assert_called_with("mock_driver", "risk", "mock_location", autocommit=False)

    def test_add_player(self):
        mock_colour = Mock()
        type(mock_colour).id = 1

        mock_mission = Mock()
        type(mock_mission).id = 1

        player = PlayerService.add_player(self.mock_self, "player one", mock_colour, mock_mission)
        self.assertDictEqual(player, {"name": "player one",
                                      "game_id": 1,
                                      "mission_id": 1,
                                      "colour_id": 1,
                                      "has_dice": False,
                                      "game_data": {"troops": 0,
                                                    "territories": [],
                                                    "cards": []}})
        self.mock_db.insert_get.assert_called_with("PLAYERS", {"name": "player one",
                                                               "game_id": 1,
                                                               "mission_id": 1,
                                                               "colour_id": 1,
                                                               "has_dice": False,
                                                               "game_data": {"troops": 0,
                                                                             "territories": [],
                                                                             "cards": []}})

    def test_list_players(self):
        self.mock_db.get.return_value = [{"name": "player one"}, {"name": "player two"}]

        players = PlayerService.list_players(self.mock_self)
        self.assertListEqual(players, [{"name": "player one"}, {"name": "player two"}])
        self.mock_db.get.assert_called_with("PLAYERS", where={"game_id": 1})

    def test_sync(self):
        PlayerService.sync(self.mock_self)
        self.mock_db.commit.assert_called_once()


if __name__ == "__main__":
    main()
