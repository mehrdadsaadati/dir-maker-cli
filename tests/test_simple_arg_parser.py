from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser
from dir_maker_cli.models.command import Command


def test_parse():
    parser = SimpleArgParser()
    assert parser.parse(["10"]) == Command(10)
    assert parser.parse(["2", "10"]) == Command(10, range_from=2)
    assert parser.parse(["2", "10", "dir_name"]) == Command(
        10, range_from=2, container_dir="dir_name"
    )
    assert parser.parse([]) is None


def test_help():
    parser = SimpleArgParser()
    help = parser.help()
    assert "Directory Maker" in help
