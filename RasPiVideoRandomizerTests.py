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

    def test__whitelist_videos__no_whitelist_strings__empty_list(self):
    	self.assertEqual([], RasPiVideoRandomizer.whitelist_videos(["Shin Chan", "Death Note", "Monster"], []))

    def test__whitelist_videos__no_matching_whitelist_strings__empty_list(self):
    	self.assertEqual([], RasPiVideoRandomizer.whitelist_videos(["Shin Chan", "Death Note", "Monster"], ["Scooby", "Rick and Morty"]))

    def test__whitelist_videos__one_video_matches_whitelist_strings__video_in_list(self):
    	self.assertEqual(["Shin Chan"], RasPiVideoRandomizer.whitelist_videos(["Shin Chan", "Death Note", "Monster"], ["Shin", "Scooby"]))

    def test__whitelist_videos__all_videos_match_whitelist_strings__video_in_list(self):
    	self.assertEqual(["Shin Chan", "Death Note", "Monster"], RasPiVideoRandomizer.whitelist_videos(["Shin Chan", "Death Note", "Monster"], ["Shin", "Death", "Monster"]))

    def test__blacklist_videos__no_blacklist_strings__full_list(self):
    	self.assertEqual(["Shin Chan", "Death Note", "Monster"], RasPiVideoRandomizer.blacklist_videos(["Shin Chan", "Death Note", "Monster"], []))

    def test__blacklist_videos__no_matching_blacklist_strings__full_list(self):
    	self.assertEqual(["Shin Chan", "Death Note", "Monster"], RasPiVideoRandomizer.blacklist_videos(["Shin Chan", "Death Note", "Monster"], ["Scooby", "Rick and Morty"]))

    def test__blacklist_videos__one_video_matches_blacklist_strings__video_not_in_list(self):
    	self.assertEqual(["Death Note", "Monster"], RasPiVideoRandomizer.blacklist_videos(["Shin Chan", "Death Note", "Monster"], ["Shin", "Scooby"]))

    def test__blacklist_videos__all_videos_match_blacklist_strings__empty_list(self):
    	self.assertEqual([], RasPiVideoRandomizer.blacklist_videos(["Shin Chan", "Death Note", "Monster"], ["Shin", "Death", "Monster"]))

unittest.main()
