import logging, sys


class ExtendLog(logging):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    def __init__(self):
        a = 1
