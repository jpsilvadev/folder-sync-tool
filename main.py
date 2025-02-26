import os
import shutil
import time
import argparse
import logging
from hashlib import md5


def calc_md5(file_path, chunksize=8192):
    """
    Calculate the MD5 hash of a file.
    Args:
        file_path (str): Path to the file.
        chunksize (int, optional): Chunk size for reading the file. Defaults to 8192.

    Returns:
        str: MD5 hash of the file.
    """
    hasher = md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunksize):
            hasher.update(chunk)
    return hasher.hexdigest()


def sync(source, replica):
    """
    One way folder synchronization from source to replica.

    Args:
        source (str): Folder path to sync from.
        replica (str): Folder path to sync to.
    """
    for root, _, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)

        # if directory does not exist in replica -> create
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info("Created directory: %s", replica_root)

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)

            # if file does not exist in replica or changes have been made -> copy
            if not os.path.exists(replica_file) or calc_md5(source_file) != calc_md5(
                replica_file
            ):
                shutil.copy2(source_file, replica_file)  # preserve metadata
                logging.info("Copied file: %s -> %s", source_file, replica_file)

    for root, _, files in os.walk(replica):
        rel_path = os.path.relpath(root, replica)
        source_root = os.path.join(source, rel_path)

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_root, file)

            # if file does not exist in source -> delete
            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info("Deleted file: %s", replica_file)

        # if directory does not exist in source -> delete
        if not os.path.exists(source_root):
            shutil.rmtree(root)
            logging.info("Deleted directory: %s", root)


def main():
    # setup logger
    logging.basicConfig(
        filename=LOG,
        filemode="w",  # assuming we want to overwrite the log file if it exists
        level=logging.INFO,
        format="[%(levelname)s] - %(asctime)s - %(message)s",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("[%(levelname)s] - %(asctime)s - %(message)s")
    )
    logging.getLogger().addHandler(console_handler)

    logging.info("Started Folder Synchronization: %s -> %s", SOURCE, REPLICA)

    if not os.path.exists(SOURCE):
        os.makedirs(SOURCE)
        logging.warning(
            "Source directory did not exist. Creating source directory: %s", SOURCE
        )

    try:
        while True:
            sync(SOURCE, REPLICA)
            logging.info(
                "Synchronization complete. Sleeping for %d seconds...", INTERVAL
            )
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        # exit gracefully
        logging.info("Stopped Folder Synchronization. Exiting...")


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

    SOURCE = os.path.abspath(args.source)
    REPLICA = os.path.abspath(args.replica)
    LOG = os.path.abspath(args.log)
    INTERVAL = args.interval

    main()
