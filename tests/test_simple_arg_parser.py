from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser
from dir_maker_cli.models.command import Command
from unittest.mock import patch
import sys


def test_parse():
    parser = SimpleArgParser()
    with patch.object(sys, "argv", ["dir_maker_cli", "10"]):
        assert parser.parse() == Command(10)
    with patch.object(sys, "argv", ["dir_maker_cli", "2", "10"]):
        assert parser.parse() == Command(10, range_from=2)
    with patch.object(sys, "argv", ["dir_maker_cli", "2", "10", "dir_name"]):
        assert parser.parse() == Command(10, range_from=2, container_dir="dir_name")
    with patch.object(sys, "argv", ["dir_maker_cli"]):
        assert parser.parse() is None


def test_help():
    parser = SimpleArgParser()
    help = parser.help()
    assert "Directory Maker" in help
