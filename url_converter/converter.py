import math
import string

FULL_CHAR = string.ascii_letters + string.digits
IGNORE_CHAR = ['a', 'A', 'e', 'E', 'i', 'I', 'l', '1', 'o', 'O', '0', 'u', 'U']
DEFAULT_TRANS_TABLE = [l for l in FULL_CHAR if l not in IGNORE_CHAR]

class CharConverter:
    def __init__(self, trans_table=None):
        if trans_table:
            self.to_message = trans_table
        else:
            self.to_message = DEFAULT_TRANS_TABLE

        self.to_code = {k: v for v, k in enumerate(self.to_message)}
        self.base = len(self.to_message)
        # print("Completed Init.")

    def encode(self, code):
        if code < 0:
            raise ValueError("Code to translate must be postive integer")

        message = ''
        while code > 0:
            code, remainder = divmod(code, self.base)
            message = self.to_message[remainder] + message
            # print("Message: {}. Remainder: {}. Code: {}.".format(message, remainder, code))
        return message

    def decode(self, message):
        code = 0
        reverse = message[::-1]
        for i, item in enumerate(reverse):
            code += self.to_code[item] * int(math.pow(self.base, i))
        return code

import unittest

class TestCharConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CharConverter()

    def test_biject(self):
        for expected in range(1000):
            message = self.converter.encode(expected)
            actual = self.converter.decode(message)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     converter = CharConverter()
#     for expected in range(1, 1000):
#         message = converter.encode(expected)
#         actual = converter.decode(message)
#         print("Expected: {}. Actual: {}. Message: {}.".format(expected, actual, message))
#         assert (expected == actual)
