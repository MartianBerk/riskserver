from unittest import TestCase, main

from mb.risk.model.colour import Colour


class ColourTests(TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "id must be int"):
            Colour()

        id = 1
        with self.assertRaisesRegex(TypeError, "colour must be str"):
            Colour(id=id)

        colour_name = "red"
        colour = Colour(id=id, colour=colour_name)
        self.assertEqual(colour.id, id)
        self.assertEqual(colour.colour, colour_name)


if __name__ == "__main__":
    main()
