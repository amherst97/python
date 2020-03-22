#!/usr/bin/env python3
"""
Test docstring
"""

import sys
import logging
from urllib.request import urlopen
from package1 import module1
from package2 import module2
from package2.package3 import module3

log = logging.getLogger(__name__)


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

        for word in story_words:
            print(word)

        log.info("Done fetch words")


if __name__ == '__main__':
    log.info("Starting the application")
    print(sys.path)
    module1.function1()
    module2.function2()

    #
    module3.function3()
