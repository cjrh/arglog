import sys
import argparse
import logging
import arglog


parser = argparse.ArgumentParser()
# Absorb all args - we're not going to use it.
parser.add_argument('blah', nargs='*')
# Must use sys because we're testing argparse
arglog.patch(parser, sys.argv[1])
args = parser.parse_args()
logger = logging.getLogger()
print(logging.getLevelName(logger.level), end='')
