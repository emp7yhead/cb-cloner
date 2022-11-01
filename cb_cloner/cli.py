import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Copy ru files in codebasics to en'
    )
    parser.add_argument('directory')
    args = parser.parse_args()
    return args.directory
