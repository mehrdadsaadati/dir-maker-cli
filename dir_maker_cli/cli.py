import sys
from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser


def main():
    # read input from args
    input = sys.argv[1:]

    # create a parser to parse input data
    parser = SimpleArgParser()
    command = parser.parse(input)
    if command is not None:
        # pass these params to dir_maker
        pass
    else:
        # parser failed to parse input data. let user know that
        print(parser.help())
    pass


if __name__ == "__main__":
    main()
