import unittest
from url_converter import converter

class TestCharConverter(unittest.TestCase):
    def setUp(self):
        self.converter = converter.CharConverter()

    def test_biject(self):
        for expected in range(1000):
            message = self.converter.encode(expected)
            actual = self.converter.decode(message)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()