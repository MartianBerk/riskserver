from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.risk.model.game import Game
from mb.risk.model.cards.missioncard import MissionCard
from mb.risk.model.player import Player


class PlayerTests(TestCase):
    def setUp(self):
        mock_game = Mock()
        mock_mission = Mock()

        self.mock_self = Mock(_name="player one",
                              _game=mock_game,
                              _mission=mock_mission,
                              _colour="red",
                              _has_dice=True,
                              _game_data={"troops": 10})

    @patch("mb.risk.model.player.TerritoryCard")
    def test_init(self, mock_territory):
        mock_territory.side_effect = lambda **kwargs: kwargs["territory"] + "." + kwargs["troop"]

        name = "player one"

        game = Mock(spec=Game)
        type(game).id = 1

        mission = Mock(spec=MissionCard,
                       mission="mock mission",
                       criteria="mock criteria")
        colour = "red"
        game_data = {
            "cards": [{"territory": "UK", "troop": "infantry"}],
            "territories": ["UK", "USA"],
            "troops": 10
        }

        with self.assertRaisesRegex(TypeError, "name must be str"):
            Player()

        with self.assertRaisesRegex(TypeError, "game must be Game"):
            Player(name=name)

        with self.assertRaisesRegex(TypeError, "mission must be MissionCard"):
            Player(name=name, game=game)

        with self.assertRaisesRegex(TypeError, "colour must be str"):
            Player(name=name, game=game, mission=mission)

        player = Player(name=name, game=game, mission=mission, colour=colour, game_data=game_data)

        self.assertEqual(player.name, name)
        self.assertEqual(player.game, 1)
        self.assertEqual(player.mission, mission)
        self.assertEqual(player.colour, "red")
        self.assertEqual(player.has_dice, False)
        self.assertEqual(player.cards, ["UK.infantry"])
        self.assertEqual(player.territories, ["UK", "USA"])

        # troops
        self.assertEqual(player.troops, 10)
        player.troops = 10
        self.assertEqual(player.troops, 20)

    def test_take_troops(self):
        # take some
        troops = Player.take_troops(self.mock_self, 2)
        self.assertEqual(troops, 2)

        # take available
        troops = Player.take_troops(self.mock_self, 10)
        self.assertEqual(troops, 8)

        # none left
        troops = Player.take_troops(self.mock_self, 10)
        self.assertEqual(troops, 0)


if __name__ == "__main__":
    main()
