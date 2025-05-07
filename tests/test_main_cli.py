import unittest
from unittest.mock import patch
import builtins
import main

class TestMainCLIMock(unittest.TestCase):
    @patch("builtins.input", side_effect=["3", "4"])  # List currencies, then exit
    def test_list_currencies_then_exit(self, mock_input):
        try:
            main.main()
        except SystemExit:
            pass

    @patch("builtins.input", side_effect=["1", "100", "1", "2", "4"])
    def test_convert_currency_flow(self, mock_input):
        try:
            main.main()
        except SystemExit:
            pass

    @patch("builtins.input", side_effect=["2", "1", "1.5", "4"])  # Update currency, then exit
    def test_update_currency_rate(self, mock_input):
        try:
            main.main()
        except SystemExit:
            pass

    @patch("builtins.input", side_effect=["x"])  # Exit immediately
    def test_exit_immediately(self, mock_input):
        try:
            main.main()
        except SystemExit:
            pass

    @patch("builtins.input", side_effect=["1", "abc", "4"])  # Invalid amount then exit
    def test_invalid_amount_entry(self, mock_input):
        try:
            main.main()
        except SystemExit:
            pass
