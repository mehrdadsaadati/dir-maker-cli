import sys
from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser
from unittest.mock import patch
from dir_maker_cli.models.command import Command


def test_parse():
    parser = SimpleArgParser()
    test_args = ["dir_maker_cli.py", "10"]
    with patch.object(sys, "argv", test_args):
        assert parser.parse() == Command(10)
    test_args = ["dir_maker_cli.py", "2", "10"]
    with patch.object(sys, "argv", test_args):
        assert parser.parse() == Command(10, range_from=2)
    test_args = ["dir_maker_cli.py", "2", "10", "dir_name"]
    with patch.object(sys, "argv", test_args):
        assert parser.parse() == Command(10, range_from=2, container_dir="dir_name")
    test_args = ["dir_maker_cli.py"]
    with patch.object(sys, "argv", test_args):
        assert parser.parse() is None


def test_help():
    parser = SimpleArgParser()
    help = parser.help()
    assert "Directory Maker" in help
