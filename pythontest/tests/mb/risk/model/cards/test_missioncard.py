from unittest import TestCase, main

from mb.risk.model.cards.missioncard import MissionCard


class MissionCardTests(TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "id must be int"):
            MissionCard()

        mock_id = 1
        with self.assertRaisesRegex(TypeError, "mission must be a str"):
            MissionCard(id=mock_id)

        mock_mission = "super secret mission"
        with self.assertRaisesRegex(TypeError, "criteria must be a str"):
            MissionCard(id=mock_id, mission=mock_mission)

        mock_criteria = "mission criteria"
        card = MissionCard(id=mock_id, mission=mock_mission, criteria=mock_criteria)
        self.assertEqual(card.id, mock_id)
        self.assertEqual(card.mission, mock_mission)
        self.assertEqual(card.criteria, mock_criteria)


if __name__ == "__main__":
    main()
