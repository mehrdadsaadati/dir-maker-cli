from dir_maker_cli.input_parser.simple_arg_parser import SimpleArgParser


def main():
    # create a parser to parse input data
    parser = SimpleArgParser()
    command = parser.parse()
    if command is not None:
        # pass these params to dir_maker
        pass
    else:
        # parser failed to parse input data. let user know that
        print(parser.help())
    pass


if __name__ == "__main__":
    main()
