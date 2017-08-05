import unittest
import RasPiVideoRandomizer

class RasPiVideoRandomizerTests(unittest.TestCase):
    def setUp(self):
        pass

    def test__video_contains_string__no_strings__false(self):
        self.assertFalse(RasPiVideoRandomizer.video_contains_string("Scooby Doo", []))

    def test__video_contains_string__no_matching_strings__false(self):
        self.assertFalse(RasPiVideoRandomizer.video_contains_string("Scooby Doo", ["Gundam", "Shin Chan"]))

    def test__video_contains_string__matching_string__true(self):
        self.assertTrue(RasPiVideoRandomizer.video_contains_string("Scooby Doo", ["Scooby"]))

    def test__video_contains_string__multiple_matching_strings__true(self):
        self.assertTrue(RasPiVideoRandomizer.video_contains_string("Scooby Doo", ["Scooby", "Doo"]))

    def test__video_contains_string__matching_string_and_non_matching_string__true(self):
        self.assertTrue(RasPiVideoRandomizer.video_contains_string("Scooby Doo", ["Gundam", "Doo"]))

unittest.main()
