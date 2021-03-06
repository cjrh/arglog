import sys
import argparse
import logging
import arglog


parser = argparse.ArgumentParser()
# Absorb all args - we're not going to use it.
parser.add_argument('blah', nargs='*')
# Must use sys because we're testing argparse
arglog.patch(parser, sys.argv[1])
args, known = parser.parse_known_args()
logger = logging.getLogger()
sys.stdout.write(logging.getLevelName(logger.level))
