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
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual([], RasPiVideoRandomizer.whitelist_videos(video_list, []))

    def test__whitelist_videos__no_matching_whitelist_strings__empty_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual([], RasPiVideoRandomizer.whitelist_videos(video_list, ["Scooby", "Rick and Morty"]))

    def test__whitelist_videos__one_video_matches_whitelist_strings__video_in_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Shin Chan"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.whitelist_videos(video_list, ["Shin", "Scooby"]))

    def test__whitelist_videos__all_videos_match_whitelist_strings__video_in_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.whitelist_videos(video_list, ["Shin", "Death", "Monster"]))

    def test__blacklist_videos__no_blacklist_strings__full_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.blacklist_videos(video_list, []))

    def test__blacklist_videos__no_matching_blacklist_strings__full_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.blacklist_videos(video_list, ["Scooby", "Rick and Morty"]))

    def test__blacklist_videos__one_video_matches_blacklist_strings__video_not_in_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Death Note", "Monster"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.blacklist_videos(video_list, ["Shin", "Scooby"]))

    def test__blacklist_videos__all_videos_match_blacklist_strings__empty_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual([], RasPiVideoRandomizer.blacklist_videos(video_list, ["Shin", "Death", "Monster"]))

    def test__file_is_video__empty_video_string__false(self):
        self.assertFalse(RasPiVideoRandomizer.file_is_video(""))

    def test__file_is_video__mp4_file__true(self):
        self.assertTrue(RasPiVideoRandomizer.file_is_video("Rick and Morty.mp4"))

    def test__file_is_video__mov_file__true(self):
        self.assertTrue(RasPiVideoRandomizer.file_is_video("Rick and Morty.mov"))

    def test__file_is_video__avi_file__true(self):
        self.assertTrue(RasPiVideoRandomizer.file_is_video("Rick and Morty.avi"))

    def test__file_is_video__mkv_file__true(self):
        self.assertTrue(RasPiVideoRandomizer.file_is_video("Rick and Morty.mkv"))

    def test__file_is_video__ogm_file__true(self):
        self.assertTrue(RasPiVideoRandomizer.file_is_video("Rick and Morty.ogm"))

    def test__file_is_video__txt_file__false(self):
        self.assertFalse(RasPiVideoRandomizer.file_is_video("Rick and Morty.txt"))
unittest.main()
