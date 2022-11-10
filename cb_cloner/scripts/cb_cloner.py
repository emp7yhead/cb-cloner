#! usr/bin/python3
import logging
from cb_cloner.cloner import copy_and_rename
from cb_cloner.cli import parse_arguments


def main():
    logging.basicConfig(level=logging.INFO)
    directory = parse_arguments()
    copy_and_rename(directory)


if __name__ == '__main__':
    main()
