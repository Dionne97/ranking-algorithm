import unittest
import sys
from unittest.mock import patch, mock_open
from collections import defaultdict
from ranking import parse_match_results, rank_teams, format_output,main


class TestLeagueRanker(unittest.TestCase):
    def test_parse_match_results(self):
        input_data = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
        ]
        expected_scores = {
            "Lions": 5,
            "Snakes": 1,
            "Tarantulas": 6,
            "FC Awesome": 1,
            "Grouches": 0,
        }
        scores = parse_match_results(input_data)
        self.assertEqual(scores, expected_scores)

    def test_rank_teams(self):
        scores = {
            "Lions": 5,
            "Snakes": 1,
            "Tarantulas": 6,
            "FC Awesome": 1,
            "Grouches": 0,
        }
        expected_ranked = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0),
        ]
        ranked = rank_teams(scores)
        self.assertEqual(ranked, expected_ranked)

    def test_format_output(self):
        ranked_teams = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0),
        ]
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        output = format_output(ranked_teams)
        self.assertEqual(output, expected_output)

    def test_integration(self):
        input_data = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
        ]
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        scores = parse_match_results(input_data)
        ranked = rank_teams(scores)
        output = format_output(ranked)
        self.assertEqual(output, expected_output)

    def test_empty_input(self):
        input_data = []
        expected_output = ""
        scores = parse_match_results(input_data)
        ranked = rank_teams(scores)
        output = format_output(ranked)
        self.assertEqual(output, expected_output)

    def test_single_match(self):
        input_data = ["Lions 3, Snakes 1"]
        expected_output = (
            "1. Lions, 3 pts\n"
            "2. Snakes, 0 pts"
        )
        scores = parse_match_results(input_data)
        ranked = rank_teams(scores)
        output = format_output(ranked)
        self.assertEqual(output, expected_output)

    def test_tie_match(self):
        input_data = ["Lions 2, Snakes 2"]
        expected_output = (
            "1. Lions, 1 pt\n"
            "1. Snakes, 1 pt"
        )
        scores = parse_match_results(input_data)
        ranked = rank_teams(scores)
        output = format_output(ranked)
        self.assertEqual(output, expected_output)
    
    def test_read_from_file(self):
        input_data = (
            "Lions 3, Snakes 3\n"
            "Tarantulas 1, FC Awesome 0\n"
            "Lions 1, FC Awesome 1\n"
            "Tarantulas 3, Snakes 1\n"
            "Lions 4, Grouches 0"
        )
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )

        with patch("builtins.open", mock_open(read_data=input_data)):
            with patch("sys.argv", ["league_ranker.py", "input.txt"]):
                with patch("sys.stdout", new_callable=lambda: sys.stdout):
                    with open("input.txt", "r") as file:
                        input_lines = file.read().strip().split("\n")
                    output = main(input_lines)
                    self.assertEqual(output.strip(), expected_output)

    def test_read_from_stdin(self):
        input_data = (
            "Lions 3, Snakes 3\n"
            "Tarantulas 1, FC Awesome 0\n"
            "Lions 1, FC Awesome 1\n"
            "Tarantulas 3, Snakes 1\n"
            "Lions 4, Grouches 0"
        )
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )

        with patch("sys.stdin", mock_open(read_data=input_data)):
            with patch("sys.argv", ["league_ranker.py"]):  # No file argument
                input_lines = input_data.strip().split("\n")
                output = main(input_lines)
                self.assertEqual(output.strip(), expected_output)

    def test_file_not_found(self):
        with patch("sys.argv", ["league_ranker.py", "nonexistent.txt"]):
            with self.assertRaises(FileNotFoundError):
                with open("nonexistent.txt", "r") as file:
                    pass


if __name__ == "__main__":
    unittest.main()
