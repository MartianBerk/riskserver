from unittest import TestCase, main

from datetime import datetime

from mb.risk.model.game import Game


class GameTests(TestCase):
    def test_init(self):
        now = datetime.now()

        with self.assertRaisesRegex(TypeError, "id must be int"):
            Game()

        with self.assertRaisesRegex(TypeError, "started must be datetime"):
            Game(id=1)

        game = Game(id=1, started=now)
        self.assertEqual(game.id, 1)
        self.assertEqual(game.started, now)
        self.assertIsNone(game.ended)

        game = Game(id=1, started=now, ended=now)
        self.assertEqual(game.id, 1)
        self.assertEqual(game.started, now)
        self.assertEqual(game.ended, now)


if __name__ == "__main__":
    main()
