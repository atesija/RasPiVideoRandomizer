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

    def test__whitelist_videos__no_whitelist_strings__full_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster"]
    	expected_videos = ["Shin Chan", "Death Note", "Monster"]
    	self.assertEqual(expected_videos, RasPiVideoRandomizer.whitelist_videos(video_list, []))

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

    def test__randomize_videos__four_videos__same_size_list(self):
    	video_list = ["Shin Chan", "Death Note", "Monster", "Rick and Morty"]
    	self.assertEqual(4, len(RasPiVideoRandomizer.randomize_videos(video_list)))

    def test__randomize_videos__four_videos__list_has_same_videos(self):
    	video_list = ["Shin Chan", "Death Note", "Monster", "Rick and Morty"]
    	expected_videos = ["Shin Chan", "Death Note", "Monster", "Rick and Morty"]
    	RasPiVideoRandomizer.randomize_videos(video_list)
    	for video in video_list:
			self.assertTrue(video in expected_videos)

    def test__is_video_order_template_key__mispelled_key__false(self):
        self.assertFalse(RasPiVideoRandomizer.is_video_order_template_key("movee"))

    def test__is_video_order_template_key__key_doesnt_exist__false(self):
        self.assertFalse(RasPiVideoRandomizer.is_video_order_template_key("music"))

    def test__is_video_order_template_key__key_exists__true(self):
        self.assertTrue(RasPiVideoRandomizer.is_video_order_template_key("show"))

    def test__is_video_order_template_key__special_key_exists__true(self):
        self.assertTrue(RasPiVideoRandomizer.is_video_order_template_key("chance"))

    def test__build_video_order__only_keys_in_template__order_is_those_keys(self):
        video_template = ["intro", "lineup", "show", "commercial", "movie"]
        expected_order = ["intro", "lineup", "show", "commercial", "movie"]
        self.assertEqual(expected_order, RasPiVideoRandomizer.build_video_order(video_template))

    def test__build_video_order__template_repeats_key_in_random_range__order_has_key_repeated(self):
        video_template = ["show", "repeat 1 4"]
        possible_expected_orders = [["show"], ["show", "show"], ["show", "show", "show"], ["show", "show", "show", "show"]]
        self.assertTrue(RasPiVideoRandomizer.build_video_order(video_template) in possible_expected_orders)

    def test__build_video_order__template_repeats_key_specific_amount__order_has_key_repeated(self):
        video_template = ["show", "repeat 5"]
        expected_order = ["show", "show", "show", "show", "show"]
        self.assertEqual(expected_order, RasPiVideoRandomizer.build_video_order(video_template))

    def test__build_video_order__template_key_chance_to_be_there__order_may_contain_key(self):
        video_template = ["movie", "chance 20"]
        possible_expected_orders = [[], ["movie"]]
        self.assertTrue(RasPiVideoRandomizer.build_video_order(video_template) in possible_expected_orders)

unittest.main()
