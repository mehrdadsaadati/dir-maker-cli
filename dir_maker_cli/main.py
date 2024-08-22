import sys
from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser


def main():
    parser = SimpleArgParser()
    command = parser.parse(sys.argv[1:])
    if command is not None:
        # pass these params to dir_maker
        pass
    else:
        print(parser.help())
    pass


if __name__ == "__main__":
    main()
