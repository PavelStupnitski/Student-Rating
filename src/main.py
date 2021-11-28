from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from CalcRating import CalcRating
from CalcDebtor import CalcDebtor
import argparse
import sys


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)


def main_ind():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    count = CalcDebtor(students).calc()
    print("Quentity: ", count)


if __name__ == "__main__":
    if sys.argv[2].split(".")[1] == "xml":
        main_ind()
    elif sys.argv[2].split(".")[1] == "txt":
        main()
    else:
        print("Not supported type file")
