from unittest import TestCase, main

from mb.risk.model.cards.missioncard import MissionCard


class MissionCardTests(TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "mission must be a str"):
            MissionCard()

        mock_mission = "super secret mission"
        with self.assertRaisesRegex(TypeError, "criteria must be a str"):
            MissionCard(mission=mock_mission)

        mock_criteria = "mission criteria"
        card = MissionCard(mission=mock_mission, criteria=mock_criteria)
        self.assertEqual(card.mission, mock_mission)
        self.assertEqual(card.criteria, mock_criteria)


if __name__ == "__main__":
    main()
