from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser
from dir_maker_cli.dir_maker import create_directories


def main():
    """Main function of the app."""

    # create a parser to parse input data
    parser = SimpleArgParser()
    command = parser.parse()
    if command is not None:
        # Create directories based on the user command
        create_directories(command)
    else:
        # parser failed to parse input data. let user know that
        print(parser.help())
    pass


if __name__ == "__main__":
    main()
