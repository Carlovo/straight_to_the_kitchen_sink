from unittest import TestCase
from straight_to_the_kitchen_sink import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello from straight_to_the_kitchen_sink!", hello())
