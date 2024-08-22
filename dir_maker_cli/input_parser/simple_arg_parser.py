from dir_maker_cli.models.command import Command
import sys


class SimpleArgParser:
    def parse(self) -> Command | None:
        try:
            args = sys.argv[1:]
            match args:
                case [range_to]:
                    return Command(int(range_to))
                case [range_from, range_to]:
                    return Command(int(range_to), int(range_from))
                case [range_from, range_to, container_dir]:
                    return Command(int(range_to), int(range_from), container_dir)
                case [range_from, range_to, container_dir, *_]:
                    return Command(int(range_to), int(range_from), container_dir)
        except ValueError as e:
            print("Invalid input (not a number):", e)

        print("Failed to read the input:", args)
        return None

    def help(self) -> str:
        return """
Directory Maker:
    Creates a list of directory in current dir or specified container_dir based on the input range numbers.

Options:
1. Specific range start:
    dir_maker_cli range_to
2. Specific range start and end:
    dir_maker_cli range_from range_to
3. Specific range and container directory name:
    dir_maker_cli range_from range_to container_dir
"""
