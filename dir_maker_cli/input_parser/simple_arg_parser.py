from dir_maker_cli.models.command import Command
import sys
from dir_maker_cli import get_logger

logger = get_logger(__name__)


class SimpleArgParser:
    """Simple argument parser that extracts data from sys.argv directly"""

    def parse(self) -> Command | None:
        """Simple argument parser that uses sys.argv to process user request

        Parses the user input from sys.argv and creates a Command as response. If failed, prints error message and returns None.

        Parameters
        ----------
            None
                Uses the sys.argv internally

        Returns
        ----------
        Command | None
            Returns a Command with extracted info from args or None if extraction failed

        Raises
            Nothing. ValueError exception is handled internally
        """

        try:
            # ignore the first arg (app name)
            args = sys.argv[1:]
            match args:
                case [range_to]:
                    logger.info(f"Extracted range_to={range_to} from user inputs")
                    return Command(int(range_to))
                case [range_from, range_to]:
                    logger.info(
                        f"Extracted range_from={range_from}, range_to={range_to} from user inputs"
                    )
                    return Command(int(range_to), int(range_from))
                case [range_from, range_to, container_dir]:
                    logger.info(
                        f"Extracted range_from={range_from}, range_to={range_to}, container_dir={container_dir} from user inputs"
                    )
                    return Command(int(range_to), int(range_from), container_dir)
                case [range_from, range_to, container_dir, *_]:  # ignores the rest
                    logger.info(
                        f"Extracted range_from={range_from}, range_to={range_to}, container_dir={container_dir} from user inputs"
                    )
                    return Command(int(range_to), int(range_from), container_dir)
        except ValueError as e:
            logger.error(f"Invalid input type (not a number): {e}")

        logger.error(f"Failed to parse user inputs: {args}")
        return None

    def help(self) -> str:
        """Generates help string of the argument parser

        Generates a help string indicating the usage of this argument parser. Can be printed directly for user.
        """

        # Make sure to contain Directory Maker title in the generated string
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
