from cleaner_utils import *
import argparse


def cli():
    parser = argparse.ArgumentParser(
        description="Clean and format bibliographic entries."
    )
    parser.add_argument("input_file", help="Path to the input bibliographic file.")
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a backup copy of the original file.",
    )
    return parser.parse_args()


def main():
    args = cli()
    clean_bibliography(file_path=args.input_file, backup=args.backup)

main()


