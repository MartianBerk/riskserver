from unittest import TestCase, main
from unittest.mock import Mock, patch

from datetime import datetime

from mb.risk.service.gameservice import GameService


class GameTests(TestCase):
    @patch("mb.risk.service.gameservice.get_global")
    @patch("mb.risk.service.gameservice.MyOdbc")
    def test_init(self, mock_db, mock_global):
        mock_global.return_value = {"driver": "mock_driver",
                                    "location": "mock_location"}

        GameService()

        mock_global.assert_called_with("dbs", "risk")
        mock_db.connect.assert_called_with("mock_driver", "risk", "mock_location")

    @patch("mb.risk.service.gameservice.Game")
    @patch("mb.risk.service.gameservice.datetime")
    def test_new_game(self, mock_datetime, mock_game):
        mock_datetime.now.return_value = datetime(year=2020, month=1, day=1)

        mock_db = Mock()
        mock_db.insert_get.return_value = {"id": 1}

        mock_self = Mock(_db=mock_db)

        game = GameService.new_game(mock_self)

        mock_db.insert_get.assert_called_with("GAMES", {"started": datetime(year=2020, month=1, day=1)})
        mock_game.assert_called_with(id=1)
        self.assertEqual(game, mock_game.return_value)

    @patch("mb.risk.service.gameservice.Game")
    def test_load_game(self, mock_game):
        mock_db = Mock()
        mock_db.get.return_value = {"id": 1}

        mock_self = Mock(_db=mock_db)

        game = GameService.load_game(mock_self, 1)

        mock_db.get.assert_called_with("GAMES", where={"id": 1})
        mock_game.assert_called_with(id=1)
        self.assertEqual(game, mock_game.return_value)


if __name__ == "__main__":
    main()
