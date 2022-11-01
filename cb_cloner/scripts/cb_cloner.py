#! usr/bin/python3
import logging
from cb_cloner.cloner import ru_to_en
from cb_cloner.cli import parse_arguments


def main():
    logging.basicConfig(level=logging.INFO)
    directory = parse_arguments()
    ru_to_en(directory)


if __name__ == '__main__':
    main()
