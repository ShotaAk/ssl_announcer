#!/usr/bin/env python

import unittest

from ssl_announcer import core


class TestCore(unittest.TestCase):

    def test_add(self):
        value = 1
        actual = core.add_one(value)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
