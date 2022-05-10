import argparse
import logging

from wand.image import Image
import os

HEIC_SUFFIX = ".HEIC"
PNG_SUFFIX = ".png"

logging.basicConfig(
    filename='output.log',
    encoding='utf-8',
    level=logging.INFO
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='Source directory', required=True)
    parser.add_argument('-d', '--destination', help='Destination directory')
    parser.add_argument('-r', '--remove', help='Remove original')
    args = parser.parse_args()

    destination = args.source if args.destination is None else args.destination

    for file in os.listdir(args.source):
        source_file = os.path.join(args.source, file)
        destination_file = os.path.join(destination, file.replace(HEIC_SUFFIX, PNG_SUFFIX))

        img = Image(filename=source_file)
        img.format = 'png'
        img.save(filename=destination_file)
        img.close()

        logging.info("Finished processing file %s", destination_file)

        if args.remove:
            os.remove(source_file)
            logging.info("Removed original file %s", source_file)

    logging.info("Finished processing all files")


if __name__ == "__main__":
    main()
