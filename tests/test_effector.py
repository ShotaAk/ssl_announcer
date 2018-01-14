#!/usr/bin/env python

import unittest

from ssl_announcer import effector


class TestEffector(unittest.TestCase):

    def test_sub(self):
        value = 1
        actual = effector.sub_one(value)
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
