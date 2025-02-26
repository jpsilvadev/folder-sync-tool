import os
import shutil
import time
import argparse
import logging
from hashlib import md5


def calc_md5(file_path, chunksize=8192):
    hasher = md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunksize):
            hasher.update(chunk)
    return hasher.hexdigest()


def main():
    pass


if __name__ == "__main__":
    # setup argparse
    parser = argparse.ArgumentParser(description="Folder Sync Tool")
    parser.add_argument(
        "--source",
        "-s",
        type=str,
        required=True,
        help="Source folder path",
    )
    parser.add_argument(
        "--replica",
        "-r",
        type=str,
        required=True,
        help="Replica folder path",
    )
    parser.add_argument(
        "--log",
        "-l",
        type=str,
        required=True,
        help="Log file path",
    )
    parser.add_argument(
        "--interval",
        "-i",
        type=int,
        required=True,
        help="Interval in seconds",
    )
    args = parser.parse_args()

    SOURCE = args.source
    REPLICA = args.replica
    LOG = args.log
    INTERVAL = args.interval

    main()
