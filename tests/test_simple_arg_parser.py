from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser
from dir_maker_cli.models.command import Command
from unittest.mock import patch
import sys


def test_parse():
    """Test the argument parser with different argument sets"""

    parser = SimpleArgParser()

    # test with range_to argument
    with patch.object(sys, "argv", ["dir_maker_cli", "10"]):
        assert parser.parse() == Command(10)

    # test with range_from, range_to arguments
    with patch.object(sys, "argv", ["dir_maker_cli", "2", "10"]):
        assert parser.parse() == Command(10, range_from=2)

    # test with range_from, range_to and container_dir arguments
    with patch.object(sys, "argv", ["dir_maker_cli", "2", "10", "dir_name"]):
        assert parser.parse() == Command(10, range_from=2, container_dir="dir_name")

    # test with no arguments
    with patch.object(sys, "argv", ["dir_maker_cli"]):
        assert parser.parse() is None


def test_help():
    """Test help generation of arg parser"""

    parser = SimpleArgParser()
    help = parser.help()

    # Make sure help string is generated and contains the Directory Maker title
    assert "Directory Maker" in help
