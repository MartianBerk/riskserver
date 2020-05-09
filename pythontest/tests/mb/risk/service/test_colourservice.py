from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.risk.service.colourservice import ColourService


class ColourServiceTests(TestCase):
    def setUp(self):
        mock_db = Mock()
        mock_db.insert_get.side_effect = lambda *args: args[1]

        patches = {
            "mb.risk.service.playerservice.MyOdbc.connect": mock_db
        }

        for p, d in patches.items():
            patch(p, d).start()

        self.mock_db = mock_db
        self.mock_self = Mock(_db=mock_db)

    def tearDown(self):
        patch.stopall()

    @patch("mb.risk.service.colourservice.get_global")
    def test_init(self, mock_global):
        mock_global.return_value = {"driver": "mock_driver", "location": "mock_location"}

        service = ColourService()
        self.assertEqual(service._db, self.mock_db.return_value)
        self.mock_db.assert_called_with("mock_driver", "risk", "mock_location")

    @patch("mb.risk.service.colourservice.Colour")
    def test_list_colours(self, mock_colour):
        mock_colour.side_effect = lambda **kwargs: kwargs
        self.mock_db.get.return_value = [{"colour": "red"}, {"colour": "blue"}]

        players = ColourService.list_colours(self.mock_self)
        self.assertListEqual(players, [{"colour": "red"}, {"colour": "blue"}])
        self.mock_db.get.assert_called_with("COLOURS")


if __name__ == "__main__":
    main()
