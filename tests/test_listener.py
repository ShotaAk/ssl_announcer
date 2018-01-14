#!/usr/bin/env python

import unittest

from ssl_announcer import listener


class TestListener(unittest.TestCase):

    def test_add(self):
        value = 1
        actual = listener.add_two(value)
        expected = 3
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
