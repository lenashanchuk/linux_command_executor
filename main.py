
import argparse
from executor import Executor


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--human", nargs="?", dest="flag", const="human", required=False)
    arg_parser.add_argument("--inode", nargs="?", dest="flag", const="inode", required=False)
    return arg_parser.parse_args()


def main():
    try:
       # args = get_args()
        res = Executor.execute(args.flag)
        print(res)
    except Exception as e:
        print(f"ERROR: {e}")
