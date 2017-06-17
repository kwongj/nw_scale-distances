#!/usr/bin/env python3
# Script by JK
# Converts/scales distances in Newick trees

import re
import argparse
from argparse import RawTextHelpFormatter
import os
import sys

# Functions
# Log a message to stderr
def msg(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# Log an error to stderr and quit with non-zero error code
def err(*args, **kwargs):
	msg(*args, **kwargs)
	sys.exit(1);

# Check tree file exists and is in Newick format
def check_newick(f):
	if not os.path.isfile(f) or os.path.getsize(f) < 1:
		return False
	with open(f, 'r') as newick:
		if newick.readline()[0] != '(':						# Check if header starts with "("
			return False
	return True

# Usage
parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Converts/scales distances in Newick trees',
	usage='\n  %(prog)s [OPTIONS] newick.tree')
parser.add_argument('nwtree', metavar='nwtree', nargs=1, help='newick tree file')
parser.add_argument('--days', action='store_true', help='output distances in days (for timed phylogeny)')
parser.add_argument('--years', action='store_true', help='output distances in years (for timed phylogeny)')
parser.add_argument('--factor', metavar='FLOAT', nargs=1, help='output distances multiplied by this scale factor')
parser.add_argument('--version', action='version', version='%(prog)s v0.1')
args = parser.parse_args()

if not check_newick(args.nwtree[0]):
	err('ERROR: Check "{}" exists and is in Newick format.'.format(args.nwtree[0]))
with open (args.nwtree[0]) as file:
	for line in file:
		a = re.findall(r':(\d+\.\d+)', line)
		for n in a:
			if args.years:
				line = line.replace(n, str(float(n)/365.2425))
			elif args.days:
				line = line.replace(n, str(float(n)*365.2425))
			elif args.factor:
				line = line.replace(n, str(float(n)*float(args.factor[0])))
			else:
				line = line
		print(line)
